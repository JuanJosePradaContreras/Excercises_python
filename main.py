#Ejercicio 16

#Escribe un programa que calcule el tiempo que tarda en llegar un automóvil a su destino.

def calculate_travel_time(distance, speed):
    
    time_hours = distance / speed
    
    hours = int(time_hours)  
    minutes = round((time_hours - hours) * 60)  
    
    return hours, minutes

def main():
   
    distance = float(input("Enter the distance to travel (in km): "))
    speed = float(input("Enter the car's average speed (in km/h): "))
    
    if speed > 120:
        print("Warning! The speed is greater than 120 km/h, which is dangerous.")
    
    hours, minutes = calculate_travel_time(distance, speed)
    
    print(f"The travel time is: {hours} hours and {minutes} minutes.")

main()