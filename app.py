from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, Docker World!")

httpd = HTTPServer(('0.0.0.0', 8080), Handler)
print("서버 시작! 포트 8080")
httpd.serve_forever()
