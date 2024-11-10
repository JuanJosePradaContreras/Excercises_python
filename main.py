#Ejercicio 17

#Escribe un programa que calcule la calificación final de un estudiante basándose en su calificación
#y si ha hecho tareas adicionales. Las tareas adicionales pueden darle un extra de puntos, pero el
#máximo de puntos no puede exceder 100.

def calculate_final_grade(grade, did_extra_assignments):

    if did_extra_assignments.lower() == "yes":
        grade += grade * 0.05  
        
    if grade > 100:
        grade = 100
    
    return grade

def main():
    
    grade = float(input("Enter the student's grade (0-100): "))
    
    did_extra_assignments = input("Did the student do extra assignments? (yes/no): ").strip()
    
    final_grade = calculate_final_grade(grade, did_extra_assignments)
    
    print(f"The student's final grade is: {final_grade:.2f}")

main()