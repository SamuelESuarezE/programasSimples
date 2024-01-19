import math

# El enunciado es muy largo :(
# Escriba un programa que reciba como entrada la temperatura original del huevo
# y muestre como salida el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.
t_y= 70
temp_original_input = float(input("Ingrese la temperatura original del huevo: "))
m_var_input = (input("Tamaño del huevo:\n\t1. Pequeño\n\t2. Grande\n"))
T_Ebu = 100
if m_var_input == "1": M_var = 47
elif m_var_input == "2": M_var = 67
else: print("Error, try again")
C_var = 3.7
P_var = 1.038
K_var = 0.0054


numerador1=((M_var**(2/3))*C_var*(P_var**(1/3)))
numerador2 =(K_var*(math.pi**2)*((4*math.pi)/3)**(2/3))
resultado1 = numerador1/numerador2
resultado2=math.log(0.76*((temp_original_input-T_Ebu)/(t_y-T_Ebu)))
resultado_final=resultado1*resultado2

print(f"El huevo tardara en cocinarse {round(resultado_final)} segundos.")
print(f"El huevo tardara en cocinarse {round(resultado_final/60)} minutos.")
