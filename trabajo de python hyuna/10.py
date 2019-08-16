frutas={
    "manzana":[1.35],
    "platano":[0.80],
    "pera":[0.85],
    "naranja":[0.70]
    }

frut=input("¿Que fruta desea comprar? ")

if frut in frutas:
    print("El kilo de esta fruta tiene el valor de",frutas.get(frut))
else:
    print ("lo sentimos No se encuentra esta fruta")
