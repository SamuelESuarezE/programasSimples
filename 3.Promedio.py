from statistics import mean

# Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
num_list=[]

for x in range(4):
    new_num = float(input("Ingrese un numero: "))
    num_list.append(new_num)
    
print(f"El promedio es {round(mean(num_list), 2)}")

