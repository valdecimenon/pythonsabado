#formatacao.py


valor1 = 10
valor2 = 20.9
#primeira forma de formatação: usando %
print("v1 = R$ %d v2 = R$ %.2f" % (valor1, valor2))

#segunda forma de formatação: {}
print("v1 = R$ {} v2 = R$ {:.2f}".format(valor1, valor2))

print("Olá Sr. {0} {1}".format("Joao", "Ferreira"))
print("Sobrenome: {1} \tNome: {0}".format("Joao", "Ferreira"))

print("R$ {:10.1f}".format(1000.12))  #total de 10 posições sendo 1 decimal
print("R$ {:07.2f}".format(4.11))       #total de 7 posições sendo 2 decimais

#terceira forma de formatação: f-string
#a partir da versão 3.6 do python foi incluido o recurso chamado: f-string
nome = "Matheus"
print(f'Meu nome é {nome}')

print(f'Menu nome é {nome.lower()}')
