print("-------------------------------------------------------")
print("Ejercicio6: DISTANCIA ENTRE 2 PUNTOS A y B, en 2D.")
print("-------------------------------------------------------")

#Entradas
print("Ingrese coordenadas del Punto A: ")
AX = float(input("Ax: "))
AY = float(input("Ay: "))
print("Ingrese coordenadas del Punto B: ")
BX = float(input("Bx: "))
BY = float(input("By: "))

#Proceso
D = ( (AX-BX)**2 + (AY-BY)**2 )**0.5

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Resultado:", D)
