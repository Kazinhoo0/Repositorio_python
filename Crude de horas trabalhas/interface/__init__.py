def linhas(linhas = 45):
    """_summary_
    Está funcao retorna linhas.
    """
    return ("-" * 45)


def cabeçalho(txt):
    """_summary_
    Está funcão cria um cabecalho simples para o programa.
    """
    print(linhas())
    print(txt.center(45))
    print(linhas())
    
    
    
def opções():
    print("""\n\033[34mSeja Bem-vindo ao seu programa de cadastramento de trabalho. Abaixo as opcões que você pode escolher
          1 - CADASTRAR UM PROJETO.
          2 - VER MEUS PROJETOS CADASTRADOS.
          3 - VER TOTAL DE HORAS TRABALHADAS EM CADA PROJETO
          4 - MODIFICAR MEU VALOR/HORA
          5 - ADICIONAR HORAS TRABALHADAS
          6 - SAIR\033[m""")
    