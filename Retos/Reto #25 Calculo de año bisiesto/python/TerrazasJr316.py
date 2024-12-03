anio = int( input("Ingrese año: "))

if (anio % 400 == 0) or (anio % 4 == 0) and (anio % 100 != 0):
    print("El año es BISIESTO")
else:
    print("El año NO es BISIESTO")