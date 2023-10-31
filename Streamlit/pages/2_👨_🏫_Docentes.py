import streamlit as st
import pandas as pd 
import plotly
import matplotlib
import matplotlib.pyplot as plt
import os
import numpy as np 
import seaborn as sns 
import plotly.express as px

    
st.set_page_config(layout='wide')

st.title(':female-teacher: Docentes das IES')
st.subheader("Dados de 2022")
st.markdown("---")

# ------------------------------------------------------------------------
# Carrega dados docentes
# ------------------------------------------------------------------------

docentes_df = pd.read_csv('./arquivos/docentes.csv', sep='|', low_memory=False)

#Testar o dataframe:
# Exibir as primeiras linhas do DataFrame: st.write(docentes_df.head())  
# Exibir os nomes das colunas no DataFrame: st.write(docentes_df.columns) 

# ------------------------------------------------------------------------
# Plot 01: docentes por sexo geral, pública e privada, com caixa de seleção
# ------------------------------------------------------------------------

titulo_plot01 = '<p style="font-family:Courier; color:blue; font-size: 25px;"><b>Docentes IES por sexo</b></p>'
st.markdown(titulo_plot01, unsafe_allow_html=True)

opcao_sexo = st.selectbox("Selecione a categoria:", ["Geral", "IES Privadas", "IES Públicas"])

# Verificar se o botão de atualização foi pressionado
botao_atualizar = st.button("Atualizar Gráfico")

# Função para criar e exibir o gráfico
def criar_e_exibir_grafico():
    if opcao_sexo == "Geral":
        titulo_plot01 = '<p style="font-family:Courier; color:blue; font-size: 25px;"><b>Geral</b></p>'
        st.markdown(titulo_plot01, unsafe_allow_html=True)
        sexo_feminino = docentes_df['QT_DOC_EX_FEMI']
        sexo_masculino = docentes_df['QT_DOC_EX_MASC']
        labels = ['Feminino', 'Masculino']
        sizes = [sexo_feminino.sum(), sexo_masculino.sum()]
        colors = ['pink', 'lightblue']
        explode = (0.1, 0)
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        ax.axis('equal')
        #ax.set_title('Docentes IES por Sexo')
        st.pyplot(fig)

    elif opcao_sexo == "IES Privadas":
        titulo_plot01 = '<p style="font-family:Courier; color:blue; font-size: 25px;"><b>IES privadas</b></p>'
        st.markdown(titulo_plot01, unsafe_allow_html=True)
        categorias_interesse = [4, 5, 6]
        docentes_interesse = docentes_df[docentes_df['TP_CATEGORIA_ADMINISTRATIVA'].isin(categorias_interesse)]
        sexo_feminino = docentes_interesse['QT_DOC_EX_FEMI']
        sexo_masculino = docentes_interesse['QT_DOC_EX_MASC']
        labels = ['Feminino', 'Masculino']
        sizes = [sexo_feminino.sum(), sexo_masculino.sum()]
        colors = ['pink', 'lightblue']
        fig, ax = plt.subplots(figsize=(8, 4))
        explode = (0.1, 0)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        st.pyplot(fig)
    
    elif opcao_sexo == "IES Públicas":
        titulo_plot01 = '<p style="font-family:Courier; color:blue; font-size: 25px;"><b>IES públicas</b></p>'
        st.markdown(titulo_plot01, unsafe_allow_html=True)
        categorias_interesse = [1, 2, 3]
        docentes_interesse = docentes_df[docentes_df['TP_CATEGORIA_ADMINISTRATIVA'].isin(categorias_interesse)]
        sexo_feminino = docentes_interesse['QT_DOC_EX_FEMI']
        sexo_masculino = docentes_interesse['QT_DOC_EX_MASC']
        labels = ['Feminino', 'Masculino']
        sizes = [sexo_feminino.sum(), sexo_masculino.sum()]
        colors = ['pink', 'lightblue']
        explode = (0.1, 0)
        fig, ax = plt.subplots(figsize=(8, 4))
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        st.pyplot(fig)

# Verificar se o botão de atualização foi pressionado e, em seguida, criar e exibir o gráfico
if botao_atualizar:
    criar_e_exibir_grafico()
st.markdown("---")


# ------------------------------------------------------------------------
# Plot 02: Escolaridade dos docentes
# ------------------------------------------------------------------------

titulo_plot01 = '<p style="font-family:Courier; color:blue; font-size: 25px;"><b>Docentes IES por escolaridade</b></p>'
st.markdown(titulo_plot01, unsafe_allow_html=True)

opcao_estudo = st.selectbox("Selecione a categoria:", ["Geral", "IES Pública", "IES Particular"])

if opcao_estudo == "Geral":
    estudo_columns = ['QT_DOC_EX_GRAD', 'QT_DOC_EX_ESP', 'QT_DOC_EX_MEST', 'QT_DOC_EX_DOUT']
    estudo_labels = ['Graduação', 'Especialização', 'Mestrado', 'Doutorado']
    somas_estudo = docentes_df[estudo_columns].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(estudo_labels, somas_estudo)
    ax.set_xlabel('Nível de Estudo')
    ax.set_ylabel('Quantidade de Docentes')
    st.pyplot(fig)
        
