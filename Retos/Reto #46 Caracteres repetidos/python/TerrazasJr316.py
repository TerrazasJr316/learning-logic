print ("Ingrese la cantidad de números a evaluar:")
n = int( input())

c = 0
for i in range(1, n+1):
    num = int( input("Ingrese número: "))
if num == 0 :
    c = c+1

print ("Hay ", c, " números ceros")