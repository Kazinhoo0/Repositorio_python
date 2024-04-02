from interface import cabecalho
from gerar_senhas import escolher
import random
def arquivoexiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("\033[31mHouve um erro na cricao do arquivo\033[m")
    else:
        print(f"\033[32mArquivo {nome} criado com sucesso\033[m")


def lerarquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("\033[31merro ao ler o arquivo\033[m")
    else:
        cabecalho("\033[33mSENHAS CADASTRADAS\033[m")
        print(a.read())
    
        

def cadastrar(arq, nome="Desconhecido"):
    try:
        a = open(arq, "at")
    except:
        print("\033[31mHouve um ERRO na abertura do arquivo!!\033[m")
    else:
        try:
            randomizar = "".join(random.sample(nome,len(nome)))
            a.write(f"{randomizar}\n")
        except:
            print("\033[31mHouve um ERRO na hora de cadastrar od dados\033[m")
        else:
            print(f"Sua nova senha é \033[32m{randomizar}\033[m")
            print(f"\033[32mSenha Cadastra com sucesso!\033[m")
            a.close()


def cadastrar2(arq, nome="Desconhecido", caracter = "Desconhecido"):
    try:
        a = open(arq, "at")
    except:
        print("\033[31mHouve um ERRO na abertura do arquivo!!\033[m")
    else:
        try:
            senha_gerada = escolher(nome,caracter)
            randomizar = "".join(random.sample(senha_gerada,len(senha_gerada)))
            a.write(f"({randomizar}\n")
        except:
            print("\033[31mHouve um ERRO ao cadastrar os dados\033[m")
        else:
            print(F"\033[32mSua nova senha é {randomizar}")
            print(f"\033[32mSenha Cadastrada com sucesso!\033[m")
            a.close()
