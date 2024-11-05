"""nombres = ("Tomas", "Flor", "luli", "vir")

for name in nombres:
    print("hola", name)"""

# .lower para poner todo en minuscula

pantalones = 10
remeras = 25
buzos = 9
bermudas = 30

while True:
    prenda= input("ingrese el tipo de prenda a vender (pantalones, remeras, buzos, bermudas, salir): ").lower ()

    if prenda == "salir":
        break 

    ventas = int(input("ingrese la cantidad de ventas: "))

    if prenda == "pantalones":
        if ventas <= pantalones:
            pantalones -= ventas
            print(f"quedan (pantalones) en stock")
        else:
            print("no hay suficiente stock de pantalones")

    if prenda == "remeras":
        if ventas <= remeras:
            remeras -= ventas
            print(f"quedan (remeras) en stock")
        else:
            print("no hay suficiente stock de remeras")

    if prenda == "buzos":
        if ventas <= buzos:
            buzos -= ventas
            print(f"quedan (buzos) en stock")
        else:
            print("no hay suficiente stock de buzos")

    if prenda == "bermudas":
        if ventas <= bermudas:
            bermudas -= ventas
            print(f"quedan (bermudas) en stock")
        else:
            print("no hay suficiente stock de bermudas")

    
