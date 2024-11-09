#Ejercicio 9

#Escribe un programa que clasifique a una persona en función de su edad.
#Solicita la edad de la persona e indica si es niño (0-12 años), adolescente (13-17 años), adulto (18-
#64 años) o anciano (65 años o más).

age = int(input("Enter your age: "))

if 0 <= age <= 12:
    print("The person is a child.")
elif 13 <= age <= 17:
    print("The person is a teenager.")
elif 18 <= age <= 64:
    print("The person is an adult.")
else:
    print("The person is a senior.")