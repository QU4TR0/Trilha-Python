# Construtores e destrutores
class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe...")

    def latir(self):
        print("auau")

def criar_cachorro():
    c = Cachorro("Chapie", "Branco")
    print(c.nome)