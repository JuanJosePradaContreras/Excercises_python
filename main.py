#Ejercicio 6

#Escribe un programa que implemente un juego de adivinanza de números. El programa genera un número aleatorio entre 1 y 10. El usuario debe adivinar el número,
#y elprograma indica si el número ingresado es mayor, menor o igual al número generado.

import random

random_number = random.randint(1, 10)

print("Welcome to the number guessing game!")
print("I've chosen a number between 1 and 10. Try to guess it!")

while True:
   
    guess = int(input("Enter your guess: "))
    
    if guess < random_number:
        print("Your guess is too low. Try again.")
    elif guess > random_number:
        print("Your guess is too high. Try again.")
    else:
        print(f"Congratulations! You guessed the number {random_number}.")