# Automação de Sistemas e Processos com Python

# Desafio:

#Todos os dias, o nosso sistema atualiza as vendas do dia anterior.
#O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, assim que começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior

#E-mail da diretoria: seugmail+diretoria@gmail.com<br>
#Local onde o sistema disponibiliza as vendas do dia anterior: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing

#Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

#Passo a passo para resolver o nosso desafio;

#Passo 1: Entrar no sistema da empresa (Link do drive)
#Passo 2: Navegar no sistema (até a pasta Exportar)
#Passo 3: Fazer o download da base de vendas
#Passo 4: Importar a base de vendas pro Python
#Passo 5: Calcular o faturamento e quantidade de produtos vendidos (os indicadores)
#Passo 6: Enviar email para diretoria 

#AVISO esse código foi programado para um tipo de tela em específico, ou seja na sua tela pode não funcionar corretamente. 
# Na aula 3 foi utilizado uma biblioteca que funciona em qualquer tela.
import pyautogui
import pyperclip
import pandas as pd
from IPython.display import display
import time

# É necessário um tempo de delay para que não haja problemas ao executar o código, e pra isso é utilizado o pyautogui.PAUSE
pyautogui.PAUSE = 1 # Aqui é definido 1 segundo de delay para contabilizar cada clique


#Press serve para apertar uma tecla
pyautogui.press("win")
pyautogui.write("Microsoft Edge Canary")
pyautogui.press("enter")
#click serve para clicar na tela com o mouse
#pyautogui.hotkey("ctrl", "t")

#hotkey serve para pressionar duas teclas juntas como por exemplo: CTRL+T
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga") #copiando o link
pyautogui.hotkey("ctrl", "v") #colando o link
pyautogui.press("enter") #entrando no arquivo
time.sleep(5) #dando um delay para que não tenha erro nos cliques
pyautogui.click(x=332, y=272, clicks=2)
time.sleep(3)
pyautogui.click(x=388, y=347)
time.sleep(2)
pyautogui.click(x=1395, y=160)
time.sleep(1)
pyautogui.click(x=1140, y=643)

# Para que o código aceite caracteres especiais é utilizado o pyperclip

tabela = pd.read_excel(r"E:\Meus Documentos\Downloads\Vendas - Dez.xlsx")
#Sempre colocar um r quando for ler um caminho de um arquivo
#para alterar a aba apenas ir em sheets
display(tabela)
#é necessário informar o caminho néeee

faturamento = tabela["Valor Final"].sum()
qtde_produtos = tabela["Quantidade"].sum()
display(faturamento)
display(qtde_produtos)

#EMAIL AUTOMÁTICO
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/1/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=84, y=175)

pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.press("tab")
pyautogui.press("tab")

pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

#f antes do texto serve para formatar a receber variáveis e colocar a variável entre chaves
#o código de formatação para valores está abaixo como :,.2f 
texto = f"""
Bom dia prezados.
Segue abaixo o faturamento obtido e a quantidade de produtos vendidos;

Faturamento: R$ {faturamento:,.2f}

Quantidade de produtos:  {qtde_produtos:,}
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")