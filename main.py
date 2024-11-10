#Ejercicio 18

#Escribe un programa que calcule el número de créditos totales de un estudiante en base a las
#materias cursadas y el puntaje obtenido en cada una. El puntaje debe ser evaluado como
#aprobado o no aprobado.

def calculate_total_credits(number_of_courses):
    total_credits = 0
    
    for i in range(1, number_of_courses + 1):
        score = float(input(f"Enter the score obtained in course {i}: "))
        
        if score >= 60:
            total_credits += 3 
    
    return total_credits

def main():

    number_of_courses = int(input("Enter the number of courses you have taken: "))
    
    total_credits = calculate_total_credits(number_of_courses)
    
    print(f"The total number of credits earned is: {total_credits}")

main()