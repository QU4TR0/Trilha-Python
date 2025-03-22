import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

ID_COLUNM = 0
ID_NAME = 1

# try:
#     with open(ROOT_PATH / 'Users.csv', 'w', encoding='utf-8') as arquivo:
#         writer = csv.writer(arquivo)
#         writer.writerow(['id','nome'])
#         writer.writerow(['1','Maria'])
#         writer.writerow(['2','João'])
# except IOError as exc:
#     print(f'Erro ao criar o arquivo: {exc}')

# try:
#     with open(ROOT_PATH / 'Alunos.csv', 'r', newline = "",encoding='utf-8') as arquivo:
#         reader = csv.reader(arquivo)
#         for row in reader:
#             print(row)
# except IOError as exc:
#     print(f'Erro ao criar o arquivo: {exc}')

# try:
#     with open(ROOT_PATH / 'Alunos.csv', 'r', newline = "",encoding='utf-8') as arquivo:
#         reader = csv.reader(arquivo)
#         for idx, row in enumerate(reader):
#             if idx == 0:
#                 continue
#             print(f'ID: {row[ID_COLUNM]}')
#             print(f'Name: {row[ID_NAME]}')
# except IOError as exc:
#     print(f'Erro ao criar o arquivo: {exc}')

try:
    with open(ROOT_PATH / 'Alunos.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader.fieldnames)
        for row in reader:
            print(f'ID: {row['RA']}')
            print(f'Name: {row['NOME']}')
            print(f'CPF: {row['CPF']}\n')
except IOError as exc:
    print(f'Erro ao criar o arquivo: {exc}')