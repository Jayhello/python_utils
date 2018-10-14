# coding:utf-8

import socket
import select


class MyBaseServer:
    def __init__(self, server_address, RequestHandlerClass):
        """Constructor, Maybe extended, do not override."""
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass

        self.__shutdown_request = False

    def server_activate(self):
        """Called by constructor to activate the server.
        Maybe overridden
        """
        pass

    def server_forever(self, poll_interval=0.5):
        """Handle one request at a time until shutdown"""
        try:
            while not self.__shutdown_request:
                r, w, e = select.select([self], [], [], poll_interval)

                if self in r:
                    self._handle_request_noblock()
        finally:
            self.__shutdown_request = True

    def shutdown(self):
        """Stop the server_forever loop.

        """
        self.__shutdown_request = True

    def handle_request(self):
        pass

    def _handle_request_noblock(self):
        """Handle one request, without blocking

        :return:
        """
        try:
            # get_request sub server return by accept method
            request, client_address = self.get_request()
            try:
                self.process_request(request, client_address)
            except:
                self.handle_error(request, client_address)
                self.shutdown_request(request)

        except socket.error:
            return

    def verify_request(self, request, client_address):
        """Verify the request.  May be overridden.

        Return True if we should proceed with this request.

        """
        return True

    def handle_error(self, request, client_address):
        """
        Handle an error gracefully. May be overridden.

        The default is to print a traceback and continue
        :param request: request socket
        :param client_address:
        """
        print '-'*40
        print 'Exception happened during processing of request from',
        print client_address
        import traceback
        traceback.print_exc()  # XXX But this goes to stderr!
        print '-'*40

    def server_close(self):
        """Called to clean up the server

        May be overridden.
        """
        pass

    def shutdown_request(self, request):
        """Called to shutdown and close an individual request."""
        self.close_request(request)

    def close_request(self, request):
        """Called to clean up an individual request."""
        pass

    def process_request(self, request, client_address):
        """Call finish_request.

        Overridden by ForkingMixIn and ThreadingMixIn.

        """
        self.finish_request(request, client_address)
        self.shutdown_request(request)

    def finish_request(self, request, client_address):
        """Finish one request by instantiating RequestHandlerClass."""
        self.RequestHandlerClass(request, client_address, self)


class MyTCPServer(MyBaseServer):
    address_family = socket.AF_INET

    socket_type = socket.SOCK_STREAM

    request_queue_size = 5

    allow_reuse_address = False

    def __init__(self, server_address, RequestHandlerClass,
                 bind_and_activate=True):
        """Constructor.  May be extended, do not override."""
        MyBaseServer.__init__(self, server_address, RequestHandlerClass)

        self.socket = socket.socket(self.address_family,
                                    self.socket_type)

        if bind_and_activate:
            try:
                self.server_bind()
                self.server_activate()
            except:
                self.server_close()
                raise

    def server_bind(self):
        """Called by constructor to bind the socket

        May be overridden
        """
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.socket.bind(self.server_address)
        # self.server_address = self.socket.getsockname()

    def server_activate(self):
        """Called by the constructor to activate the server
        May be overridden.
        """

        self.socket.listen(self.request_queue_size)

    def server_close(self):
        """Called to clean up the server

        May be overridden
        """
        self.socket.close()

    def fileno(self):
        """Return socket file number

        Interface required by select()
        """
        return self.socket.fileno()

    def get_request(self):
        """Get the request and client address from the socket

        May be overridden
        """
        return self.socket.accept()

    def shutdown_request(self, request):
        try:
            request.shutdown(socket.SHUT_WR)
        except socket.error:
            pass

        self.close_request(request)

    def close_request(self, request):
        """Called to clean up an individual request"""
        request.close()


class MyBaseRequestHandler:
    def __init__(self, request, client_address, server):
        self.request = request
        self.client_address = client_address
        self.server = server

        self.setup()
        try:
            self.handle()
        finally:
            self.finish()

    def setup(self):
        pass

    def handle(self):
        pass

    def finish(self):
        pass


class MyStreamRequestHandler(MyBaseRequestHandler):
    rbufsize = -1
    wbufsize = 0

    def setup(self):
        self.connection = self.request
        self.rfile = self.connection.makefile('rb', self.rbufsize)
        self.wfile = self.connection.makefile('wb', self.wbufsize)

    def finish(self):
        if not self.wfile.closed:
            try:
                self.wfile.flush()
            except socket.error:
                # A final socket error may have occurred here, such as
                # the local error ECONNABORTED.
                pass
        self.wfile.close()
        self.rfile.close()


if __name__ == '__main__':
    import httplib
    import SimpleHTTPServer
    import SimpleXMLRPCServer
    # test for socket default timeout
    sock = socket.socket()
    print sock.gettimeout()
    # None

    # print socket name
    sock.bind(('', 8888))
    print sock.getsockname()

    # set timeout = 1
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print sock.gettimeout()

    pass
