import socket
from db import db_initialize, save_msg

HOST = '127.0.0.1'
PORT = 5000

def socket_initialize():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Servidor escuchando en {HOST}:{PORT}")
        return server
    except socket.error as e:
        print(f"Error al configurar el socket: {e}")
        return None  

def client(client_socket, direction):
    try:
        while True:
            mensaje = client_socket.recv(1024).decode('utf-8')
            if not mensaje:
                break
            print(f"Mensaje recibido de {direction}: {mensaje}")

            fecha_envio = save_msg(mensaje, direction[0])
            if fecha_envio:
                respuesta = f"Mensaje recibido: {fecha_envio}"
            else:
                respuesta = "Error: no se pudo guardar el mensaje."

            client_socket.sendall(respuesta.encode('utf-8'))
            
    except socket.error as e:
        print(f"Error en la conexión con {direction}: {e}")
    finally:
        client_socket.close()
        print(f"Conexión cerrada con {direction}")

def accept_connections(server):
    while True:
        client_socket, direction = server.accept()
        print(f"Conexión aceptada de {direction}")
        client(client_socket, direction)



if __name__ == "__main__":
    if not db_initialize():
        print("No se pudo inicializar la base de datos. Se cerrará el servidor")
    else:
        server = socket_initialize()
        if server is None:
            print("No se pudo inicializar el socket. Se cerrará el servidor")
        else:
            accept_connections(server)