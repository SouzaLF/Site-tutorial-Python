import streamlit as st
import webbrowser
from PIL import Image
import pandas as pd

st.markdown("<h1 style='text-align: center; color: #0000CD;'><b>Iniciei.PY\n\n\n</b></h1>", unsafe_allow_html=True) 
"\n""\n"
st.markdown("<h2 style='text-align: left; color: Black;'><b><center>Iniciando com a linguagem Python\n</center></b></h2>", unsafe_allow_html=True)
st.info("Aqui você aprenderá a programar em Python de maneira objetiva e direta. Portanto, vamos ao que\ninteressa!")

st.markdown("<h3 style='text-align: left; color: #20B2AA;'><b>Passo 1: Instalando o interpretador da linguagem\n</b></h3>", unsafe_allow_html=True)
st.text('Interpretador -  é um programa que aceita comandos escritos em Python e os executa, linha a linha.\nEle verifica se o programa foi escrito corretamente (exibindo mensagens de erro).\n\nObservação: Existem vários interpretadores disponíveis como o VSCode, o PyCharm, etc. Aqui vamos\nusar o "IDLE" por ser fácil e simples instalar e de utilizá-lo.')

if st.button('Link para download'):
    webbrowser.open_new_tab('https://www.python.org/downloads/')

image2 = Image.open('C:/Users/lfsou/OneDrive/Documentos/CONTEÚDO/Download.png')
st.image(image2, caption= "Realizando o download no site...", use_column_width=True)

image3 = Image.open('C:/Users/lfsou/OneDrive/Documentos/CONTEÚDO/menu iniciar.png')
st.image(image3, caption= 'No menu iniciar pesquise "IDLE" e execute como administrador...', use_column_width=True)

#Passo 2 e 3
#st.markdown("<h2 style='text-align: left; color: Black;'><b><center>Primeiros Programas em Python\n</center></b></h2>", unsafe_allow_html=True)
"\n"
#Print
st.markdown("<h3 style='text-align: left; color: #20B2AA;'><b>Passo 2: Exibindo seu nome no programa\n</b></h3>", unsafe_allow_html=True)
st.text('Copie o código após ">>>" e cole no seu interpretador substituindo "Gabriel" pelo seu nome,\nincluindo as aspas, e veja o que acontece')
code1 = '''
>>> print("Gabriel")
A saída será => Gabriel'''
st.code(code1, language='python')
#Operadores matemáticos
st.markdown("<h3 style='text-align: left; color: #20B2AA;'><b>Passo 3: Operadores aritméticos\n</b></h3>", unsafe_allow_html=True)
st.text("Os operadores aritméticos são utilizados na execução de operações matemáticas, tais como a soma e a\nsubtração, por exemplo.")
operadores = {'Soma': '+', 'Subtração': '-', 'Multiplicação': '*', 'Divisão': '/', 'Exponenciação': '**', 'Resto da divisão': '%'}
op = pd.DataFrame(list(operadores.items()),
            columns=['Operação', 'Operador'])
op
"\n"
st.markdown("<h6 style='text-align: left; color: black;'><b>Exemplos:\n</b></h6>", unsafe_allow_html=True)
'\n'
code2 = '''
#Soma
>>> print(2+2)
4'''
st.code(code2, language='python')
code3 = '''
#Operadores
>>> print(10%3*10**2+1-10*4/2)
81'''
st.code(code3, language='python')
#passo 4
st.markdown("<h3 style='text-align: left; color: #20B2AA;'><b>Passo 4: Criar variável\n</b></h3>", unsafe_allow_html=True)
st.text('Criamos uma variável para armazenar um dado qualquer. Este processo é chamado "declaração de\nvariável".')
code4 = '''
#Variáveis
>>> Altura = 36
>>> Lucro = 50
'''
st.code(code4, language='python')

code5 = '''
#Exibindo valores das variáveis
>>> print(Altura)
36
>>> print(Lucro)
50
'''
st.code(code5, language='python')

#passo 5
st.markdown("<h3 style='text-align: left; color: #20B2AA;'><b>Passo 5: Tipificação em python\n</b></h3>", unsafe_allow_html=True)
st.text("Você pode alterar o tipo de uma variável durante a execução do código e o Python não lançará\nnenhuma Exception.")
operadores = {'<class "str">': 'Informação textual', '<class "int">': 'Números inteiros', '<class "bool">': 'True/False', '<class "float">': 'Números flutuante', '<class "complex">': 'Números complexos'}
tipo = pd.DataFrame(list(operadores.items()),
            columns=['Tipo', 'Descrição'])
