#Ejercicio 5

#Escribe un programa que, dado un número del 1 al 7, imprima el día correspondiente de la
#semana usando match .

number = int(input("Enter a number between 1 and 7: "))

match number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid number. It must be between 1 and 7.")