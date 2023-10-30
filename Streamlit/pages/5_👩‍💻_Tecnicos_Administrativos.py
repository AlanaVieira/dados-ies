import streamlit as st
import datetime
from datetime import datetime
import os

# Analise
import pandas as pd 
import numpy as np 

#Visualization
import matplotlib
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly
import plotly.express as px


st.set_page_config(page_title='Analise TAE', 
                    page_icon=':books:', 
				    layout='wide', 
                    initial_sidebar_state='expanded')

st.title(':chart_with_upwards_trend: Força de trabalho técnico-adminsitrativa em educação :flag-br:')
st.subheader('Escopo: Instituições de cursos Presenciais de Ensino Superior - Públicas e Privadas')
st.subheader("Dados de 2012-2022")
st.markdown("---")
# ------------------------------------------------------------------------
# Parametros plots seaborn
# ------------------------------------------------------------------------
sns.set(style="darkgrid")

# ------------------------------------------------------------------------
# Carrega os dados da força de trabalho das IES
# ------------------------------------------------------------------------
@st.cache_data 
def carregar_dados_taes():
    data = pd.read_csv("../data/dados_ies_taes_docentes_2012_2022.csv", low_memory=False)
    return data
ies = carregar_dados_taes() 

ies['QT_TEC_MASC'] = ies["QT_TEC_FUNDAMENTAL_INCOMP_MASC"] + ies["QT_TEC_FUNDAMENTAL_COMP_MASC"] + ies["QT_TEC_MEDIO_MASC"] + \
    ies["QT_TEC_SUPERIOR_MASC"] + ies["QT_TEC_ESPECIALIZACAO_MASC"] + ies["QT_TEC_MESTRADO_MASC"] + ies["QT_TEC_DOUTORADO_MASC"] 

ies['QT_TEC_FEM'] =  ies["QT_TEC_FUNDAMENTAL_INCOMP_FEM"] + ies["QT_TEC_FUNDAMENTAL_COMP_FEM"]+ ies["QT_TEC_MEDIO_FEM"] + \
    ies["QT_TEC_SUPERIOR_FEM"] + ies["QT_TEC_ESPECIALIZACAO_FEM"] + ies["QT_TEC_MESTRADO_FEM"] + ies["QT_TEC_DOUTORADO_FEM"] 

#-------------------------------------------------------------------------------------------------#
# agrupar o dataframe para gerar o graficos por região e proporção de taes por aluno matriculado
#-------------------------------------------------------------------------------------------------#

df_regiao =  ies.groupby(['NO_REGIAO_IES', 'NU_ANO_CENSO']).agg({'QT_TEC_MASC':'sum', 'QT_TEC_FEM':'sum', 'QT_MAT':'sum'}).reset_index()
df_regiao['RELACAO_MATR_TAES'] = round(( (df_regiao['QT_TEC_MASC']+ df_regiao['QT_TEC_FEM']) / df_regiao['QT_MAT'])*100,2)
df_regiao = df_regiao.sort_values(by=(["NU_ANO_CENSO"]), ascending=False)

#-------------------------------------------------------------------------------------------------#
# agrupar o dataframe para gerar o graficos por categoria e proporção de taes por aluno matriculado
#-------------------------------------------------------------------------------------------------#

df_cat =  ies.groupby(['Tipo_Cat_Admn', 'NU_ANO_CENSO']).agg({'QT_TEC_MASC':'sum', 'QT_TEC_FEM':'sum', 'QT_MAT':'sum'}).reset_index()
df_cat = df_cat[df_cat['QT_MAT']>0]
df_cat['RELACAO_MATR_TAES'] = round(( (df_cat['QT_TEC_MASC']+ df_cat['QT_TEC_FEM']) / df_cat['QT_MAT'])*100,2)
df_cat = df_cat.sort_values(by=(["NU_ANO_CENSO"]), ascending=False)


#--------------------------------------------------------------------------#
# agrupar o dataframe para gerar o graficos por sexo e tipo de instituição
#--------------------------------------------------------------------------#
df_sexo = ies.groupby(['NU_ANO_CENSO', 'TIPO_INST']).agg({'QT_TEC_MASC':'sum','QT_TEC_FEM':'sum'}).reset_index()

df_sexo = df_sexo.rename(columns={'QT_TEC_MASC':'Masculino', 'QT_TEC_FEM':'Feminino'})