tipo
"\n"
st.markdown("<h6 style='text-align: left; color: black;'><b>Exemplos:\n</b></h6>", unsafe_allow_html=True)
'\n'
code6 = '''
#String
>>> print(str(Altura) + str(Lucro))
3650'''
st.text('A função "str"" converte as variáveis "Altura" e "Lucro" no tipo texto. Neste caso, o python\nune as duas variáveis do tipo texto agora.')
st.code(code6, language='python')
'\n'
code7 = '''
#int
>>> print(int(Altura) + int(Lucro))
86'''
st.text('Já a função "int" converte as variáveis em números inteiros.')
st.code(code7, language='python')

#passo 6
st.markdown("<h3 style='text-align: left; color: #20B2AA;'><b>Passo 6: Programa que solicita valores para a variável\n</b></h3>", unsafe_allow_html=True)
operadores = {'int()': 'Números inteiros', 'float()': 'Números em ponto flutuante', 'str() ': 'Informação textual', 'bool()': 'Valores booleanos', 'complex()': 'Números complexos'}
tipo = pd.DataFrame(list(operadores.items()),
            columns=['Função', 'Conversão em'])
tipo
"\n"
st.markdown("<h6 style='text-align: left; color: black;'><b>Exemplos:\n</b></h6>", unsafe_allow_html=True)
'\n'
code8 = '''
#Input
>>> Valor = input("Digite um número qualquer:")
Digite um número qualquer: 10 #Número informado
>>> print(Valor)
10

>>> Valor = input("Digite um número qualquer:")
Digite um número qualquer: 1000 #Número informado
>>> print(Valor)
1000'''
st.code(code8, language='python')
'\n'
st.text('Os dados recebidos pela função input são do tipo <class "str">. Para converter qualquer valor,\nbasta escolher a função de conversão que deseja.')
code9 = '''
#Conversão
>>> Valor = input("Digite um número qualquer:")
Digite um número qualquer: 8 #Número informado
#inteiro
>>> print(int(Valor))
8

#real
>>> print(float(Valor))
8.0'''
st.code(code9, language='python')
#passo 7
st.markdown("<h3 style='text-align: left; color: #20B2AA;'><b>Passo 7: sugestão\n</b></h3>", unsafe_allow_html=True)
arredondamento = {'round': 'Números inteiros', 'float()': 'Números em ponto flutuante', 'str() ': 'Informação textual', 'bool()': 'Valores booleanos', 'complex()': 'Números complexos'}
tipo = pd.DataFrame(list(operadores.items()),
            columns=['Função', 'Conversão em'])
tipo





#passo 7
st.markdown("<h3 style='text-align: left; color: #20B2AA;'><b>Passo 8: Aplicação 1\n</b></h3>", unsafe_allow_html=True)
#Aplicação1
st.text("1 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em\ngraus Celsius. Função de conversão C = 5 * ((F-32) / 9).")
code10 = '''
#Passo1
>>> Fahrenheit = input("Digite a temperatura em Fahrenheit:")
Digite a temperatura em Fahrenheit: 82.4

#Passo2
>>> Conversão = 5 * ((float(Fahrenheit)-32) / 9)
>>> print("Temperatura em celsius =", "%.2f" % Conversão,"°")  #("%.2f" %) arredondamento com duas casas decimais
Temperatura em celsius = 28.00 °
'''
st.code(code10, language='python')
'\n'
st.markdown("<h3 style='text-align: left; color: #20B2AA;'><b>Passo 9: Aplicação 2\n</b></h3>", unsafe_allow_html=True)
#Aplicação2
st.text("2 - Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.\nCalcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o\nImposto de Renda, 8% para o INSS e 5% para o Sindicato.")
code11 = '''
#Opção1
>>> Valor_hora = float(input("Informe qual o valor da hora trabalhada:"))
>>> Horas_trabalhadas = float(input("Informe o total de horas trabalhas no mês:"))
>>> Salário_bruto = Valor_hora * Horas_trabalhadas
>>> Descontos = Salário_bruto * ((11+8+5)/100)
>>> Salário_líquido = Salário_bruto - Descontos
>>> print("Seu salário total =", Salário_líquido)

#Opção2
>>> Valor_hora = float(input("Informe qual o valor da hora trabalhada:"))
>>> Horas_trabalhadas = float(input("Informe o total de horas trabalhas no mês:"))
>>> print("Seu salário total =", ((Valor_hora * Horas_trabalhadas) - ((Valor_hora * Horas_trabalhadas) * ((11+8+5)/100))))
'''
st.code(code11, language='python')