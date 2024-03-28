import random
from time import sleep
import functions
ultsorteio = (3, 7, 11, 35, 38 , 56)
print("-=" * (33))
print ("GERADOR DE NUMEROS PARA MEGA-SENA".center(60))
print("-=" * (33))  



print("""1 -\033[34mFAZER UMA APOSTA/GERAR NUMEROS PRO SORTEIO 2024\033[m
2 -\033[34mVER O RESULTADO DO ULTIMO SORTEIO\033[m""")
while True:
    try:
        res = int(input("\033[33mSua Opção\033[m: "))
        break
    except (ValueError,TypeError):
        print("\033[31mERRO!! As opções só aceitam numeros inteiros, tente novamente\033[m")
    finally:
        print("\033[34mCARREGANDO OPÇÕES...\033[m")
        sleep(2.0)


if res == 2 :
    print("-=" * (33))
    print("\033[33mOPÇÃO 2\033[m".center(60))
    print("-=" * (33))
    print(F"\033[33mOS NUMEROS SORTEADOS NA ULTIMA MEGA-SENA SÃO\033[m: \033[32m{ultsorteio}\033[m")

if res == 1:
    print("\033[33mQuantos numeros deseja apostar?\033[m ")
    print("""    \033[34mA - 6 Numeros(R$5,00)
    B - 7 Numeros (R$12,00)
    C - 12 Numeros (R$45,00)
    D - 15 Numeros (R$60,00)
    E - Sair da aposta\033[m.""")
  
    while True:
        try:
            choose = str(input("\033[33mInsira sua escolha\033[m:")).upper()
            if choose == "E":
                sleep(1.0)
                print("\033[33mCANCELANDO O PROGRAMA...\033[m")
                sleep(3.0)
                print("\033[33mVOLTE SEMPRE PARA FAZER A SUA FEZINHA\033[m .-.")
                break
            saldo = float(input("\033[34mFaça o pagamento aqui:\033[m\n\033[32mR$"))
            preços = {'A': 5, 'B': 12, 'C': 45, 'D': 60} 
            preço = preços[choose] 
            while saldo < preço:
                print("\033[31mSaldo insuficiente. O valor pago não foi sufuciente para completar o pagamento\033[m.")
                while True: 
                    try:
                        saldo = float(input("\033[34mInsira um novo valor: R$\033[34m"))
                        break
                    except (ValueError,KeyboardInterrupt):
                        print("\033[31mERRO!!,Insira apenas numeros reais o inteiros, porfavor...\033[m ")   
        except (TypeError,ValueError):
            print("\033[31m!!ERRO!!, Por favor escolha uma opção acima\033[m")
        else:
            sleep(0.40)
            print("\033[32mPAGAMENTO EFETUADO\033[m.")
            sleep(1.0)
            print("\033[34mGERANDO OS NUMEROS...\033[m")
            sleep(3.0)
            print("\033[34mEAÍ,ANSIOSO PRA FAZER SUA FÉZINHA\033[m ?")
            print("-=" * 40)
            print("\033[4;37mNUMEROS GERADOS\033[m".center(60))
            print("-=" * 40)
            break

    if choose == "A":
        numeros = tuple(range(0,61))
        sorteados = random.sample(numeros, 6)
        valor =5
        troco = saldo - 5
        print(f"\033[34mVocê pagou {functions.format(saldo)} seu troco é de {functions.format(troco)}\033[34m")
        print(f"\033[34mO resultado dos seis numeros gerados é : {sorteados}\033[34m")
    
    
    if choose == "B":
        numeros = tuple(range(0,61))
        sorteados = random.sample(numeros, 7)
        valor = 12
        troco = saldo - 12
        print(f"\033[34mVocê pagou {functions.format(saldo)} seu troco é de {functions.format(troco)}\033[m")
        print(f"\033[34mO resultado dos sete numeros gerados é : {sorteados}\033[m")
    

    if choose == "C":
        numeros = tuple(range(0,61))
        sorteados = random.sample(numeros, 12)
        valor = 45
        troco = saldo - 45
        print(f"\033[34mVocê pagou {functions.format(saldo)} seu troco é de {functions.format(troco)}\033[34m")
        print(f"\033[34mO resultado dos doze numeros gerados é : {sorteados}\033[34m")
    
        
    if choose == "D":
        numeros = tuple(range(0,61))
        sorteados = random.sample(numeros, 15)
        valor = 60
        troco = saldo - 60
        print(f"\033[34mVocê pagou {functions.format(saldo)} seu troco é de {functions.format(troco)}\033[m")
        print(f"\033[34mO resultado dos quinze numeros gerados é : {sorteados}\033[34m")
    if choose == "E":
        print("")