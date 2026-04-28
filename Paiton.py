from Funciones import menu

menu()

resultado = 0
num1 = 0
num2 = 0

opcion = int(input("Ingrese una opcion: "))

if opcion == 1:
    print("Sumando")

    num1 = int(input("Ingrese el numero1: "))
    num2 = int(input("Ingrese el numero2: "))

    resultado = num1 + num2

    print(f"El resultado de la suma es: {resultado}")

elif opcion == 2:
    print("Restando")

    num1 = int(input("Ingrese el numero1: "))
    num2 = int(input("Ingrese el numero2: "))

    resultado = num1 - num2

    print(f"El resultado de la resta es: {resultado}")

elif opcion == 3:
    print("Multiplicando")

    num1 = int(input("Ingrese el numero1: "))
    num2 = int(input("Ingrese el numero2: "))

    resultado = num1 * num2

    print(f"El resultado de la multiplicacion es: {resultado}") 

elif opcion == 4:
    print("Dividiendo")

    num1 = int(input("Ingrese el numero1: "))
    num2 = int(input("Ingrese el numero2: "))

    resultado = num1 / num2

    print(f"El resultado de la division es: {resultado}") 

elif opcion == 5:
    print("Potencia")

    num1 = int(input("Ingrese el numero1: "))
    num2 = int(input("Ingrese el numero2: "))

    resultado = num1 ** num2

    print(f"El resultado de la potencia es: {resultado}")          

else:
    print("Opcion no valida, intente nuevamente")

    menu()