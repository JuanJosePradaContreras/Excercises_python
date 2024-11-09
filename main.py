#Ejercicio 3

#Crea una calculadora que solicite dos números y una operación matemática (+, -, *, /). Usa match
#para realizar la operación correspondiente

def calculator():
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    match operation:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Cannot divide by zero."
        case _:
            result = "Invalid operation."

    print(f"Result: {result}")
