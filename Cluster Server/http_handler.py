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
            '/status' : {'status':200}
        }

        if self.path in paths:
            self.respond(paths[self.path])
        else:
            self.respond({'status':404})

    def handle_http(self, status_code, path):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        content = '''
            <!DOCTYPE html>
            <html>
            <body>

            <h1>Getting server updates</h1>
            <p></p>
            <div id="result"></div>

            <script>
            if(typeof(EventSource) !== "undefined") {
                var source = new EventSource("demo_sse.php");
                source.onmessage = function(event) {
                    document.getElementById("result").innerHTML = event.data + "<br>";
                };
            } else {
                document.getElementById("result").innerHTML = "Sorry, your browser does not support server-sent events...";
            }
            </script>

            </body>
            </html>
        '''

        return bytes(content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['status'], self.path)
        self.wfile.write(response)