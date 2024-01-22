# Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
suma = 0

for x in range(4):
    new_num = float(input("Ingrese un numero: "))
    suma+=new_num
promedio=suma/4

print(f"El promedio es {round(promedio, 2)}")

