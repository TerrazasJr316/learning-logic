print("-------------------------------------------------------")
print("Ejercicio4: PUNTAJE TOTAL DE PARTIDOS.")
print("-------------------------------------------------------")

#Entradas
print("Ingrese número de partidos ganados")
PG = int( input())
print("Ingrese número de partidos empatados")
PE = int( input())
print("Ingrese número de partidos perdidos")
PP = int( input())

#Proceso
PPG = PG*3
PPE = PE*1
PPP = PP*0
PF = PPG + PPE + PPP

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Puntaje Final: ", PF)