df_sexo = df_sexo.pivot(index='NU_ANO_CENSO', columns='TIPO_INST', values=['Masculino','Feminino']).reset_index()
novas_colunas = ['Ano','Privada - Masculino', 'Pública - Masculino', 'Privada - Feminino', 'Pública - Feminino']
df_sexo = df_sexo.set_axis(novas_colunas, axis=1)

df_sexo = df_sexo.melt(id_vars='Ano', value_name='Total', var_name='Tipo/Sexo')
df_sexo = df_sexo.sort_values(by=(["Ano", "Tipo/Sexo"]), ascending=False)

#--------------------------------------------------------------------#
# Filtrar o data set somando as quantidades por escolaridade e sexo
#--------------------------------------------------------------------#
df_escolaridade = ies.groupby(['NO_REGIAO_IES', 'NU_ANO_CENSO', 'TIPO_INST']).agg({'QT_TEC_FUNDAMENTAL_INCOMP_FEM':'sum', 'QT_TEC_FUNDAMENTAL_INCOMP_MASC':'sum',\
                                                                       'QT_TEC_FUNDAMENTAL_COMP_FEM':'sum', 'QT_TEC_FUNDAMENTAL_COMP_MASC':'sum',\
                                                                       'QT_TEC_MEDIO_FEM':'sum', 'QT_TEC_MEDIO_MASC':'sum',\
                                                                       'QT_TEC_SUPERIOR_FEM':'sum', 'QT_TEC_SUPERIOR_MASC':'sum',\
                                                                       'QT_TEC_ESPECIALIZACAO_FEM':'sum', 'QT_TEC_ESPECIALIZACAO_MASC':'sum',\
                                                                       'QT_TEC_MESTRADO_FEM':'sum', 'QT_TEC_MESTRADO_MASC':'sum',\
                                                                       'QT_TEC_DOUTORADO_FEM':'sum', 'QT_TEC_DOUTORADO_MASC':'sum',\
                                                                        'QT_TEC_FEM':'sum', 'QT_TEC_MASC':'sum'}).reset_index()

df_escolaridade['Superior incompleto - Masculino'] = df_escolaridade['QT_TEC_FUNDAMENTAL_INCOMP_MASC'] + df_escolaridade['QT_TEC_FUNDAMENTAL_COMP_MASC']+ df_escolaridade['QT_TEC_MEDIO_MASC']
df_escolaridade['Superior incompleto - Feminino'] = df_escolaridade['QT_TEC_FUNDAMENTAL_INCOMP_FEM'] + df_escolaridade['QT_TEC_FUNDAMENTAL_COMP_FEM']+ df_escolaridade['QT_TEC_MEDIO_FEM']

df_escolaridade['Superior completo - Masculino'] = df_escolaridade['QT_TEC_SUPERIOR_MASC'] 
df_escolaridade['Superior completo - Feminino'] = df_escolaridade['QT_TEC_SUPERIOR_FEM'] 

df_escolaridade['Pós-Graduação - Masculino'] = df_escolaridade['QT_TEC_ESPECIALIZACAO_MASC'] + df_escolaridade['QT_TEC_MESTRADO_MASC']+ df_escolaridade['QT_TEC_DOUTORADO_MASC']
df_escolaridade['Pós-Graduação - Feminino'] = df_escolaridade['QT_TEC_ESPECIALIZACAO_FEM'] + df_escolaridade['QT_TEC_MESTRADO_FEM']+ df_escolaridade['QT_TEC_DOUTORADO_FEM']

df_escolaridade = df_escolaridade.groupby('NU_ANO_CENSO').agg({'Superior incompleto - Masculino':'sum', \
                                                  'Superior incompleto - Feminino':'sum',\
                                                  'Superior completo - Masculino':'sum',\
                                                  'Superior completo - Feminino' :'sum',\
                                                  'Pós-Graduação - Masculino' :'sum',\
                                                  'Pós-Graduação - Feminino':'sum'}).reset_index()

df_escolaridade_melt = df_escolaridade.melt(id_vars='NU_ANO_CENSO', var_name='Escolaridade', value_name='Total').dropna()


