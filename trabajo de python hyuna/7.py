import math

def IMC(altura,peso):
    imc=math.pow(altura,2)/peso

    if imc<15:
        print("Su imc es de: ",imc," usted tiene delgadez muy severa, coma mas")
    if imc>15 and imc<15.9:
        print("Su imc es de: ",imc," usted tiene delgadez severa,coma mas")
    if imc>16 and imc<18.4:
        print("Su imc es de: ",imc," usted tiene delgadez,coma mas")
    if imc>18.5 and imc<24.9:
        print("Su imc es de: ",imc," usted tiene un peso saludable")
    if imc>25 and imc<29.9:
        print("Su imc es de: ",imc," usted tiene sobrepeso,coma menos")
    if imc>30 and imc<34.9:
        print("Su imc es de: ",imc," Significa obesidad severa,coma menos")
    if imc>40:
        print("Su imc es de: ",imc,"Obesidad morvida y perturvadora, coma menis por favor")

altura=float(input("Ingrese su altura "))
peso=float(input("Ingrese su peso"))

IMC(altura,peso)
