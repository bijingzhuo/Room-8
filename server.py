import http.server
import json
import socketserver


cities = [
    "Helsinki",
    "Espoo",
    "Tampere",
    "Vantaa",
    "Oulu",
    "Turku",
    "Jyväskylä"
]

class RESTRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        self.wfile.write(json.dumps(cities).encode())


port = 9091
httpd = socketserver.TCPServer(("", port), RESTRequestHandler)

print(f"REST Services running on port {port}")
httpd.serve_forever()

