
import socket

HOST = '127.0.0.1'  
PORT = 5000         


def client_initialize():
    try:
       
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        cliente.connect((HOST, PORT))
        print(f"Conectado al servidor en {HOST}:{PORT}")

        while True:
            message = input("Escriba un mensaje. Si quiere salir, escriba 'éxito': ")
            
            if message == "":
                print("El message está vacío. Por favor, vuelva a intentarlo.")
                continue
            
            if message.lower() in ["exito", "éxito"]:
                break

            cliente.sendall(message.encode('utf-8'))
            
            respuesta = cliente.recv(1024).decode('utf-8')
            
            print(f"Respuesta del servidor: {respuesta}")

        cliente.close()
        print("Conexión cerrada")
    except socket.error as e:
      
        print(f"Error de conexión: {e}")



if __name__ == "__main__":
    client_initialize()
