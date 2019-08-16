import math

def area(radio):
    areacirculo=(math.pi*math.pow(radio,2))
    return areacirculo

par=float(input("Introdusca el radio "))
total=area(par)

print("El area del circulo es: ",total)
