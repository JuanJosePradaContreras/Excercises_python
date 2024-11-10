#Ejercicio 22

#Escribe un programa que clasifique un triángulo en agudo, obtuso o rectángulo según sus ángulos
#internos usando if .

def classify_triangle(angle1, angle2, angle3):

    if angle1 + angle2 + angle3 != 180:
        return "The angles do not form a valid triangle."
    
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        return "Right" 
    
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        return "Obtuse"  
    
    else:
        return "Acute" 

def main():
   
    angle1 = float(input("Enter the first angle of the triangle: "))
    angle2 = float(input("Enter the second angle of the triangle: "))
    angle3 = float(input("Enter the third angle of the triangle: "))
    
    result = classify_triangle(angle1, angle2, angle3)
    
    print(f"The triangle is: {result}")

main()