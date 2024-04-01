from time import sleep
from interface import cabecalho, opções
from gerar_senhas import caracteres_especiais, numeros, escolher
from guardar_senhas import arquivoexiste, criararquivo, lerarquivo, cadastrar, cadastrar2

sleep(0.60)
cabecalho("\033[4;33mGERADOR DE SENHAS\033[m")

arq = "Minhasenhascadastradas.txt"

sleep(1.5)
if arquivoexiste(arq):
    print("\033[34mArquivo encontrado com Sucesso!\033[m")
else:
    print("\033[31mArquivo não encontrado!!\033[m")
    sleep(1.0)
    print("\033[32mCriando arquivo...\033[m")
    sleep(2.0)
    criararquivo(arq)

sleep(2.5)

cabecalho(
    "\033[4;33mEscolha uma opção de senha(s) que você deseja gerar\033[m")
opções()

while True:
    try:
        res = int(input(f"\033[33mSua Opção:\033[m"))
        break
    except (ValueError, TypeError):
        print("\033[31mERRO!!, Digite apenas numeros inteiros...\033[m")


sleep(3.0)
if res == 0:
    lerarquivo(arq)


if res == 1:
    sleep(2.0)
    resultado = numeros()
    senha = ''.join(map(str, resultado))
    print("\033[34mGERANDO OS NUMEROS...\033[m")
    sleep(2.50)
    print(f"Sua nova senha de 8 dígitos é: {senha}\n")
    cadastrar(arq, senha)


elif res == 2:
    n = numeros()
    caracteres = caracteres_especiais(1)
    senha = "".join(map(str, n))
    senha2 = "".join(map(str, caracteres))
    sleep(0.50)
    print("\033[34mGERANDO OS NUMEROS...\033[m")
    sleep(2.50)
    print(f"\033[32mSua nova senha de 8 digitos e 1 caractere especial é: {senha2}{senha}\033[m\n")
    s = (f"{senha2}{senha}")
    cadastrar(arq, s)

if res == 3:
    n = numeros()
    caracteres = caracteres_especiais(2)
    senha = "".join(map(str, n))
    senha2 = "".join(map(str, caracteres))
    sleep(0.50)
    print("\033[34mGERANDO OS NUMEROS...\033[m")
    sleep(2.50)
    print(f"\033[32mSua nova senha de 8 digitos e 1 caractere especial é: {senha2}{senha}\033[m\n")
    s = (f"{senha}{senha2}")
    cadastrar(arq, s)

elif res == 4:
    num = int(input("Quantos numeros na senha : "))
    caracter = int(input("Quantos caracteres deseja adicionar na sua senha:"))
    print("\033[34mGERANDO OS NUMEROS...\033[m")
    sleep(2.50)
    cadastrar2(arq, num, caracter)
