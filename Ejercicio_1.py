
import os
os.system('cls' if os.name == 'nt' else 'clear')

saludo="Hola_Mundo"

try:
    print(saludo.index('o',4,7))
except ValueError:
    print('No se encontro la subcadena')

cedula="1613200500141"
departamento=cedula[0:2]
print(departamento)
municipio=cedula[0:4]

print(saludo[0:4])

mensaje="Hola"
mensaje2="Hola Mundo"
numero="123456"
decimales="3.99"

mensaje="London is Red"
print(mensaje.split(" "))

nombre="Anthony*Joseph*Gutierrez*Amaya"
print(nombre.split("*"))
print(nombre.count("*"))

nombreI=nombre.replace("*"," ")
print(nombreI)