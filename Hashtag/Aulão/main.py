#Passo a passo do projeto

#1. Abrir o sistema da empresa

# entrar no site do sistema (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
import pyautogui as  pgui
import time
import pandas as pd

pgui.PAUSE = 0.5

# abrir o navegador
pgui.press('win') 
pgui.write('edge')
pgui.press('enter')

# entrar no site do sistema
pgui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pgui.press('enter')

#para garantir que o site vai carregar
time.sleep(3)
#2. Fazer login
pgui.click(x=805, y=387)
pgui.write('antoniacomi.gs@gmail.com')
pgui.press('tab')
pgui.write('123senha')
pgui.press('tab')
pgui.press('enter')

time.sleep(3)

#3. Abrir/Importar a base de dados de produtos para cadastrar
tabela = pd.read_csv('produtos.csv')

#4. Cadastrar um produto
codigo = 'MOLO000251'
pgui.press('tab')
pgui.write(codigo)
pgui.press('tab')

#5. Repetir issto tudo até acabar a lista de produtos