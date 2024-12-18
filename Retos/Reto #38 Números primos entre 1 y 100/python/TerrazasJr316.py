primero = 2
limite = 1000

Cont = 0

for i in range(primero, limite):
    primo = True
    j = 2
    
    while (i > j) and (primo == True):
        if i%j == 0 :
            primo = False
            break
        else:
            j = j + 1
            
    if primo == True :
        print(i, "es primo.")
        Cont = Cont + 1

print("Entre", primero, "y" , limite, "hay", Cont, "nº primos")
