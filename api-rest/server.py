from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class RestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Servir el archivo HTML para la interfaz
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            with open("index.html", "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404)

    def do_POST(self):
        # Verificar que la ruta sea la correcta para la API
        if self.path == '/api/nombre':
            # 1. Leer el cuerpo de la petición
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            # 2. Decodificar el JSON recibido
            data = json.loads(post_data.decode('utf-8'))
            nombre_recibido = data.get("nombre", "Invitado")

            # 3. Preparar la respuesta JSON
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            # CORS para permitir peticiones (útil si usas puertos distintos)
            self.send_header('Access-Control-Allow-Origin', '*') 
            self.end_headers()

            respuesta = {
                "mensaje": f"¡Hola {nombre_recibido}!",
                "status": "success",
                "servidor": "Python http.server"
            }
            
            # 4. Enviar respuesta
            self.wfile.write(json.dumps(respuesta).encode('utf-8'))
        else:
            self.send_error(404)

if __name__ == "__main__":
    server = HTTPServer(('localhost', 8000), RestHandler)
    print("API REST corriendo en http://localhost:8000")
    server.serve_forever()