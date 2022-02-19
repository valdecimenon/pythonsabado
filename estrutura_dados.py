#estrutura_dados.py

#lista = contém elementos duplicados
#contém elementos em ordem = possui índice
#            0                 1              2          3            4         5
lista = ["banana", "laranja", "banana", "uva", "laranja", "uva"]
print(lista)
print(lista[5])
#verifica se tem banana
if lista[0] == 'banana':
    print('Tem banana na lista')
if 'banana' in lista:
    print('Tem banana na lista')

#list comprehension  (compreensão de lista) 
entrada = ['a', 1, 'b', 'c', 2, 3, 'c', 'd']
saida = []
[saida.append(x) for x in entrada if type(x) == int]
print(saida)

#idem
for x in entrada:
    if type(x) == int:
        saida.append(x)


#conjunto = não contém elementos duplicados
#conjunto não possui índice
conjunto=  {"banana", "laranja", "banana", "uva", "laranja", "uva"}
#conjunto = {'uva', 'laranja', 'banana'}
print(conjunto)
#print(conjunto[0])  => erro, não possui indice
if 'banana' in conjunto:
    print('Tem banana no conjunto')

#set comprehension
letras = {x for x in 'abracadabra' if x not in 'abc'}
print(letras)

#dicionario é formado pelo par "chave" : valor
#a chave é o índice do dicionário, portanto não pode ser duplicada
contatos = {'joao' : '3028-0449', 'maria' : '9999-1234'}
print(contatos['joao'])
print(contatos['maria'])
#altera o conteúdo da chave
contatos['joao'] = '3333-4444'

#retorna lista de chaves
print(list(contatos))
#existe luiz no dicionário contatos?
if 'luiz' not in contatos:
    print('Telefone do Luiz não cadastrado')

if 'joao' in contatos:
    print(f'Telefone do João: {contatos["joao"]}')

#dicionário criado a partir de uma lista
lista_contatos = [
                            ('João', '3028-0449'),
                            ('Pedro', '9999-9999'),
                            ('Ana', '8797-4545'),
                            ('Mariana', '3333-1234'),
                          ]
#converte a lista de tuplas em um dicionario de contatos
dic_contatos = dict(lista_contatos)

#imprime as chaves
print(dic_contatos.keys())
#imprime os valores
print(dic_contatos.values())

print('\nLista de todos os contatos')
for nome in dic_contatos.keys():
    print(f'{nome} = {dic_contatos[nome]}')

#apaga um contato
del dic_contatos['Pedro']
if 'Pedro' not in dic_contatos:
    print('Não tem mais Pedro')
