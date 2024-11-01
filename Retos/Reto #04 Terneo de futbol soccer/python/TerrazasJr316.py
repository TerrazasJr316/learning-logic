print("Ingrese número de partidos ganados")
PG = int( input())
print("Ingrese número de partidos empatados")
PE = int( input())
print("Ingrese número de partidos perdidos")
PP = int( input())

PPG = PG*3
PPE = PE*1
PPP = PP*0
PF = PPG + PPE + PPP

print("Puntaje Final: ", PF)
