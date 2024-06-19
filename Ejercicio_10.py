import os
os.system('cls' if os.name == 'nt' else 'clear')

edad=int(input("Ingrese su edad: "))

if edad >= 21:
    print("Eres mayor de edad")
elif edad >= 18:
    print("Eres ciudadano")
else:
    print("Eres menor de edad")