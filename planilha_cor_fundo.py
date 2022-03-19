#planilha_cor_fundo.py

import xlsxwriter
import os
import datetime

caminhoArquivo = "terceiro_arquivo.xlsx"

workbook = xlsxwriter.Workbook(caminhoArquivo)

#propriedades da planilha
workbook.set_properties({
    'category' : 'Estudante',
    'title' : 'Arquivo do Excel criado com python',
    'subject' : 'Aula Python Excel',
    'author' : 'Valdeci Menon',
    'company' : 'SOFTGRAF Cursos Avançados',
    'create' : datetime.date(2022, 3, 5),
    'comments' : 'Bem vindo ao Python para Excel'
})

#cria uma nova sheet em branco com o nome de Dados
worksheet = workbook.add_worksheet('Dados')

#armazena a cor amarela para ser usada como cor de fundo na célula
corFundo = workbook.add_format({'fg_color' : 'yellow'})

#armazena a cor azul para ser usada como cor da fonte 
corFonte = workbook.add_format()
corFonte.set_font_color('blue')

#adiciona dados no worksheet
worksheet.write('A1', 'Nome', corFundo)
worksheet.write('B1', 'Idade', corFundo)
worksheet.write('A2', 'João da Silva')
worksheet.write('B2', 33, corFonte)
worksheet.write('A3', 'Maria da Silva')
worksheet.write('B3', 32, corFonte)

#fecha arquivo
workbook.close()

#abre planilha
os.startfile(caminhoArquivo)