col1,col2 = st.columns(2)    
#--------------------------------------------------------------#
# grafico 1 - linhas - proporção do total de taes/alunos matriculados
#--------------------------------------------------------------#
with col1:    
    titulo_plot01 =  '<p style="font-family:Courier; color:Black; font-size: 23px;"><b>Relação Técnico Administrativos por Discentes Matriculados por Região - Evolução</b></p>'
    st.markdown(titulo_plot01, unsafe_allow_html=True)

    fig, ax = plt.subplots(1, 1,  figsize=(22,12))
    ano_min = df_regiao['NU_ANO_CENSO'].min()
    ano_max = df_regiao['NU_ANO_CENSO'].max()

    ax =  sns.pointplot(x="NU_ANO_CENSO", y='RELACAO_MATR_TAES', hue="NO_REGIAO_IES", data=df_regiao,  markers='o')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha="right", fontsize=16)
    ax.set(xlabel=''); 
    ax.set_ylabel('Relação TAEs/Matriculados', fontsize=18)
    ax.tick_params(axis='y', labelsize=14)
    ax.grid(color='gray', linestyle='--', linewidth=1.2, axis='y', alpha=.2)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5,
           fontsize='x-large')

    st.pyplot(fig)

with col2:    
    titulo_plot01 =  '<p style="font-family:Courier; color:Black; font-size: 23px;"><b>Relação Técnico Administrativos por Discentes Matriculados por Categoria - Evolução</b></p>'
    st.markdown(titulo_plot01, unsafe_allow_html=True)

    fig, ax = plt.subplots(1, 1,  figsize=(22,12))
    ano_min = df_cat['NU_ANO_CENSO'].min()
    ano_max = df_cat['NU_ANO_CENSO'].max()

    ax =  sns.pointplot(x="NU_ANO_CENSO", y='RELACAO_MATR_TAES', hue="Tipo_Cat_Admn", data=df_cat,  markers='o')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha="right", fontsize=16)
    ax.set(xlabel=''); 
    ax.set_ylabel('Relação TAEs/Matriculados', fontsize=18)
    ax.tick_params(axis='y', labelsize=14)
    ax.grid(color='gray', linestyle='--', linewidth=1.2, axis='y', alpha=.2)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5,
           fontsize='x-large')

    st.pyplot(fig)

# Cria as colunas
col3,col4 = st.columns(2)    
#--------------------------------------------------------------------------#
#Ajustar os dados para gerar os graficos por sexo e escolaridade
#------------------------------------------------ -------------------------#
with col3:    
    titulo_plot02 =  '<p style="font-family:Courier; color:Black; font-size: 23px;"><b>Técnicos Administrativos por Sexo e Tipo de Instituição - Evolução</b></p>'
    st.markdown(titulo_plot02, unsafe_allow_html=True)
    fig1 = px.bar(df_sexo, y='Total', x='Ano', color='Tipo/Sexo', color_discrete_sequence=px.colors.qualitative.G10,
                    barmode = 'stack', width=800, height=900, labels=dict(Tipo = 'Tipo/Sexo'), text='Total')
    fig1.update_xaxes(tickangle=0)
    fig1.update_traces(textposition='inside', insidetextfont=dict(color='white', size=16,family='Times New Roman'))
    fig1.update_layout( yaxis=dict(title='', titlefont_size=22, tickfont_size=18),
                        xaxis=dict(title='', titlefont_size=22, tickfont_size=18),  
                        legend=dict(x=0.1,y=-0.30, font = dict(size = 18)), 
                       hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"))				     
    st.plotly_chart(fig1, use_container_width=True)	

with col4:      
    titulo_plot03 =  '<p style="font-family:Courier; color:Black; font-size: 23px;"><b>Técnicos Administrativos por Sexo e Escolaridade - Evolução</b></p>'
    st.markdown(titulo_plot03, unsafe_allow_html=True)
    fig3 = px.bar(df_escolaridade_melt, y='Total', x='NU_ANO_CENSO', color='Escolaridade', color_discrete_sequence=px.colors.qualitative.G10,
                    barmode = 'stack', width=800, height=900, labels=dict(Escolaridade = 'Escolaridade'), text='Total')
    fig3.update_xaxes(tickangle=0)
    fig3.update_traces(textposition='inside', insidetextfont=dict(color='white', size=16,family='Times New Roman'))
    fig3.update_layout( yaxis=dict(title='', titlefont_size=22, tickfont_size=18),
                        xaxis=dict(title='', titlefont_size=22, tickfont_size=18),  
                        legend=dict(x=0.1,y=-0.40, font = dict(size = 18)), 
                       hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"))				  
    st.plotly_chart(fig3, use_container_width=True)	
    