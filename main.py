#Ejercicio 15

#Escribe un programa que calcule el salario neto de un empleado después de aplicar impuestos.

def calculate_net_salary(gross_salary, country):
    
    match country:
        case "Country A":
            tax_rate = 0.20  
        case "Country B":
            tax_rate = 0.15  
        case "Country C":
            tax_rate = 0.10  
        case _:
            tax_rate = 0.18  
    
    
    net_salary = gross_salary * (1 - tax_rate)
    return net_salary

def main():
    
    gross_salary = float(input("Enter your gross salary: "))
    country = input("Enter your country of residence (Country A, Country B, Country C, other): ").strip()
    
   
    net_salary = calculate_net_salary(gross_salary, country)
    
    
    print(f"Your net salary after taxes is: {net_salary:.2f}")

main()