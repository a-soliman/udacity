from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            print(self.path)
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body><h1>Hello!</h1></body></html>" 
                self.wfile.write(bytes(output, 'utf8'))
                print(output)
                return
        except IOError:
            self.send_error(404, "File Not Found {}".format(self.path))

def main():
    try:
        port = 8081
        server = HTTPServer(('', port), webserverHandler)
        print("Webserver running on port {}".format(port))
        server.serve_forever()

    except KeyboardInterrupt:
        print("^C entered, stopping web server...")
        server.socket.close()



if __name__ == '__main__':
    main()