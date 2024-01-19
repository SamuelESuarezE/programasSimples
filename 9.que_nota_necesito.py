# Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.
# Donde NC es el promedio de certámenes, NL el promedio de laboratorio y NF la nota final.
# Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio,
# y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

c1_input = float(input("Ingrese nota certamen 1: "))
c2_input = float(input("Ingrese nota certamen 2: "))
lab_input = float(input("Ingrese nota laboratorio: "))
nc_promedio = (60-lab_input*0.3)/0.7
c3 = (nc_promedio*3)-c1_input-c2_input

print(f"Necesita nota {round(c3)} en el certamen 3")




