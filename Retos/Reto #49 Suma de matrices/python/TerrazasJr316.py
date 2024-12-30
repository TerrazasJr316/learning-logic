A = []
B = []
C = []

print ("Ingrese dimensión de la matriz,máximo 100")
S = int( input("Número de Filas: "))
R = int( input("Número Columnas: "))

for i in range(S):
    A.append( [] ) #Agregamos una i fila vacía en A
    B.append( [] ) #Agregamos una i fila vacía en B
    C.append( [] ) #Agregamos una i fila vacía en C
    for j in range(R):
        A[i].append( int( input("A{}{}: ".format(i+1,j+1))))
        B[i].append( int( input("B{}{}: ".format(i+1,j+1))))
        C[i].append( A[i][j] + B[i][j])

print(A)
print(B)
print(C)
