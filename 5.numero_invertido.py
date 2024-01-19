# Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

numero = input("Ingrese numero: ")
invertido=""

for x in range(len(numero)):
    invertido+=numero[-(x+1)]
print(invertido)