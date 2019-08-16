traduccion={}

y=int(input("Cuantas palabras desea Ingresar: "))

for x in range(y):
    print(" ")
    palabra1=input("Ingrese un palabra en español: ")
    palabra2=input("Ingrese la traduccion de la palabra anterior: ")

    traduccion[palabra1]=palabra2

print(traduccion)


IngresoP=input("Ingrese una plabra para saber su traduccion en ingles: ")

if IngresoP in traduccion:
    print("La Traduccion de "+ IngresoP +" es: "+ " "+ traduccion[IngresoP])
else:
    print("No se puedo Traducir, lo sentimos")

