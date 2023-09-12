import os
from time import sleep
s=0
op=133

os.system("cls")

def soma(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mult(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
def pot(a,b):
    return(a ** b)
def rad(a,b):
    return(a ** (1/1))

while op!=0:

    os.system("cls")

    print ("=====================================\n\n    '+' __ soma\n    '-' __ subtração\n    '*' __ multiplicação\n    '/' __ divisão\n    '**' __ potenciação\n    '**/' __ radiciação\n\n=====================================")

    op=int(input("Qual operação deseja fazer?\n"))
    
    a=int(input("primeiro valor:"))
    b=int(input("segundo valor:"))
    
    
    if op == 1:
        resultado = soma(a, b)
        os.system("cls")
        print ("O resultado obtido foi:",resultado)
        sleep(2)
    
    elif op == 2:
        resultado = sub(a, b)
        os.system("cls")
        print ("O resultado obtido foi:",resultado)
        sleep(2)
    elif op == 3:
        resultado = mult(a, b)
        os.system("cls")
        print ("O resultado obtido foi:",resultado)
        sleep(2)
    elif op == 4:
        resultado = div(a, b)
        os.system("cls")
        print ("O resultado obtido foi:",resultado)
        sleep(2)
    elif op == 5:
        resultado = pot(a, b)
        os.system("cls")
        print ("O resultado obtido foi:",resultado)
        sleep(2)
    elif op == 6:
        resultado = rad(a, b)
        os.system("cls")
        print ("O resultado obtido foi:",resultado)
        sleep(2)
    else:
        print ("não foi possivel")