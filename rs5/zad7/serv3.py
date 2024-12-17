from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/kolicnik':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            if 'zbroj' not in data or 'umnozak' not in data:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'error': 'Nedostaju podaci za zbroj ili umnozak'}
                self.wfile.write(json.dumps(response).encode())
                return

            zbroj = data['zbroj']
            umnozak = data['umnozak']

            if zbroj == 0:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'error': 'Dijeljenje s 0 nije dozvoljeno'}
                self.wfile.write(json.dumps(response).encode())
                return

            kolicnik = umnozak / zbroj
            response = {'kolicnik': kolicnik}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=Handler, port=8085):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
