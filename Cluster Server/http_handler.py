import time
from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        paths={
            '/' : {'status':200},
            '/index.html' : {'status':200},
            '/status' : {'status':200}
        }

        if self.path in paths:
            self.respond(paths[self.path])
        else:
            self.respond({'status':404})

    def handle_http(self, status_code, path):
        if '/status' in path and status_code == 200:
            self.send_response(status_code)
            self.send_header('Content-type', 'text/event-stream')
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()

            content = str(time.asctime()) + ' Time'
        else:
            self.send_response(status_code)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            if '.html' in path and status_code == 200:
                with open('html' + path) as file:
                    content = file.read()
                    file.close()
            elif '.html' not in path and status_code == 200:
                with open('html' + path + '/index.html') as file:
                    content = file.read()
                    file.close()
            else:
                with open('html/' + str(status_code) + '.html') as file:
                    content = file.read()
                    file.close()

        return bytes(content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['status'], self.path)
        self.wfile.write(response)