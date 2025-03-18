#1) EL usuario debe intruducir un numero entero, con todas sus validaciones para un numero entero
#2) El programa debe decir, si el numero ingresado es : 
# 2.a) par o impar
# 2.b) si es fibunacci
# 2.c) si es primo
x = int(input("numero: "))
num1=0
num2=1
num=0
c=0
while True:
    num = num1 + num2
    num1 = num2
    num2 = num
    if x == num:
        c = 1
        break
    elif x < num:
        break
if c == 1:
    print("tu numero está en figonacci")
else:
    print("tu numero no esta en figonacci")
    