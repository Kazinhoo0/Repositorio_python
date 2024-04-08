from interface import cabecalho, opcoes
from banco_de_dados import banco_db
from Func import novo_projeto, ver_projetos, horas_trab, alter_horas,soma_horas_trab
from time import sleep


sleep(0.30)
cabecalho("\033[4;33mCRUD CONTROLE DE HORAS\033[m")
sleep(1.0)
banco_db()
sleep(1.5)

while True:
    opcoes()
    try:
        escolha = int(input("\033[33mSua opcão:\033[m "))
    except (ValueError, TypeError):
        print("\033[31m!!ERRO!! Porfavor insira apenas numeros inteiros.")
    
    if escolha == 1:
        cabecalho("\033[33mCADASTRO DE PROJETOS\033[m")
        novo_projeto()
        sleep(3.5)
    if escolha == 2:
        cabecalho("\033[33mPROJETOS CADASTRADOS\033[m")
        ver_projetos()
        sleep(3.5)
    if escolha == 3:
        cabecalho("\033[33mHORAS TRABALHADAS/PROJETO\033[m")
        horas_trab()
        sleep(3.5)
    if escolha == 4:
        cabecalho("\033[33mMODIFICAR VALOR/HORA\033[m")
        alter_horas()
        sleep(3.5)
    if escolha == 5:
        cabecalho("\033[33mACRESCIMO DE HORAS\033[m")
        soma_horas_trab()    
        sleep(3.5)
    if escolha == 6:
        print("\033[31mFECHANDO CONSULTAS...\033[m")
        sleep(2.0)
        break
