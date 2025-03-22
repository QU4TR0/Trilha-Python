from pathlib import Path

ROOT_PATH = Path(__file__).parent

# try:
#     with open(ROOT_PATH / 'Exemplo.txt', 'r', encoding = 'utf-8') as arquivo:
#         print(arquivo.read())
# except IOError as exc:
#     print(f'Erro ao abrir o arquivo: {exc}')


# try:
#     with open(ROOT_PATH / 'UTF8.txt', 'w', encoding = 'utf-8') as arquivo:
#         arquivo.write('Manipulando arquivos com Python.')
# except IOError as exc:
#     print(f'Erro ao abrir o arquivo: {exc}')

try:
    with open(ROOT_PATH / 'UTF8.txt', 'r', encoding = 'ascii') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f'Erro ao abrir o arquivo: {exc}')