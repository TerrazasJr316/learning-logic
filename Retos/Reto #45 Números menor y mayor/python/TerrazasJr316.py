con = 0

for i in range(2, n):
    if n % i == 0 :
        con = con + 1
if con == 0:
    print (n, " Es un número primo")
else:
    print (n, " No es un número primo")
