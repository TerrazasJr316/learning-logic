import math

print("-------------------------------------------------------")
print("Ejercicio5: NÚMERO DE MICRO DISCOS 3.5 NECESARIOS")
print("-------------------------------------------------------")

#Entradas
print("Ingrese GB: ")
GB = float( input())

#Proceso
MG = GB*1024
MD = MG/1.44

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print(MD)

#En caso de Decimal Aproximar al siguiente entero
#Ya que la parte decimal debe ser almacenada en otro DISCO 3.5
print("Numero de Discos necesarios: ", math.ceil(MD))
