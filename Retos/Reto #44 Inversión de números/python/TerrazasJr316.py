aux = 0
aux2 = 0

print("Ingrese un número: ")

n = int( input())
i = 10

while i <= n:
    aux = n%10
    n = n // 10
    aux2 = aux2*10 + aux
aux2 = aux2*10 + n

print("El número invertido será:", aux2)
