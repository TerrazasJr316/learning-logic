print("Ingrese dimensión del vector: ");
n = int( input())
v = n*['']
for i in range(n):
    v[i] = input("Ingrese Caracter: ")

z = ''
d = n

for i in range(n//2):
    z = v[i]
    v[i] = v[d-1]
    v[d-1] = z
    d = d - 1

for i in range(n):
    print(v[i])