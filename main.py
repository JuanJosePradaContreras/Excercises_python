#Ejercicio 4

#Escribe un programa que determine el tipo de triángulo en función de sus lados usando if .

def triangle_type():

    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))

    if side1 == side2 == side3:
        triangle = "Equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        triangle = "Isosceles"
    else:
        triangle = "Scalene"

    print(f"The triangle is {triangle}.")

triangle_type()
