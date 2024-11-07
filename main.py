#Ejercicio 1

#Solicita al usuario que ingrese un número y verifica si es par o impar

message = int(input("Introduce a number: "))

if message % 2 == 0:
    print(f"""{message} is an even number""")

else:
    print(f"""{message} is an odd number""")

