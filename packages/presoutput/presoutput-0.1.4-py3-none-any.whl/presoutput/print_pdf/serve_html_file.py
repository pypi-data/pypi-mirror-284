import http.server
import socketserver
import threading
import os


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    html_file = None
    base_dir = None

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def translate_path(self, path):
        # Serve the requested file if it exists, otherwise serve the HTML file
        requested_path = os.path.join(MyHttpRequestHandler.base_dir, path.lstrip("/"))
        if os.path.exists(requested_path) and not os.path.isdir(requested_path):
            return requested_path
        else:
            return os.path.join(MyHttpRequestHandler.base_dir, MyHttpRequestHandler.html_file)

    def log_message(self, format, *args):
        self.server.log(f"Server: {format % args}")


class LocalWebServer:
    def __init__(self, html_file, port=8000, verbose=0):
        MyHttpRequestHandler.html_file = os.path.basename(html_file)
        MyHttpRequestHandler.base_dir = os.path.dirname(os.path.abspath(html_file))
        self.port = port
        self.verbose = verbose
        self.server_thread = None
        self.httpd = None

    def _log(self, message):
        if self.verbose >= 1:
            print(message)

    def start(self):
        if not self.server_thread or not self.server_thread.is_alive():
            self.httpd = socketserver.TCPServer(("", self.port), MyHttpRequestHandler)
            self.httpd.log = self._log  # Assign _log method to server.log
            self.server_thread = threading.Thread(target=self.httpd.serve_forever)
            self.server_thread.daemon = True
            self.server_thread.start()
            self._log(
                f"Server started at port {self.port}. Serving {MyHttpRequestHandler.html_file}"
            )

    def close(self):
        if self.server_thread and self.server_thread.is_alive():
            self.httpd.shutdown()
            self.httpd.server_close()
            self.server_thread.join()
            self._log("Server closed.")