# Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

numero = float(input("Ingrese un numero: "))
decimal = numero - int(numero)
print(round(decimal,1))
