SUE = float( input("Ingrese Sueldo: "))

if SUE < 1000:
    AUM = SUE*0.15
    SUE = SUE + AUM

print("El sueldo es:", SUE)
