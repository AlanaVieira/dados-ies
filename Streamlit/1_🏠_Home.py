import pandas as pd
import streamlit as st
#import altair as alt
from streamlit_option_menu import option_menu
from PIL import Image
import plotly.express as px
#from numerize.numerize import numerize
import os
#import requests
#import pickle



#@st.cache

########## CONFIGURAÇÃO DA PÁGINA########
st.set_page_config(
    page_title='DASHBOARD ANÁLISE DOS DADOS DAS INSTITUIÇÕES DE ENSINO SUPERIOR DO BRASIL',
    page_icon='📊',
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'http://www.meusite.com.br',
        'Report a bug': "http://www.meuoutrosite.com.br",
        'About': "Esse app foi desenvolvido no curso ENAP ."
    }
)
####### --- Criar o dataframe########################

#df = pd.read_csv('./arquivos/MICRODADOS_ED_SUP_IES_2022.CSV', encoding='latin-1', sep=';')
#df_ies = pd.read_csv('./arquivos/dados_cursos_escopo_consolidado.csv', encoding='utf-8', sep='|')

header_left, header_mid, header_right = st.columns([1, 3, 1], gap="large")
##############################################################################
#######LOGO INICIAL#################
logo = Image.open('./Midia/logo.png')
st.image(logo, width=800)
st.markdown('---')

#######################################LOAD HTML ##############################################
###########PLOTE MAPA HTML
with st.container():
    st.write("Apresentamos o dashboard da Análise das Instituições de Ensino Superior do Brasil que está dividido em quatro seções. Cada uma seção apresenta os nossos resultados encontrados nas análises realizadas sobre: Instituições, Docentes, Discentes e Técnicos Administrativos. Na seção 'Projeto', detalhamos o processo de desenvolvimento deste projeto. Em 'Quem Somos', vocês encontrarão informações de contato sobre o nosso grupo.")
    
    st.markdown('---')

    st.subheader('Mapa da Distribuição de Instituições de Ensino Públicas e Privadas nos Estados do Brasil: Uma Análise Comparativa')
   
###############################################################################################
    # Carrega o arquivo HTML
    with open('.\data\ies_interativo.html', 'r', encoding='utf-8') as file:
        html_code = file.read()

    # Exibe o conteúdo HTML
    st.components.v1.html(html_code, height=800, scrolling=True)


 #######################################################################################################

