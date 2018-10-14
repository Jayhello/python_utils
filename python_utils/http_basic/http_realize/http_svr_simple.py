# _*_coding:utf-8 _*_

import BaseHTTPServer


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    Page = '''
    <html>
        <body>
            <p>Hello World</p>
        </body>
    </html>
    '''

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page)


if __name__ == '__main__':
    serverAddress = ('', 8888)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
