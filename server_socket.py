import socket
from tree import ArbolBinario
from utils import insert_numbers_in_list
"""
# Crear un socket de servidor TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket a la dirección y puerto
server_address = ("localhost", 7536)
server_socket.bind(server_address)

# Escuchar conexiones entrantes
server_socket.listen(5)
print(f"Servidor escuchando en {server_address}")
"""
values = insert_numbers_in_list()
print(f"campos sin ordenar {values}")
arbol = ArbolBinario()
for value in values:

    """
    # Esperar a que un cliente se conecte
    print("Esperando conexión de un cliente...")
    connection, client_address = server_socket.accept()
    print(f"Conexión establecida con: {client_address}")

    # Recibir los datos en fragmentos
    data = connection.recv(1024)
    if data:
        received_message = data.decode()
        print(f"Recibido: {received_message}")
        # Separar los números usando el delimitador
        numbers_str = received_message.split(",")
    """ 
    arbol.insertar(value)

    # Responder al cliente
    message_to_send_to_client = f"Mensaje recibido. Se han insertado los datos del árbol binario"
    # connection.sendall(message_to_send_to_client.encode())
arbol.recorrer_inorden()
