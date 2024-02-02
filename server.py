import http.server
import socketserver

# Define el puerto en el que se ejecutará el servidor
puerto = 8000

# Configura el manejador del servidor para servir archivos estáticos
handler = http.server.SimpleHTTPRequestHandler

# Crea el servidor en el puerto especificado
with socketserver.TCPServer(("", puerto), handler) as httpd:
    print(f"Servidor web activo en el puerto {puerto}")
    # Mantén el servidor en funcionamiento
    httpd.serve_forever()
