# Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b
# de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
# del triangulo, dado por el teorema de Pitágoras: c2=a2+b2

from math import sqrt

while True:
        cateto_A = input("Ingrese cateto A: ")
        cateto_B = input("Ingrese cateto B: ")
        try:
            cateto_A = float(cateto_A)
            cateto_B = float(cateto_B)
            if cateto_A>0 and cateto_B>0:
                hipo = sqrt((cateto_A**2)+(cateto_B**2))
                print("La hipotenusa es",round(hipo,2))
                break
            else: print("Error, try again.")
        except ValueError:
            print("Error, try again")