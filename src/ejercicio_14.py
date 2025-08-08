import random

secreto = random.randint(1, 10)
adivina = int(input("Adivina el número (1-10): "))
while adivina != secreto:
    adivina = int(input("Incorrecto. Intenta de nuevo: "))
print("¡Felicidades! Adivinaste el número.")
