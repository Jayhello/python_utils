import sys, os, BaseHTTPServer


class ServerException(Exception):
    '''For internal error reporting.'''
    pass


class CaseNoFile(object):
    @staticmethod
    def test(handler):
        return not os.path.exists(handler.full_path)

    @staticmethod
    def act(handler):
        raise ServerException({"'{0}' not found".format(handler.full_path)})


class CaseExistFile(object):
    @staticmethod
    def test(handler):
        return os.path.isfile(handler.full_path)

    @staticmethod
    def act(handler):
        handler.handle_file(handler.full_path)


class CaseError(object):
    @staticmethod
    def test(handler):
        return True

    @staticmethod
    def act(handler):
        raise ServerException("'{0}' unknown object".format(handler.full_path))


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    CasesLst = [CaseNoFile, CaseExistFile, CaseError]

    Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """

    def do_GET(self):
        try:
            self.full_path = os.getcwd() + self.path
            for case in self.CasesLst:
                if case.test(self):
                    case.act(self)
                    break

        except Exception as msg:
            self.handle_error(msg)

    def handle_file(self, path):
        try:
            with open(path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content)

    def send_content(self, content):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

if __name__ == '__main__':
    serverAddress = ('', 8888)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
