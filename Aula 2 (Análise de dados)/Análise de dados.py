# Análise de Dados com Python

#Desafio:

#Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
#O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
#Isso representa uma perda de milhões para a empresa.
#O que a empresa precisa fazer para resolver isso?

#Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing 
#Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset


# Lógica que será aplicada

# Passo 1: Importar a base de dados (ter uma)

# Passo 2: Vizualizar a base de dados para ver o que é possível fazer

# Passo 3: Tratamentos de dados (corrigir os problemas da base de dados) como;
# Coluna inutil
# Valores reconhecidos de forma errada (verificar como está sendo reconhecidos os valores)
# Tratar valores vazios

# IMPORTANTE sempre formatar a base de dados

# Passo 4: Análise inicial (Entender quantas pessoas cancelaram e etc...)

# Passo 5: Análise detalhada

# Informação que não te ajuda, te atrapalha. 
#churn são os cancelamentos do serviço

import pandas as pd

tabela = pd.read_csv(r"telecom_users.csv")

print(tabela)

#drop serve para excluir, ele consegue deletar linhas ou colunas
#axis é o eixo (coluna ou linha)
#axis = 0 -> linha
#axis = 1 -> coluna
#caso queira deletar mais de uma coluna colocar em conchetes, por ex: tabela = tabela.drop(["Unnamed: 0"],[nome tal], axis=1)

tabela = tabela.drop("Unnamed: 0", axis=1)

#Valores non-null são valores que não estão vazios
#object -> Texto
#int -> números inteiros
#float -> números com casa decimal


#transformando a coluna de texto para número
#errors serve para corrigir quando der erro de uma letra naquele local
#método coerce serve para deixar vazio o local em que ocorreu aquele erro
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# Tratando valores vazios
#dropna serve para deletar os valores vazios
#método how="all" exclui apenas as colunas que estão completamente vazias, já o any exclui se houver pelo menos 1 valor vazios
tabela = tabela.dropna(how="all", axis=1) #excluir colunas com todos os valores vazios
tabela = tabela.dropna(how="any", axis=0) #excluir linhas com pelo menos 1 valor vazio

#ver biblioteca do dropna
print(tabela.info())

print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize="true")) #normalize="true" serve para colocar em porcentagem
print(tabela["Churn"].value_counts(normalize="true").map("{:.2%}".format)) #código para formatar em porcentagem

#análize comparativa entre os clientes encontrando um padrão para tirar informações
import plotly.express as px

#histogram serve para fazer análizes comparativas
#para criar será necessário a sua tabela, informações para o eixo x e informações para color

#Para executar o for em várias vezes é necessário ir com o tab para a mesma direção
for coluna in tabela.columns: #define todas as colunas para a variável coluna

    #Aqui ele está comparando todas as colunas de uma vez em um código (Esse código pode demorar para carregar)
    grafico = px.histogram(tabela, x=coluna, color="Churn", color_discrete_sequence=["blue", "green"])
    grafico.show()

    # Conclusão
    # Pessoas com famílias menores tem mais chance de cancelar 
    # Podemos criar um plano família para reduzir os cancelamentos

    # Estamos perdendo muitos clientes nos primeiros meses
    # Pode ser alguma ação promocional que atrai clientes que só querem usufluir
    # A primeira experiência esta sendo ruim

    # Taxa de cancelamento alta na fibra por o serviço estar ruim
    # Quanto mais serviços o cliente tem, menor a chance de cancelamento.

    # A maioria dos cancelamentos está no contrato mensal
    # Como solução pode dar desconto no contrato anual

    # Evitar boleto eletrônico, dar desconto as outras opções