elif opcao_estudo == "IES Pública":
    categorias_interesse = [1, 2, 3]
    docentes_interesse = docentes_df[docentes_df['TP_CATEGORIA_ADMINISTRATIVA'].isin(categorias_interesse)]
    estudo_columns = ['QT_DOC_EX_GRAD', 'QT_DOC_EX_ESP', 'QT_DOC_EX_MEST', 'QT_DOC_EX_DOUT']
    estudo_labels = ['Graduação', 'Especialização', 'Mestrado', 'Doutorado']
    somas_estudo = docentes_interesse[estudo_columns].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(estudo_labels, somas_estudo)
    ax.set_xlabel('Nível de Estudo')
    ax.set_ylabel('Quantidade de Docentes')

    st.pyplot(fig)

elif opcao_estudo == "IES Particular":
    categorias_interesse = [4, 5, 6]
    docentes_interesse = docentes_df[docentes_df['TP_CATEGORIA_ADMINISTRATIVA'].isin(categorias_interesse)]
    estudo_columns = ['QT_DOC_EX_GRAD', 'QT_DOC_EX_ESP', 'QT_DOC_EX_MEST', 'QT_DOC_EX_DOUT']
    estudo_labels = ['Graduação', 'Especialização', 'Mestrado', 'Doutorado']
    somas_estudo = docentes_interesse[estudo_columns].sum()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(estudo_labels, somas_estudo)
    ax.set_xlabel('Nível de Estudo')
    ax.set_ylabel('Quantidade de Docentes')
    
    st.pyplot(fig)
    
st.markdown("---")

# ------------------------------------------------------------------------
# Plot 03: Idade docentes
# ------------------------------------------------------------------------

titulo_plot01 = '<p style="font-family:Courier; color:blue; font-size: 25px;"><b>Docentes IES por idade</b></p>'
st.markdown(titulo_plot01, unsafe_allow_html=True)


idade_columns = ['QT_DOC_EX_0_29', 'QT_DOC_EX_30_34', 'QT_DOC_EX_35_39', 'QT_DOC_EX_40_44',
                 'QT_DOC_EX_45_49', 'QT_DOC_EX_50_54', 'QT_DOC_EX_55_59', 'QT_DOC_EX_60_MAIS']
idade_labels = ['0-29 anos', '30-34 anos', '35-39 anos', '40-44 anos', '45-49 anos',
                '50-54 anos', '55-59 anos', '60 anos ou mais']

# caixa de seleção
opcao_idade = st.selectbox("Selecione a categoria:", ["Geral", "IES Pública", "IES Particular"], key='opcao_idade')

if opcao_idade == "Geral":
    somas_idade = docentes_df[idade_columns].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(idade_labels, somas_idade)
    ax.set_xlabel('Faixa Etária')
    ax.set_ylabel('Quantidade de Docentes')
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif opcao_idade == "IES Pública":
    categorias_interesse = [1, 2, 3]
    docentes_interesse = docentes_df[docentes_df['TP_CATEGORIA_ADMINISTRATIVA'].isin(categorias_interesse)]
    somas_idade = docentes_interesse[idade_columns].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(idade_labels, somas_idade)
    ax.set_xlabel('Faixa Etária')
    ax.set_ylabel('Quantidade de Docentes')
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif opcao_idade == "IES Particular":
    categorias_interesse = [4, 5, 6]
    docentes_interesse = docentes_df[docentes_df['TP_CATEGORIA_ADMINISTRATIVA'].isin(categorias_interesse)]
    somas_idade = docentes_interesse[idade_columns].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(idade_labels, somas_idade)
    ax.set_xlabel('Faixa Etária')
    ax.set_ylabel('Quantidade de Docentes')
    plt.xticks(rotation=45)
    st.pyplot(fig)

st.markdown("---")

# ------------------------------------------------------------------------
# Plot 04: Cor/raça docentes
# ------------------------------------------------------------------------

titulo_plot01 = '<p style="font-family:Courier; color:blue; font-size: 25px;"><b>Docentes IES por raça</b></p>'
st.markdown(titulo_plot01, unsafe_allow_html=True)

#Docentes por Raça/Cor Normalizado e Ordem Decrescente
raca_columns = ['QT_DOC_EX_BRANCA', 'QT_DOC_EX_PRETA', 'QT_DOC_EX_PARDA',
                'QT_DOC_EX_AMARELA', 'QT_DOC_EX_INDIGENA', 'QT_DOC_EX_COR_ND']
raca_labels = ['Branca', 'Preta', 'Parda', 'Amarela', 'Indígena', 'Não Declarada']

# caixa de seleção
opcao_raca = st.selectbox("Selecione a categoria:", ["Geral", "IES Pública", "IES Particular"], key='opcao_raca')

