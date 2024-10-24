print("-------------------------------------------------------")
print("Complemento3: CAMBIOS DE SOLES a EUROS y DÓLARES")
print("-------------------------------------------------------")

#Constantes
EU = 3.84
DO = 2.28

#Entradas
print("Ingrese la cantidad de soles:")
s = float( input())

#Proceso
d = s/DO
e = s/EU

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("En", s, "soles hay ", e, "euros")
print("En", s, "soles hay ", d, "dólares")