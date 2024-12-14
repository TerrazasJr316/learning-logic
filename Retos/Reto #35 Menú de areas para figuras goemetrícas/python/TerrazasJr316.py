
PI = 3.1416

print("Ingrese valores del menú:")
print("1: Área del triángulo:")
print("2: Área del círculo:")
Opc = int( input("Opc: "))

if Opc == 1 :
    print("Área del Triángulo")
    print("Ingrese el lado del triángulo")
    L = float( input("L: "))
    A = ( (3 ** 0.5)/ 4) * L**2
    print("\nEl área del triángulo es:", A)
elif Opc == 2:
    print("Área del Círculo")
    print("Ingrese el radio del círculo")
    R = float( input("R: "))
    C = PI * R**2
    print("\nEl área del círculo es:", C)
else:
    print("\nerror")