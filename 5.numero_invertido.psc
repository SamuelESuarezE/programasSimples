Algoritmo numeroinvertido
	Definir numeroUser Como Cadena
	Escribir 'Ingrese un numero:'
	Leer numeroUser
	Definir invertido Como Cadena
	Para x<-longitud(numeroUser) Hasta 1 Con Paso -1 Hacer
		invertido <- invertido+Subcadena(numeroUser,x,x)
	FinPara
	Escribir invertido
FinAlgoritmo
