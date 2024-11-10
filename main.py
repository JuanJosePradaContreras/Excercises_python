#Ejercicio 12

#Escribe un programa que calcule el IMC y determine el estado de peso.

def calculate_bmi(weight, height):
    
    return weight / (height ** 2)

def classify_bmi(bmi):
    
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    
    bmi = calculate_bmi(weight, height)
    
    
    weight_status = classify_bmi(bmi)
    
    print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")
    print(f"Your weight status is: {weight_status}")

main()