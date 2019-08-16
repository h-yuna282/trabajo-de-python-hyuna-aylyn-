lista=[]
n=0
control=0
p=0
for k in range (0,10):
    datos=int(input("Digite un valor: "))
    lista.append(datos)
    p=p+lista[k]
    if lista[k]==5:
        n+=1
    if lista[k]>control:
        control=lista[k]
    

print (lista)
print ("Hay",n," veces 5")
print ("El numero mayor es: ",control)
print ("El promedio es: ",p/10)
