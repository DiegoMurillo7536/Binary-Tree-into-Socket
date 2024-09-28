import socket
from tree import ArbolBinario
# Crear un socket de servidor TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket a la dirección y puerto
server_address = ("localhost", 7536)
server_socket.bind(server_address)

# Escuchar conexiones entrantes
server_socket.listen(5)
print(f"Servidor escuchando en {server_address}")

# Instancia del arbol y lista de datos que se le enviarán al arbol
arbol = ArbolBinario()
data_list = []


while len(data_list) < 30:
    # Esperar a que un cliente se conecte
    print("Esperando conexión de un cliente...")
    connection, client_address = server_socket.accept()
    print(f"Conexión establecida con: {client_address}")

    # Recibir los datos en fragmentos
    data = connection.recv(1024)
    if data:
        received_message = data.decode()
        print(f"Recibido: {received_message}")
        data_list = eval(data)
        for number in range(len(data_list)):
            arbol.insertar(data_list[number])
        arbol.recorrer_inorden()

    message_to_send_to_client = (
        f"Mensaje recibido. Se han insertado los datos al árbol binario"
    )
    connection.sendall(message_to_send_to_client.encode())