if opcao_raca == "Geral":

    somas_raca = docentes_df[raca_columns].sum()
    # Calcular o total de docentes
    total_docentes = somas_raca.sum()
    # Calcular as porcentagens
    porcentagens_raca = (somas_raca / total_docentes) * 100
    # Organizar as raças em ordem decrescente de porcentagem
    porcentagens_raca, raca_labels = zip(*sorted(zip(porcentagens_raca, raca_labels), reverse=True))

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(raca_labels, porcentagens_raca)
    ax.set_xlabel('Raça/Cor')
    ax.set_ylabel('Porcentagem de Docentes (%)')
    st.pyplot(fig)

elif opcao_raca == "IES Pública":
    categorias_interesse = [1, 2, 3]
    docentes_interesse = docentes_df[docentes_df['TP_CATEGORIA_ADMINISTRATIVA'].isin(categorias_interesse)]
    somas_raca = docentes_interesse[raca_columns].sum()

    # Calcular o total de docentes
    total_docentes = somas_raca.sum()

    # Calcular as porcentagens
    porcentagens_raca = (somas_raca / total_docentes) * 100

    # Organizar as raças em ordem decrescente de porcentagem
    porcentagens_raca, raca_labels = zip(*sorted(zip(porcentagens_raca, raca_labels), reverse=True))
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(raca_labels, porcentagens_raca)
    ax.set_xlabel('Raça/Cor')
    ax.set_ylabel('Porcentagem de Docentes (%)')
    st.pyplot(fig)

elif opcao_raca == "IES Particular":
    categorias_interesse = [4, 5, 6]
    docentes_interesse = docentes_df[docentes_df['TP_CATEGORIA_ADMINISTRATIVA'].isin(categorias_interesse)]
    somas_raca = docentes_interesse[raca_columns].sum()
    # Calcular o total de docentes
    total_docentes = somas_raca.sum()

    # Calcular as porcentagens
    porcentagens_raca = (somas_raca / total_docentes) * 100

    # Organizar as raças em ordem decrescente de porcentagem
    porcentagens_raca, raca_labels = zip(*sorted(zip(porcentagens_raca, raca_labels), reverse=True))

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(raca_labels, porcentagens_raca)
    ax.set_xlabel('Raça/Cor')
    ax.set_ylabel('Porcentagem de Docentes (%)')
    st.pyplot(fig)


st.markdown("---")

# ------------------------------------------------------------------------
# Plot 05: Jornada de trabalho
# ------------------------------------------------------------------------

titulo_plot01 = '<p style="font-family:Courier; color:blue; font-size: 25px;"><b>Docentes IES por jornada de trabalho</b></p>'
st.markdown(titulo_plot01, unsafe_allow_html=True)
jornada_columns = ['QT_DOC_EX_INT_DE', 'QT_DOC_EX_INT_SEM_DE', 'QT_DOC_EX_PARC', 'QT_DOC_EX_HOR']
jornada_labels = ['Integral com Dedicação Exclusiva', 'Integral sem Dedicação Exclusiva', 'Parcial', 'Horista']

# soma para cada categoria
somas_jornada = docentes_df[jornada_columns].sum()

# ordem decrescente
somas_jornada, jornada_labels = zip(*sorted(zip(somas_jornada, jornada_labels), reverse=True))

# Gráfico de barras horizontais
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(jornada_labels, somas_jornada)
ax.set_ylabel('Jornada de Trabalho')
ax.set_xlabel('Quantidade de Docentes')
ax.set_title('Quantidade de Docentes por Jornada de Trabalho (Ordem Decrescente)')

st.pyplot(fig)

st.markdown("---")

# ------------------------------------------------------------------------
# Plot 06: Docentes com deficiência
# ------------------------------------------------------------------------

titulo_plot01 = '<p style="font-family:Courier; color:blue; font-size: 25px;"><b>Docentes IES com deficiência</b></p>'
st.markdown(titulo_plot01, unsafe_allow_html=True)

# Calcular o número de docentes sem deficiência
docentes_df['QT_DOC_SEM_DEFICIENCIA'] = docentes_df['QT_DOC_EXE'] - docentes_df['QT_DOC_EX_COM_DEFICIENCIA']

# Calcular as porcentagens em relação ao número total de docentes
docentes_df['Porcentagem_Com_Deficiencia'] = (docentes_df['QT_DOC_EX_COM_DEFICIENCIA'] / docentes_df['QT_DOC_EXE']) * 100
docentes_df['Porcentagem_Sem_Deficiencia'] = (docentes_df['QT_DOC_SEM_DEFICIENCIA'] / docentes_df['QT_DOC_EXE']) * 100

# Criar o gráfico de pizza
plt.figure(figsize=(8, 8))
labels = ['Com Deficiência', 'Sem Deficiência']
sizes = [docentes_df['Porcentagem_Com_Deficiencia'].sum(), docentes_df['Porcentagem_Sem_Deficiencia'].sum()]
colors = ['#ff9999', '#66b3ff']  # Cores para "Com Deficiência" e "Sem Deficiência"
explode = (0.1, 0)  # Explodir a fatia "Com Deficiência"
fig, ax = plt.subplots(figsize=(8, 4))
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
ax.axis('equal')
st.pyplot(fig)




