#veiculos.py

#classe mãe
class Veiculo:

    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

    def __str__ (self):
        return 'Veiculo placa: ' + self.placa

    def ligar(self):
        print('Veiculo ligado...')

    def abastecer(self):
        print('Veiculo abastacendo...')

    

#classe filha
class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cor):
        super().__init__(marca, modelo, placa, ano)
        self.cor = cor

    def ligar(self):
        print('Carro ligado')

    def abastecer(self):
        print('Carro abastacendo...')

#classe filha
class Motocicleta(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cilindrada):
        super().__init__(marca, modelo, placa, ano)
        self.cilindrada = cilindrada

    def ligar(self):
        print('Moto ligada')

    def abastecer(self):
        print('Moto abastacendo...')



