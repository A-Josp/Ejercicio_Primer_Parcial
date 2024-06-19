palabra = input("Ingrese una palabra: ")

if palabra[::-1]==palabra:
    print("Es palindromo")
else:
    print("No es palindromo")