#Ejercicio 11

#Escribe un programa que convierta grados Celsius a Fahrenheit o Fahrenheit a Celsius usando
#match .

temperature = float(input("Enter the temperature: "))
scale = input("Enter the scale (C for Celsius or F for Fahrenheit): ").upper()

match scale:
    case 'C':
        
        result = (temperature * 9/5) + 32
        print(f"{temperature}°C is equal to {result:.2f}°F.")
    case 'F':

        result = (temperature - 32) * 5/9
        print(f"{temperature}°F is equal to {result:.2f}°C.")
    case _:
        
        print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")