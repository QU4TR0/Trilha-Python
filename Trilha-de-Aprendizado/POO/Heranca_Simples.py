class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(veiculo):
    pass

class Carro(veiculo):
    pass

class Caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'}, estou carregado...")

moto = Motocicleta("Azul", "123-456", 2)
moto.ligar_motor()

carro = Carro("Prata", "FAQ-3545", 4)
carro.ligar_motor()

caminhao = Caminhao("Branco", "GFD-1234", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(carro)
print(moto)
print(caminhao)