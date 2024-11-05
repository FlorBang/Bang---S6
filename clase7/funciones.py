#Como declarar una función

""" def saludar():
    print("Hola")
    print("¿Como estas?")
    print("Un gusto verte")

saludar() """

""" def saludar(nombre):
    print("Hola " + nombre)
    print("¿Como estas?")
    print("Un gusto verte")

saludar("Julian")
saludar("flor")"""


"""def saludar(nombre, estado):
    print("Hola " + nombre)
    print("¿Como estas? bien / mal")
    if estado == "bien":
        print("Que bueno verte bien ¿En que te puedo ayudar?")
    else:
        print("¿En que te puedo ayudar?")


saludar(input("Ingrese su nombre: "), input("Escribe tu estado: (bien / mal)"))
saludar(input("Ingrese su nombre: "), input("Escribe tu estado: (bien / mal)"))
saludar(input("Ingrese su nombre: "), input("Escribe tu estado: (bien / mal)"))
saludar(input("Ingrese su nombre: "), input("Escribe tu estado: (bien / mal)")) """


def saludar (nombre, apellido, empresa):
    print("Hola " + nombre + apellido)
    print("Bienvenido a " + empresa)
    print("Un gusto tenerte con nosotros")

saludar(nombre= "Pepe ", apellido= "Perez", empresa= "BDS")
saludar(nombre= "Flor ", apellido= "Bang", empresa= "Pinterest")
saludar(nombre= "Tomas ", apellido= "Saenz", empresa= "Microsoft")
saludar(nombre= "Julian ", apellido= "Pana", empresa= "StarWars")
saludar(nombre= "Ornella ", apellido= "Forgione", empresa= "SHEIN")