import os
from http.server import BaseHTTPRequestHandler, HTTPServer

MESSAGE = "Hello from ShipIt Weekend!"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"<h1>{MESSAGE}</h1><p>Built with Docker, shipped to Azure, automated with GitHub Actions.</p>".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


HTTPServer(("0.0.0.0", int(os.environ.get("PORT", "8080"))), Handler).serve_forever()
