V1 = []

print ( "Ingrese cantidad de elementos del vector: ")
n = int( input())

print ( "Ingrese los valores del vector: ")

for x in range(n):
    valor = int( input("V{}: ".format(x+1)))
    V1.append(valor)

print ( "Los elementos del vector son: ")

for y in range(n):
    for x in range(n-1):
        if V1[x] < V1[x+1]:
            m = V1[x]
            V1[x] = V1[x+1]
            V1[x+1] = m
print(V1)

