suma = 0
num = int(input("Ingresa un número (0 para terminar): "))
while num != 0:
    suma += num
    num = int(input("Ingresa otro número (0 para terminar): "))
print("Suma total:", suma)
