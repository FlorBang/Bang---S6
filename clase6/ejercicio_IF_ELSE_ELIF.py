# calculadora simple

"""El programa pedirá al usuario que ingrese dos números y una operación (+, -, *, /).
Utilizando condicionales, el programa realizará la operación correspondiente y mostrará el resultado.
Si el usuario ingresa una operación inválida, se mostrará un mensaje de error."""

operación = input("Ingresa el tipo de operación que desea ejecutar:(+ - * /)")
num1 = int(input("ingrese el 1er número: "))
num2 = int(input("ingrese el 2ndo número: "))

if operación == "+":
    print(num1 + num2)
elif operación == "-":
    print(num1 - num2)
elif operación == "*":
    print(num1 * num2)
elif operación == "/":
    print(num1 / num2)
else:
    print("operación no válida")