frase = "programacion es divertida"
contador = 0
for letra in frase.lower():
    if letra in "aeiou":
        contador += 1
print("Cantidad de vocales:", contador)
