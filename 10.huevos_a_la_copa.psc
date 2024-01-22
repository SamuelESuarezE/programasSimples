Algoritmo huevos_a_la_copa
	Definir temp_original_input Como Real
	Escribir 'Ingrese la temperatura original del huevo:'
	Leer temp_original_input
	Definir m_var_input Como Real
	Escribir 'Tamaño del huevo 1. Pequeño 2. Grande:'
	Leer m_var_input
	t_y <- 70
	T_Ebu <- 100
	C_var <- 3.7
	P_var <- 1.038
	K_var <- 0.0054
	Si (m_var_input==1) Entonces
		M_var <- 47
	SiNo
		Si (m_var_input==2) Entonces
			M_var <- 67
		SiNo
			Escribir 'Error, try again'
		FinSi
	FinSi
	numerador1 <- ((M_var^(2/3))*C_var*(P_var^(1/3)))
	numerador2 <- (K_var*(pi^2)*((4*pi)/3)^(2/3))
	resultado1 <- numerador1/numerador2
	resultado2 <- ln(0.76*((temp_original_input-T_Ebu)/(t_y-T_Ebu)))
	resultado_final <- resultado1*resultado2
	Escribir 'El huevo tardara en cocinarse ', redon(resultado_final), ' segundos.'
	Escribir 'El huevo tardara en cocinarse ', redon(resultado_final/60), ' minutos.'
FinAlgoritmo
