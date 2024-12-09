print("Ingrese el Costo del artículo: ")
costo = float( input())
print("Ingrese la marca: ")

m = input()

if costo >= 2000 and m == "NOSY" :
    pa = costo*0.90
    pt = pa*0.95
elif costo >= 200 and m != "NOSY" :
    pt = costo*0.90
elif costo < 2000 and m == "NOSY" :
    pa = costo*0.95
    pt = pa + pa*0.20
elif costo < 2000 and m != "NOSY" :
    pa = costo*1.20

print("Usted pagara:", pt, "soles")