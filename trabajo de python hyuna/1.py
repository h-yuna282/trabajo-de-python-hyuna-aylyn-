def prod(n1,n2):
    T=n1*n2
    return T

Y=int(input ("Digite un numero "))
G=int (input("Digite otro numero "))

total=prod(Y,G)

suma=Y+G

if total>=1000:
    print(total," la suma es: ",suma)
else:
    print(suma)
