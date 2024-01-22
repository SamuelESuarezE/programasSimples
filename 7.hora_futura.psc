Algoritmo horaFutura
	Escribir 'Hora actual:'
	Leer hora_actual
	Escribir 'Cantidad de horas:'
	Leer cantidad_horas
	hora_futura <- (hora_actual+cantidad_horas) MOD 24
	Escribir 'En ', cantidad_horas, ' horas, el reloj marcara las ', hora_futura
FinAlgoritmo