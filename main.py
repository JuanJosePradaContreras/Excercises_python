#Ejercicio 7

#Escribe un programa que determine si un número es positivo, negativo o cero usando if .
#Solicita al usuario que ingrese un número y determina si es positivo, negativo o cero.

number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")