ca = 0

numCar = 10
print("Ingrese", numCar, "caracteres: ")
for i in range(0, numCar):
    m = input("Ingrese Caracter: ")
if m == "a" :
    ca = ca + 1

print ("En", numCar, "caracteres hay", ca, "caracteres 'a'")