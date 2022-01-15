# Automação Web e Busca de Informações com Python

# Desafio: 

#Trabalhamos em uma importadora e o preço dos nossos produtos é vinculado a cotação de:
#- Dólar
#- Euro
#- Ouro

#Precisamos pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto devemos cobrar pelos nossos produtos, considerando uma margem de contribuição que temos na nossa base de dados.

#Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=sharing

#Para isso, vamos criar uma automação web:

# Lógica para calcular a cotação automáticamente

# Passo 1: Pesquisar a cotação do dollar/moeda
# Passo 2: Pesquisar a cotação do euro
# Passo 3: Pesquisar cotação do ouro
# Passo 4: importar a base e atualizar as cotações na minha base
# Passo 5: Calcular os novos preços e salvar/exportar a base de dados

#Selenium fornece o controle total do navegador (é necessário instalar o web driver e colocar na pasta do seu python)
#criar um navegador
#entrar em sites
#encontrar informações / itens no site

import time
import pandas as pd
from typing import Container
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()
#aqui ele vai acessar o navegador e pesquisar as cotações coletando as informações necessárias
navegador.get("https://www.google.com.br/")

#aqui você vai ter que copiar o código que você quer do campo de busca através do inspecionar, o ideal é copiar sempre como XPATH
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
#Aqui ele encontra a cotação do dólar 
cotacao_dolar = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_dolar + " Cotação Dólar")

navegador.get("https://www.google.com.br/")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_euro + " Cotação Euro")

#Para descobrir a cotação do ouro foi necessário entrar em um site externo devido ao google não disponibilizar da mesma forma que o dólar e o euro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')

#trocar a virgula para o ponto
cotacao_ouro = cotacao_ouro.replace(",", ".")

print(cotacao_ouro + " Cotação Ouro")


#agora temos que incluir esses dados na base de dados e calcular eles, tudo isso é feito logo abaixo:
tabela = pd.read_excel("Produtos.xlsx")

#para editar uma tabela específica
#tabela.loc[Linha, Coluna]
#tabela.loc[1, 'Cotaçao'] = float(cotacao_euro)
#pode ser passado ou um n° ou uma condição

#ATENÇÃO A VIRGULA NESSSA PARTE
tabela.loc[tabela["Moeda"] == 'Dólar', 'Cotação'] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == 'Euro', 'Cotação'] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == 'Ouro', 'Cotação'] = float(cotacao_ouro)
#(IMPORTANTE) 2 sinais de igual "==" significa comparação

#Agora vamos atualizar as colunas:

# Preço de compra = preço original * Cotação
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

# Preço de Vendas = Preço de Compra * Margem
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

print(tabela)

# e aqui vamos exportar, Esse index=False significa que ele vai tirar os indices do python.
tabela.to_excel("ProdutosExportadosPy.xlsx", index=False)