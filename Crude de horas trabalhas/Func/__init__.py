import mysql.connector
from banco_de_dados import estabelecer_conexao
from time import sleep

def alter_horas():
    """
    Esta função tem o objetivo de alterar o seu valor/hora em algum determinado projeto.
    Ela pede ao usuário o ID do projeto a ser mudado, e também o novo valor.
    """
    conexao_banco = estabelecer_conexao()
    cursor = conexao_banco.cursor()
    while True:
        try:
            while True:
                try:
                    valor = float(input("Novo Valor: "))
                    break
                except (ValueError,TypeError):
                    print("\033[31mERRO!! Por favor insira penas numeros inteiro ou reais...\033[m")
            while True:
                try:
                    identificador = int(input("Insira o id do projeto, a ser mudado: "))
                    break
                except (TypeError,ValueError):
                    print("\033[31mERRO!!, Por favor insira apenas numeros inteiros ou reais...\033[m")
            
            comando = f"""UPDATE horastrabalhadas.projetos SET valor_hora = {valor} WHERE idprojeto = '{identificador}'"""
        
            cursor.execute(comando)
            
            conexao_banco.commit()
            print("\033[32mValor alterado com sucesso!\033[m")
        except TypeError as e:
            print(f"ERRO: {e}")
        except mysql.connector.Error as e:
            print(f"ERRO: {e}")
        
        
        finally:
            cursor.close()
            conexao_banco.close()
            break
          
    
    
def horas_trab():
    """
    Está função,faz uma consulta das horas trabalhas em todos os projetos cadastrados no banco de dados.
    """
    conexao_banco = estabelecer_conexao()
    while True:
        try:
            cursor = conexao_banco.cursor()
            comando = "SELECT nome,horastrab FROM projetos"
            cursor.execute(comando)
            resultado = cursor.fetchall()
            for i in resultado:
                nome, horatrab = i
                print(f"Projeto: {nome}")
                sleep(0.60)
                print(f"Horas trabalhadas {horatrab}")
                sleep(0.60)
            break
        except TypeError as e:
            print(f"ERRO: {e}")
        except mysql.connector.Error as e:
            print(f"ERRO: {e}")
        finally:
            cursor.close()
            conexao_banco.close()
        
        
def ver_projetos():
    """
    Está função, mostra todas as estatísticas de todos os projetos que o usuário cadastrou.
    """
    conexao_banco = estabelecer_conexao()
    try:
        cursor = conexao_banco.cursor()
        comando = "SELECT * FROM projetos"
        cursor.execute(comando)
        resultados = cursor.fetchall()
        for i in resultados:
            idprojeto,nome,horas_trab,valorhora,data = i
            print(f"Projeto ID: {idprojeto}")
            sleep(0.60)
            print(f"Nome: {nome}")
            sleep(0.60)
            print(f"Horas trab: {horas_trab} horas")
            sleep(0.60)
            print(f"Valor/hora: R${valorhora}")
            sleep(0.60)
            print(f"Data Inicio: {data}")        
    except TypeError as e:
        print(f"Erro: {e}")
    except mysql.connector.Error as e:
        print(f"ERRO: {e}")
    finally:
        cursor.close()
        conexao_banco.close()

    
def novo_projeto():
    """
    Esta função, cadastra um novo projeto ao seu banco de dados, ela pede todas as informações que seram imprimidas na função ver_projetos
    """
    conexao_banco = estabelecer_conexao()
    while True:
        cursor = conexao_banco.cursor() 
        try:
            while True:  
                try: 
                    nome = str(input("Nome do projeto: "))
                    break
                except TypeError:
                    print("ERRO! Este campo aceita apenas caracteres...")
            try:     
                data = int(input("Data de inicio: "))
                horastrab = int(input("Horas trabalhas: "))
                valorhora = float(input("Valor hora: R$ "))
                break
            except (TypeError,ValueError):
                print("ERRO! Insira apenas numeros reais ou inteiros por favor...")
            comando = f"""INSERT INTO projetos (nome, horastrab , valor_hora, data) VALUES ('{nome}', {horastrab} ,{valorhora},{data})"""
            
            cursor.execute(comando)
            conexao_banco.commit()
        except TypeError as e:
            print(f"ERRO:{e}")
        except mysql.connector.Error as e:
            print(f"ERRO: {e}")
        finally:
            print("\033[32mNovo projeto inserido com sucesso!!\033[m")
            cursor.close()
            conexao_banco.close()
    
    
def soma_horas_trab():
    """
    Está função, permite o usuário adicionar horas trabalhas em um projeto.
    """
    conexao_banco = estabelecer_conexao()
    while True:
        cursor = conexao_banco.cursor()
        try:        
            try:
                idprojeto = int(input("Id do projeto a ser alterado: "))
                somatrab = float(input("Quantas horas trabalhou hoje:  "))
                break
            except (ValueError,TypeError):
                print("ERRO! Este campo aceita apenas numeros reais ou inteiros...")
        
            comando = f"""UPDATE projetos SET horastrab = horastrab + {somatrab} WHERE idprojeto = {idprojeto}"""
            cursor.execute(comando)
            conexao_banco.commit()

        except Exception as e:
            print(f"Erro: {e}")
        finally:
            print(f"\033[32mHoras trabalhadas no projeto {idprojeto} atualizadas com sucesso.\033[m")
            cursor.close()
            conexao_banco.close()
            