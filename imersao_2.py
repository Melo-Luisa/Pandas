#Aula 2 - Preparação e Limpeza de Dados
import pandas as pd
import numpy as np
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

#valores que estão faltando
#print(df.isnull())

#somou tudo que é nulo 
#print(df.isnull().sum())

#print(df['ano'].unique())

#um filtro mais completo indo de fora para dentro 
#selecionamos a base, detro dela só os valores Nan e desses valores qualquer um em colunas mas linha por linha 
#print(df[df.isnull().any(axis=1)])

#colocar a media do dado é um boa prática para substituir os dados Nan

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
#print(df_salario)

#Novo DataFrame - Tempestade
df_temperatura = pd.DataFrame({
    'Dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    'temperatura': [np.nan, np.nan, np.nan, 28, 27]
})

#ffill - forward fill - preencher conforme o proximo
df_temperatura['preenchido_ffill'] = df_temperatura['temperatura'].ffill()
#bfill - back fill - preenchido conforme o anterior
df_temperatura['preenchido_bfill'] = df_temperatura['temperatura'].bfill()
# print(df_temperatura)

df_cidades = pd.DataFrame({
    'nomes': ['Ana', 'Bruno', 'Carol', 'Daniel', 'Val'],
    'cidade': ['Sao Paulo', np.nan, 'Curitiba', np.nan, 'Belem']
})

#criando uma nova coluna chamada cidade_preenchida para preencher como Não informado
df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna('Não informado')
# print(df_cidades)

df_limpo = df.dropna()
#isnull - mostra os valores null na tabela
# print(df_limpo.isnull().sum())
print(df_limpo.info())

#transformar float para int (ano)
df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))
print(df_limpo.head())

