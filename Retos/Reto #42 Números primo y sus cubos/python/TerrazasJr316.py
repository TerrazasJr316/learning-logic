b = 2

for i in range(1, 29):
    co = 0
    
    for a in range(2, b//2):
        if b % a == 0 :
            co = co + 1
            a = b
    if co == 0 :
        print("El cubo de", b," es: ", b**3)
    b = b + 1
