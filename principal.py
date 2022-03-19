#principal.py

from veiculos import *

def principal():

    veiculo = Veiculo('Marca', 'modelo', 'AXX-1234', 1)

    carro = Carro('WV', 'Polo', 'ABC-1234', 2020, 'Branco')
    moto = Motocicleta('Honda', 'CG 160', 'MMM-1234', 2021, 600)

    veiculo.abastecer()
    #chama __str__ automaticamente
    print(veiculo)

    lista = [veiculo, carro, moto, 'banana', 123, 3.14]

    for item in lista:
        if (isinstance (item, Carro)):
            print('Temos um carro na lista')
        elif (isinstance (item, Motocicleta)):
            print('Temos uma motocicleta na lista')
        elif (isinstance (item, Veiculo)):
            print('Temos um veiculo na lista')
        elif (isinstance (item, str)):
            print('Temos uma string na lista')
        elif (isinstance (item, int)):
            print('Temos um int na lista')
        else:
            print('Valor desconhecido na lista')

    

if __name__ == '__main__':
    principal()
