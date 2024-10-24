print("-------------------------------------------------------")
print("Ejercicio3: PUNTAJE FINAL.")
print("-------------------------------------------------------")

#Entradas
print("Ingrese número de respuestas correctas: ")
RC = int( input())
print("Ingrese número de respuestas incorrectas: ")
RI = int( input())
print("Ingrese número de respuestas en blanco: ")
RB = int( input())

#Proceso
PCR = RC*3
PRI = RI*-1
PRB = RB*0
PF = PCR + PRI + PRB

#Salida
print("El puntaje total es:", PF)