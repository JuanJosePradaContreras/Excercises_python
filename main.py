#Ejercicio 20

#Escribe un programa que convierta una calificación numérica en una letra de acuerdo a un
#sistema de calificación específico, usando match .

def convert_to_letter(grade):
    
    match grade:
        case grade if 90 <= grade <= 100:
            return "A"
        case grade if 80 <= grade < 90:
            return "B"
        case grade if 70 <= grade < 80:
            return "C"
        case grade if 60 <= grade < 70:
            return "D"
        case _:
            return "F"  

def main():
   
    grade = float(input("Enter your grade (0-100): "))
    
    if 0 <= grade <= 100:
        
        letter = convert_to_letter(grade)
       
        print(f"Your grade is: {letter}")
    else:
        print("The grade must be between 0 and 100.")

main()