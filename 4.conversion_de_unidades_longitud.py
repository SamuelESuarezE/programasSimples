# Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.

input_cm = float(input("Ingrese longitud: "))
pulgadas = input_cm/2.54
print(f"{input_cm} cm = {round(pulgadas, 2)} in")