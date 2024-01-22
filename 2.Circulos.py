from math import pi

# Escriba un programa que reciba como entrada el radio de un círculo
# y entregue como salida su perímetro y su área:

while True:
    radio = input("Ingrese el radio del circulo: ")
    try:
        radio = float(radio)
        perimetro = 2*pi*radio
        area = pi*(radio**2)
        print(f"El perimetro es {round(perimetro, 2)} y el area es {round(area,2)}")
        break
    except ValueError:
        print("Error, intentalo de nuevo.")