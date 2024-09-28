import socket
import random

def obtener_datos():
    datos = []
    while len(datos) < 30:
        try:
            numero = random.randint(-99,99)
            if 10 <= numero <= 99:
                datos.append(numero)
            else:
                print(f"Error: El número {numero} debe tener 2 cifras.")
            if numero < 0:
                print(f"El número {numero} es un número negativo. Por lo tanto no se pondrá en el arbol binario")

        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
    enviar_lista_de_numeros(datos)

def enviar_lista_de_numeros(datos):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 7536))
    client_socket.send(str(datos).encode())
    client_socket.close()


def main():
    obtener_datos()


if __name__ == "__main__":
    main()
