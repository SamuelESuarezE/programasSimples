Algoritmo que_nota_necesito
	Escribir 'Ingrese nota certamen 1:'
	Leer c1_input
	Escribir 'Ingrese nota certamen 2:'
	Leer c2_input
	Escribir 'Ingrese nota laboratorio:'
	Leer lab_input
	nc_promedio <- (60-lab_input*0.3)/0.7
	c3 <- (nc_promedio*3)-c1_input-c2_input
	Escribir 'Necesita nota ', redon(c3), ' en el certamen 3'
FinAlgoritmo
