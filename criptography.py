from cryptography.fernet import Fernet #Importamos fernet

key = Fernet.generate_key()
code = Fernet(key)

susurro = "Esto es un secreto, que nadie lo sepa"

mensaje = susurro.encode() #Con .encode() covertimos el mensaje en bytes por que Fernet solo trabaja con binarios

print("\n-----------------------------------")
print("-----------------------------------")
print("-----------------------------------")
print("Mensaje a Cifrar:", susurro)
print("-----------------------------------")
print("-----------------------------------")
print("----------------------------------- \n")

secreto = code.encrypt(mensaje)

print("ooooooooooooooooooooooooooooooooooo")
print("Susurro cifrado:", secreto)
print("ooooooooooooooooooooooooooooooooooo \n" )

detective = code.decrypt(secreto).decode()  #con decrypt(variable del mensaje cifrado) devuelve el resultado de bytes
                                            #con decode devuelve el resultado a string.

print("+++++++++++++++++++++++++++++++++++")
print("El detective a descifrado el mensaje")
print(f"Detective: El mensaje dice \"{detective}\" .")
print("+++++++++++++++++++++++++++++++++++ \n")
