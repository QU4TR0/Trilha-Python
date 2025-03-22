class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro = 18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        self.marcha = 1

    def buzinar(self):
        print("Plim Plim")

    def parar(self):
        print("Parando Bicicleta ...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vruummmm")

    # def __str__(self):
    #     return f"Bicicleta: Cor: {self.cor}, Modelo: {self.modelo}, Ano: {self.ano}, Valor: {self.valor}"

    def trocar_marcha(self, nro_marcha):
        print("Trocando marcha")

        def _trocar_marcha():
            if nro_marcha > self.marcha:
                print("Marcha trocada... ")
            else:
                print("Não foi possível trocar de marcha...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
b1.buzinar()
b1.parar()
b1.correr()
print(b1)