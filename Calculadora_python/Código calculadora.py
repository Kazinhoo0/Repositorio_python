print("Este programa é uma calculadora em python")


def soma(a, b):
    s = 0
    s = a + b
    return s


def subtracao(a, b):
    s = 0
    s = a - b
    return s


def multiplicacao(a, b):
    s = 0
    s = a * b
    return s


def divisao(a, b):
    s = 0
    s = a / b
    return s


def média(a, b):
    s = 0
    s = (a + b) / 2
    return s


# programa principal
while True:
    n1 = input("Insira o primeiro numero: ")
    if n1.isdigit():
        n1 = int(n1)
        break
    else:
        print("\033[31m!!!ERRO!!!, Por favor insira apenas numeros inteiros válidos.\033[m")
while True:
    n2 = input("Insira o segundo numero: ")
    if n2.isdigit():
        n2 = int(n2)
        break
    else:
        print("\033[31m!!!ERRO!!!, Por favor insira apenas numeros inteiros válidos\033[m.")
print(""""Qual operacao algébrica você quer efetuar com os numeros:
    [1] soma
    [2] subtracão
    [3] multiplicacão
    [4] média
    [5] divisao""")
while True:
    choose = input("Sua escolha: ")
    if choose.isdigit():
        choose = int(choose)
        break
    else:
        print("\033[31m!!!ERRO!!!, Por favor insira apenas numeros inteiros válidos.\033[m")

if choose == 1:
    print(f"O resultado da soma {n1} + {n2} é igual a: {soma(n1, n2)}")
if choose == 2:
    print(f"A subtracão de {n1} - {n2} é igual a: {subtracao(n1, n2)}")
if choose == 3:
    print(f"A multiplicacão de {n1} * {n2} é igual a: {multiplicacao(n1, n2)}")
if choose == 4:
    print(f"A média de {n1} por {n2} é igual a: {média(n1, n2)}")
if choose == 5:
    print(f"A divisao de {n1} / {n2} é igual a: {divisao(n1, n2)}")
