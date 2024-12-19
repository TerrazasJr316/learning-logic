print("Ingrese el valor de X: ")
x = int( input())

e = 1
num = 1
den = 1
i = 1

num = x**i
den = den*i
i = i + 1
e = e + num/den

while not (num/den < 0.000001):
    num = x**i
    den = den*i
    i = i + 1
    e = e + num/den

print("e elevado al", x, "es: ", e)
