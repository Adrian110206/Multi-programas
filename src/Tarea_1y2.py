def cambios():
    hola=input("coloca lo que quieras: ")
    print(hola)
    while True:
        op=input("¿deseas cambiar el mensaje? si (1) no(2)")
        if op.isnumeric()==True and int(op)>0:
            p=int(op)
            if p ==1:
                hola=input("¿Que desea escribir?:")
                print(hola)
                break
            elif p==2:
                print("nos vemos.")
                break
            else:
                print("porfavor, siga las instrucciones.")
        else:
            print("porfavor, siga las instrucciones.")
if __name__ == "__main__":
    cambios()
