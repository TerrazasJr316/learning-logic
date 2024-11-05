print("Ingrese coordenadas del Punto A: ")
AX = float(input("Ax: "))
AY = float(input("Ay: "))
print("Ingrese coordenadas del Punto B: ")
BX = float(input("Bx: "))

BY = float(input("By: "))

D = ( (AX-BX)**2 + (AY-BY)**2 )**0.5

print("Resultado:", D)