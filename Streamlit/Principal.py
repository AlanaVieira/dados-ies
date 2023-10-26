import os
import pandas as pd 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly
import plotly.express as px
import streamlit as st


st.set_page_config(page_title='Analise IES', 
                   page_icon=':books:', 
                   layout='centered', 
                   initial_sidebar_state='expanded', 
                   menu_items={
					'About': 'Esta análise utiliza dados de fontes abertas, como IBGE e INEP'})
				   
st.title(':male-student: :female-student: Censo da Educação do Ensino Superior no Brasil :flag-br:')
subtitle = '<p style="font-family:Courier; color:Green; font-size: 20px;">Análise dos dados das Instituições e Cursos de Ensino Superior</p>'
st.markdown(subtitle, unsafe_allow_html=True)				   
st.markdown("---")

# st.sidebar.header("Quais análises você deseja visualizar?")
# analise_interesse = st.sidebar.selectbox('Selecione o seu objeto de interesse:',
                                   # ('Características das Instituições de Ensino Superior', 
								   # 'Características dos Cursos', 
								   # 'Vagas Disponíveis',
								   # 'Evolução das Matrículas',
								   # 'Evolução dos Ingressantes',
								   # 'Evolução dos Concluintes'))
								   







