import math

print("-------------------------------------------------------")
print("Complemento7: CALCULAR EL TERCER LADO DEL TRIANGULO")
print("-------------------------------------------------------")

#Constantes
PI = 3.1416

#Entradas
print("Ingrese lados del triángulo:")
b = float( input("Lado b: "))
c = float( input("Lado c: "))
print("Ingrese el ángulo en grados sexagesimales:")
alfa = float( input())

#Proceso
#fórmula para calcular lado 'a' con alfa transformado
a = ( b**2 + c**2 - 2*b*c * math.cos( alfa*PI/180 ) )**0.50

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("El lado a es:", a)
