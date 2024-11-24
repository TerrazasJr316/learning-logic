import math

PI = 3.1416

print("Ingrese lados del triángulo:")
b = float( input("Lado b: "))
c = float( input("Lado c: "))
print("Ingrese el ángulo en grados sexagesimales:")
alfa = float( input())

a = ( b**2 + c**2 - 2*b*c * math.cos( alfa*PI/180 ) )**0.50

print("El lado a es:", a)