print("Ingrese las velocidades de ambos vehículos: ")
v1 = float( input("V1: "))
v2 = float( input("V2: "))
print("Ingrese la distancia que los separa: ")
d = float( input("Distancia: "))

if v1 > 0 and v2 > 0 :
    t = d/(v1+v2)
    print(t, "segundos")
else:
    print("ERROR")
