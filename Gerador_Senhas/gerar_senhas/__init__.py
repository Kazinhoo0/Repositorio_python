import random

def caracteres_especiais(quantidade = 1):
    caracteres = "#$@!&%*"
    resultado = "".join(random.choice(caracteres)  for _ in range(quantidade))
    return resultado


def numeros(quantidade = 8):
    numeros = tuple(range(0,10))
    resultado = (random.sample(numeros,quantidade))
    return resultado



def escolher(num,caracter):
    numeros = tuple(range(0,10))
    gerador = random.sample(numeros,num)
    gerador_str = "".join(map(str, gerador))
    caracteres = "#$@!&%*"
    g = "".join(random.sample(caracteres,caracter))
    return (f"{g}{gerador_str}")
