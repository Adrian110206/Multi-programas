def citas():
    cita='"Nunca se alcanzo la verdad total, ni nunca se esta totalmente alejado de ella."'
    autor=" Atistóteles. "
    print(f'{cita} -{autor}')
    op=input("desea modificar lso espacios del autor?. eliminar los esapcios del final(1), inicio (2), ambos(3), o no(4)")
    while True:
        if op.isdecimal()==True and int(op)>0:
            opc=int(op)
            if opc==1:
                print(f"{cita} -{autor.rstrip()}")
                break
            elif opc==2:
                print(f"{cita} -{autor.lstrip()}")
                break
            elif opc==3:
                print(f"{cita} -{autor.strip()}")
                break
            elif opc==4:
                print(f"{cita} -{autor}")
                break
        else:
            print("¿Mis instrucciones no fueron claras?, me refiero a que solo acepta eso, no acepta numeros negativos o que no esten en esa opciones, ni simbolos.")
print(citas())