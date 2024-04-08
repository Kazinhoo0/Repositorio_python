import mysql.connector

def banco_db():
    """
    funcão de conexão com DB, e verifiçacão de erros na conexão
    """
    conexao_banco = mysql.connector.connect(
        host='localhost',
        user='root',
        password="",
        database='horastrabalhadas'
    )
    while True:   
        try:
            print("\033[32mBanco de dados conectado com sucesso!!\033[m")
            break
        except mysql.connector.DatabaseError as e :
            print(f"\033[31mERRO {e} Não conseguimos a conectar com o banco de dados.\033[m")
            break
        
    return conexao_banco

           
def estabelecer_conexao():
   try: 
        conexao_banco = mysql.connector.connect(
            host='localhost',
            user='root',
            password="",
            database='horastrabalhadas'
        )
        return conexao_banco
   except mysql.connector.Error as e:
       print(f"ERRO: {e}")
       return conexao_banco, e


