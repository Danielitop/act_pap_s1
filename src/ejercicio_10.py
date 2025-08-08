contador = 0
palabra = input("Escribe una palabra (fin para terminar): ")
while palabra.lower() != "fin":
    contador += 1
    palabra = input("Escribe otra palabra (fin para terminar): ")
print("Total de palabras ingresadas:", contador)
