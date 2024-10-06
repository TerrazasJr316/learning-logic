print("-------------------------------------------------------")
print("Complemento10: DISTANCIA DE DOS PUNTOS en 3D.")
print("-------------------------------------------------------")

#Entradas
print("Ingrese valores del punto A(x1, y1 y z1): ")
x1 = float( input("x1: "))
y1 = float( input("y1: "))
z1 = float( input("z1: "))

print("Ingrese valores del punto B(x2, y2 y z2): ")
x2 = float( input("x2: "))
y2 = float( input("y2: "))
z2 = float( input("z2: "))

#Proceso
dis = ( (z2-z1)**2 + (y2-y1)**2 + (x2-x1)**2 )**0.5

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("La distancia es:", dis)
