
#!/usr/bin/env python3
"""
Very simple HTTP server responding to user with Get request information
Usage::
    ./pywai.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import pprint

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(pprint.pformat(self.headers)))
        self._set_response()
        headerinfo=pprint.pformat(self.headers.items())
        clientinfo=pprint.pformat(self.client_address)
        lineinfo=pprint.pformat(self.requestline)
        versioninfo=pprint.pformat(self.request_version)
        self.wfile.write("<pre> {} </pre>".format(headerinfo).encode('utf-8'))
        self.wfile.write("<pre> {} </pre>".format(clientinfo).encode('utf-8'))
        self.wfile.write("<pre> {} </pre>".format(lineinfo).encode('utf-8'))
        self.wfile.write("<pre> {} </pre>".format(versioninfo).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
