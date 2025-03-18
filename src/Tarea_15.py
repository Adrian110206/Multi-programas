def par_impar():
    numeros = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
    pares = [num for num in numeros if num % 2 == 0]
    impares = []
    print("Ingresa números impares:")
    while True:
        entrada = input("Número impar: ")
        if entrada.isnumeric()==True and int(entrada)>0:
                numero = int(entrada)
                if numero % 2 == 1:
                    impares.append(numero)
                    op=input("¿Deseas salir? salir (S) continuar(N):\n")
                    if op.isnumeric()==True and int(op)>0:
                        p=int(op)
                    if p=="S":
                        break
                    elif p=="N":
                        print("De acuerdo.")
                else:
                    print("Ese número no es impar. Intenta de nuevo.")
                    op=input("¿Deseas salir? salir (S) continuar(N):\n")
                    if op.isnumeric()==True and int(op)>0:
                        p=int(op)
                        if p=="S":
                            break
                        elif p=="N":
                            print("De acuerdo.")
    print("Lista de números pares:", pares)
    print("Lista de números impares:", impares)
print(par_impar())