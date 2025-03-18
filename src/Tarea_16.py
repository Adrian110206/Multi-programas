def factorial():
    num = int(input("Ingresa un número para calcular su factorial: "))
    if num < 0:
        print("No se puede calcular el factorial de un número negativo.")
    else:
        for i in range(num):
            if i == 0 or i == 1:
                print(1)
            else:
                resultado=i * factorial(i - 1)
        print(f"El factorial de {num} es {resultado}")
print(factorial())