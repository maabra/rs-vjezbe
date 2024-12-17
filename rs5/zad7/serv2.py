from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import math

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/umnozak':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            if 'brojevi' not in data:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'error': 'Nisu proslijeđeni brojevi'}
                self.wfile.write(json.dumps(response).encode())
                return

            umnozak = math.prod(data['brojevi'])
            response = {'umnozak': umnozak}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=Handler, port=8084):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
