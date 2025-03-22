from pathlib import Path

ROOT_PATH = Path(__file__).parent

# try:
#     arquivo = open('meuarquivo.py')
# except FileNotFoundError as exc:
#     print("Arquivo não encontrado!")
#     print(exc)
    
# try:
#     arquivo = open(ROOT_PATH / "Novo-Diretorio")
# except IsADirectoryError as exc:
#     print(f"Não foi possível abrir o arquivo: {exc}")

try:
    arquivo = open(ROOT_PATH / "Novo-Diretorio" / "Novo.txt", 'r')
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc)
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")   
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")