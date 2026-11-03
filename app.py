import os
from http.server import BaseHTTPRequestHandler, HTTPServer

MESSAGE = "Shipped automatically by GitHub Actions!"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"<h1>{MESSAGE}</h1><p>Built with Docker, shipped to Azure, automated with GitHub Actions.</p>".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


HTTPServer(("0.0.0.0", int(os.environ.get("PORT", "8080"))), Handler).serve_forever()





<a href="https://skill-sch.com/certificate/shipit-efa9145a74e4" target="_blank" rel="noopener" title="Verified ShipIt Weekend credential"><img src="https://skill-sch.com/badges/shipit-weekend-2026.png" alt="ShipIt Weekend 2026 · Verified by SKILL.SCH" width="120" height="120"></a>