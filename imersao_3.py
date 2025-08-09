#Aula 2 - Preparação e Limpeza de Dados
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

novos_nomes = {
    "work_year": "ano",
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location':'empresa',
    'company_size': 'tamanho_empresa'
}
df.rename(columns=novos_nomes, inplace=True)
df.head()
senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}
df['senioridade'] = df['senioridade'].replace(senioridade)
df['senioridade'].value_counts()

contrato = {
    'FT': 'Full Time',
    'PT': 'Part Time',
    'CT': 'Temp',
    'FL': 'Freela'
}
df['contrato'] = df['contrato'].replace(contrato)
df['contrato'].value_counts()

#ordem não importa
tamanho_empresa={
    'L': 'Large',
    'S': 'Small',
    'M': 'Medium'
}

df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
df['tamanho_empresa'].value_counts()

mapa_trabalho = {
    0: 'presencial', 
    50: 'hibrido',
    100: 'remoto'
}

df['remoto'] = df['remoto'].replace(mapa_trabalho)
df['remoto'].value_counts()

#Vamos criar um novo DataFrame - teste
df_salario = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Val'],
    'salario': [4000, np.nan, 5000, np.nan, 100000]
})

#criamos uma nova coluna para mostrar a media e substitui a média e arredonda
df_salario['salario_media'] = df_salario['salario'].fillna(df_salario['salario'].mean().round(2))
#criamos uma nova coluna para mostrar mediana 
#Revisar Estatistica!!
df_salario['salario_mediana'] = df_salario['salario'].fillna(df_salario['salario'].median())

df_limpo = df.dropna()

#transformar float para int (ano)
df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))
df_limpo.head()

'''
AULA 3 - criandoo gráficos e contando histórias
Lembrete: no vscode devemos baicar o matplotlib e seaborn
Neles sempre devemos usar o plt.show() para geração de gráficos
'''
# df_limpo['senioridade'].value_counts().plot(kind='bar', title='Distribuição de Senioridade')
# sns.barplot(data=df_limpo, x='senioridade', y='usd')
# plt.show()

#vamos organizar a tabela acima com matplolib
# plt.figure(figsize=(10,5))
# sns.barplot(data=df_limpo, x='senioridade', y='usd')
# plt.title("Salario médio por senioridade")
# plt.xlabel("Senioridade")
# plt.ylabel("Salário médio anual (USD)")
# plt.show()

#chamando a tabela de senioridade do menor para o maior, sendo a média dos salarios, o index trazendo apenas os títulos
ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).index #lembrando que o ascending é a ordem crescente ou decrescente
# print(ordem)

#novo gráfico dessa ordem
# plt.figure(figsize=(10,5))
# sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem)
# plt.title("Salario médio por senioridade")
# plt.xlabel("Senioridade")
# plt.ylabel("Salário médio anual (USD)")
# plt.show()

#mais uma análise, gráfico em histplot - histograma
# plt.figure(figsize=(10,5))
# sns.histplot(df_limpo['usd'], bins=50,kde=True)
# plt.title("Distribuição de salários anuais")
# plt.xlabel("Salario em USD")
# plt.ylabel("Frequencia")
# plt.show()

#gráfico boxplot - interessante para estatistica
# plt.figure(figsize=(8,5))
# sns.boxplot(x=df_limpo['usd'])
# plt.title("Boxplot Salário")
# plt.xlabel("Salário em USD")
# plt.show()

#juntando categorias
# ordem_senioridade = ['Junior', 'Pleno', 'Senior', 'Executivo']
# plt.figure(figsize=(8,5))
# sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade') #trazendo cores
# plt.title("Boxplot Distribuição por Senioridade")
# plt.xlabel("Salário em USD")
# plt.show()

#Usando gráficos INTERATIVOS

# senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()

# fig = px.bar(senioridade_media_salario,
#              x='senioridade',
#              y='usd',
#              title='Média Salarial por Senioridade',
#              labels={'senioridade': 'Nível de Senioridade', 'usd': 'Média Salarial Anual (USD)'})

# fig.show()

#Grafico estilo pizza/torta
# remoto_contagem= df_limpo['remoto'].value_counts().reset_index()
# remoto_contagem.columns = ['Tipo de trabalho', 'quantidade']

# fig = px.pie(remoto_contagem,
#              names='Tipo de trabalho',
#              values='quantidade',
#              title='Proporção dos tipos de trabalho'
#              )

# fig.show()

#grafico estilo rosca
# remoto_contagem= df_limpo['remoto'].value_counts().reset_index()
# remoto_contagem.columns = ['Tipo de trabalho', 'quantidade']

# fig = px.pie(remoto_contagem,
#              names='Tipo de trabalho',
#              values='quantidade',
#              title='Proporção dos tipos de trabalho',
#              hole=0.5
#              )

# fig.show()
     
#Melhorando leitura do Gráfico de Rosca

remoto_contagem= df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['Tipo de trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
             names='Tipo de trabalho',
             values='quantidade',
             title='Proporção dos tipos de trabalho',
             hole=0.5
             )
fig.update_traces(textinfo='percent+label')
fig.show()