#Ejercicio 8

#Escribe un programa que determine si un año es bisiesto o no.
#Solicita al usuario que ingrese un año y determina si es bisiesto (divisible entre 4, pero no entre
#100, salvo que sea divisible entre 400).

def is_leap_year(year):
    
    if year < 1582:
        return year % 4 == 0 

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")