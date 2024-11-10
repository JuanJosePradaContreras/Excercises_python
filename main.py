#Ejercicio 14

#Escribe un programa que permita al usuario adivinar una letra secreta usando match .

def guess_letter():
    secret_letter = "A"
    
    while True: 
        user_guess = input("Guess the secret letter: ").upper()
        
        match user_guess:
            case _:
                if user_guess == secret_letter:
                    print("Congratulations! You guessed the secret letter.")
                    break 
                else:
                    print("Sorry! You didn't guess it. Try again.")

guess_letter()