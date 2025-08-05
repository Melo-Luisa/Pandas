#importando biblioteca do python e nomeando como pd
import pandas as pd

#importar um banco de dados atribuindo o nome df - dataframe
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
#banco de dados do kagle

#leitura geral do bd
#usando o print pois estamos usando python no console
print(df.head())

#lembrando também que o pandas mostra apenas os 5 primeiros dados
print(df.head(10))

#imprimi o df mais geral, um resumo técnico
print(df.info())

#tambem mostrando os dados para uma analise mais estatistica, então temos o mean - media / std - / min - minimo / max - maximo e os valores entre 
print(df.describe())

#nos mostra quntas linhas e colunas temos, resultado: (133349, 11)
print(df.shape)

#usando manipulações básicas de python conseguimos mostrar os dados de forma mais organizada como atribuindo a variaveis
linhas, colunas = df.shape[0], df.shape[1] #atribuindo as valores do vetor 
print(f"Linhas: {linhas}\nColunas: {colunas}")

#trazendo as categorias da tabela (as colunas)
print(df.columns)

#Renomeando as categorias para uma fácil absorção
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

#renomeadndo baseado no novo dicionário de categorias
df.rename(columns=novos_nomes, inplace=True)
df.head()

#Selecionando categorias/colunas por vez
print(df['senioridade'].value_counts())
print(df['ano'].value_counts())
print(df['cargo'].value_counts())
print(df['contrato'].value_counts())
#podemos fazer com todos

#********************Renomeando Siglas para Portugues**************************
senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}
df['senioridade'] = df['senioridade'].replace(senioridade)
print(df['senioridade'].value_counts())

contrato = {
    'FT': 'Full Time',
    'PT': 'Part Time',
    'CT': 'Temp',
    'FL': 'Freela'
}
df['contrato'] = df['contrato'].replace(contrato)
print(df['contrato'].value_counts())

#ordem não importa
tamanho_empresa={
    'L': 'Large',
    'S': 'Small',
    'M': 'Medium'
}

df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
print(df['tamanho_empresa'].value_counts())

mapa_trabalho = {
    0: 'presencial', 
    50: 'hibrido',
    100: 'remoto'
}

df['remoto'] = df['remoto'].replace(mapa_trabalho)
print(df['remoto'].value_counts())

print(df.head(200))

#alguns dados - quantidade de elementos, tipos de cada categorias, maior elemento de cada categoria, frequencia de cada categoria
print(df.describe(include='object'))