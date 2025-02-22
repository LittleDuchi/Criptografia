import streamlit as st  # Streamlit para crear la interfaz web
import os
from cryptography.fernet import Fernet #Importamos fernet

# Generar clave AES de 16 bytes
key = Fernet.generate_key()
code = Fernet(key)

# Solicitar el texto a cifrar por consola
texto = input("Introduce el texto a cifrar: ")

mensaje = texto.encode() 

#texto ya cifrado
secreto = code.encrypt(mensaje)

# Crear el objeto para descifrar
mensaje_descifrado =code.decrypt(secreto).decode()

# Crear la carpeta si no existe
if not os.path.exists("archivos"):
    os.makedirs("archivos")

# Guardar el texto original en un archivo
with open("archivos/texto_original.txt", "w") as f:
    f.write(texto)

# Guardar el texto cifrado en un archivo
with open("archivos/texto_cifrado.txt", "wb") as f:
    f.write(secreto)

print("Texto cifrado guardado como 'archivos/texto_cifrado.txt'")


try:
    # Descifrar y verificar
    mensaje_descifrado = code.decrypt(secreto).decode()

    # Guardar el texto descifrado en un archivo
    with open("archivos/texto_descifrado.txt", "w") as f:
        f.write(mensaje_descifrado)

    print("Texto descifrado guardado como 'archivos/texto_descifrado.txt'")

except ValueError:
    print("Error: El texto cifrado no es válido o la clave es incorrecta.")
