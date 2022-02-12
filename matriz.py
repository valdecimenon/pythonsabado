#matriz.py

print('Matriz usando lista...')
matriz = [
                 [1,2,5,6],
                 [3,4,8,9],
                 [3,4,8,9],
                 [1,2,5,6]
              ]

print(matriz)
#   linha=0, coluna=0
print(matriz[0][0])
#   linha=3 coluna=3
print(matriz[3][3])

#imprime cada linha da matriz
for linha in matriz:
    print(linha)

#definindo uma matriz com o elemento *
qlinhas = int(input('\nQuantidade de linhas: '))
qcolunas = int(input('\nQuantidade de colunas: '))

linha = [0] * qcolunas
matriz = [linha] * qlinhas
for linha in matriz:
    print(linha)


