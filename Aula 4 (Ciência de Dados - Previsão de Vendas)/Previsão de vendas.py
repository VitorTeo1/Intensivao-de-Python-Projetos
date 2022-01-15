# Projeto Ciência de Dados - Previsão de Vendas

#- Nosso desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios nas 3 grandes redes que a empresa Hashtag investe: TV, Jornal e Rádio

#- Base de Dados: https://drive.google.com/drive/folders/1o2lpxoi9heyQV1hIlsHXWSfDkBPtze-V?usp=sharing

# Lógica utilizada

# Passo 1: Entendimento do contexto do desafio (área de vendas)
# Passo 2: Entendimento da Área/Empresa
# Passo 3: Extração/Obtenção dos dados
# Passo 4: Ajuste de Dados (Tratamento/Formatação)
# Passo 5: Análise Exploratória
# Passo 6: Modelagem + Algoritimos (Aqui que entra a Inteligência Artificial)
# Passo 7: Interpretação de Resultados 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn

tabela = pd.read_csv("advertising.csv")
tabela.info()

# Criar gráfico com seaborn

# Exibir gráfico com plt

# O gráfico utilizado aqui será o de coorelação, quanto mais próximo de 1 a coorelação estiver, maior é a precisão e a certeza da interferência
# O Annot é o número que serve para incluir os números na tabela de coorelação, é recomendado sempre incluir.
# Cmap é a seleção de cores

sns.heatmap(tabela.corr(), cmap="Wistia", annot=True)

plt.show()

y = tabela["Vendas"] # Esse é quem eu quero prever
#Para coletar mais de uma coluna da tabela é utilizado dois colchetes
x = tabela[["TV", "Radio", "Jornal"]] # Esse é quem eu vou usar para fazer a previsão

from sklearn.model_selection import train_test_split

#ele separa 80% dos dados como treino e 20% como dados de teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)

# Modelos utilizados: Regressão linear e Árvore de Decisão

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

#criando a inteligência
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

#Treino da inteligência artificial
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

#qual é o melhor modelo? comparação entre os dois
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

from sklearn import metrics

print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_arvoredecisao))

# Visualização gráfica das previsões dos dois modelos
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste
tabela_auxiliar['Previsão Regressão Linear'] = previsao_regressaolinear
tabela_auxiliar['Previsão Árvore da Decisão'] = previsao_arvoredecisao

plt.figure(figsize=(14,4)) #para aumentar o tamanho do gráfico
sns.lineplot(data=tabela_auxiliar)
plt.show()

novos = pd.read_csv("novos.csv") #aqui vai ser a tabela dos investimentos no mês seguinte 
previsao = modelo_arvoredecisao.predict(novos) # e aqui vai estar a previsão

print(previsao) # nesse print é informado a previsão da tabela (novos).