import sys

import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
while True:
    opc= input("¿que archivo deseas entrar? por titulos, cambios(1), nombre de usuario (2), citas(3), name(4),mult(5), num favorito(6),Transporte favorito(7), pizzas(8), animales(9), par impar(10), factorial(11), anagramas(12), fibunacci(13), numeros primos(14), salir (15).")
    if opc.isnumeric()==True and int(opc)>0:
        op=int(opc)
        if op==1:
            import Tarea_1y2
            print(Tarea_1y2.cambios())
        elif op==2:
            import Tarea_3y4
            print(Tarea_3y4.nombre_usuario())
        elif op==3:
            import Tarea_5y6
            print(Tarea_5y6.citas())
        elif op==4:
            import Tarea_7
            print(Tarea_7.name())
        elif op==5:
            import Tarea_8
            print(Tarea_8.mult())
        elif op==6:
            import Tarea_9_10y11
            print(Tarea_9_10y11.num_fav())
        elif op==7:
            import Tarea_12
            print(Tarea_12.transporte_fav())
        elif op==8:
            import Tarea_13
            print(Tarea_13.pizzas())
        elif op==9:
            import Tarea_14
            print(Tarea_14.animales())
        elif op==10:
            import Tarea_15
            print(Tarea_15.par_impar())
        elif op==11:
            import Tarea_16
            print(Tarea_16.factorial())
        elif op==12:
            import Tarea_17
            print(Tarea_17.anagramas())
        elif op==13:
            import Tarea_18
            print(Tarea_18.fibunacci())
        elif op==14:
            import Tarea_19
            print(Tarea_19.num_primo())
        elif op==15:
            print("nos veremos pronto usuario.")
            break
