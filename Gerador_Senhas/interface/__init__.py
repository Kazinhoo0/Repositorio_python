def leiaint(msg):
    res = 0
    while True:
        try:
            res = int(input(msg))
            break

        except ValueError:
            print(
                "\033[31mERRO!!, O programa aceita apenas numeros inteiros, tente novamente\033[m. ")

        except TypeError:
            print(
                "\033[31mERRO!!,Você adicionou um tipo de dado não compátivel,Por favor insira apenas valores numeréricos\033[m.")
    return res



def linha(linha = 42):
    return ("-" * linha)

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    

def opções():
    return print("""\033[34m0 - Ver minhas senhas cadastradas
1 - senha com no minimo 8 digitos e sem caractéres especiais
2- senha com 8 digitos e com 1 caracter especial
3- senha com 8 digitos e com 2 caracteres especiais
4- escolher quantos digitos e quantos caracteres especiais\033[m""")