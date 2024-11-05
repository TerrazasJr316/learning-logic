import math

print("Ingrese GB: ")
GB = float( input())

MG = GB*1024
MD = MG/1.44

print(MD)
print("Numero de Discos necesarios: ", math.ceil(MD))
