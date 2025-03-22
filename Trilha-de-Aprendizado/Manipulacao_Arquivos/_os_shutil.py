import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
# print(ROOT_PATH.parent) # d:\Faculdade\Curso Python\Trilha-Python\Trilha-de-Aprendizado\Manipulacao_Arquivos

# os.mkdir(ROOT_PATH / 'Novo-Diretorio')

arquivo = open(ROOT_PATH / 'Novo.txt', 'w')
arquivo.close()

# os.rename(ROOT_PATH / "Novo.txt", ROOT_PATH / 'Alterado.txt')

# os.remove(ROOT_PATH / "Alterado.txt")
shutil.move(ROOT_PATH / "Novo.txt", ROOT_PATH / "Novo-Diretorio" / 'Novo.txt')

# print(__file__) # d:\Faculdade\Curso Python\Trilha-Python\Trilha-de-Aprendizado\Manipulacao_Arquivos\_os_shutil.py