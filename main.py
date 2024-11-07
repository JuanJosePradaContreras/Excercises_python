#Ejercicio 2

#Solicita al usuario una calificación y determina si la nota es aprobatoria (>= 60) o reprobatoria (<60).

message = int(input("Introduce a grade: "))

if message >= 60 and message <= 100:
    print(f"""YOU APPROVED""")

elif message >= 0 and message < 60:
    print(f"""YOU DISAPPROVED""")

else:
    print(f"""THE GRADE IS INVALID""")
