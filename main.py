#Ejercicio 21

#Escribe un programa que calcule el costo de estacionamiento basado en el número de horas, con
#tarifas progresivas.

#El costo de estacionamiento se calcula de la siguiente manera:
#Primera hora: $5
#Segunda a cuarta hora: $4 por hora
#Más de cuatro horas: $3 por cada hora adicional
#Solicita al usuario el número de horas de estacionamiento y calcula el costo total.

def calculate_parking_cost(hours):
   
    if hours <= 1:
        return 5 
       
    elif 2 <= hours <= 4:
        return 5 + (hours - 1) * 4
     
    else:
        return 5 + 3 * (hours - 4) + 12  

def main():
    
    hours = float(input("Enter the number of parking hours: "))
    
    cost = calculate_parking_cost(hours)
    
    print(f"The total parking cost is: ${cost:.2f}")

main()