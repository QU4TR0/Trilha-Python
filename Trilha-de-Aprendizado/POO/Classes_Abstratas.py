# ABC: Abstract Base Class
from abc import ABC, abstractmethod


class ControleRemoto(ABC):

    @abstractmethod    
    def ligar(self):
        pass

    @abstractmethod 
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado")
        print("Ligada!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligada!")

    @property
    def marca(self):
        return "Midea"

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)