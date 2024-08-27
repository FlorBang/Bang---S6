#CALCULAR PORCENTAJE DE UNA COMPRA

precio_original = float (input("Ingrese el precio original de la compra: "))
descuento = int (input("Ingresa el porcentaje de descuento: "))

#CALCULAR EL DESCUENTO

precioDescuento = (precio_original * descuento) / 100
precioFinal = precio_original - precioDescuento

print ("El precio final de la compra, con el descuento es: $", precioFinal)