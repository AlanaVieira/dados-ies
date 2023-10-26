import os
import pandas as pd 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly
import plotly.express as px
import streamlit as st

st.title(':classical_building: Mapa das Instituições de Ensino Superior :flag-br:')
st.subheader("Dados de 2022")
st.markdown("---")

#subtitle = '<p style="font-family:Courier; color:Green; font-size: 18px;"> </p>'
#st.markdown(subtitle, unsafe_allow_html=True)				   


# ------------------------------------------------------------------------
# Carrega dados IES
# ------------------------------------------------------------------------
colunas_CO = ['CO_REGIAO_IES',  'CO_UF_IES', 'CO_MESORREGIAO_IES', 'CO_MICRORREGIAO_IES',
 'CO_MANTENEDORA', 'CO_IES', 'COD_IBGE', 'IN_CAPITAL_IES', 'NU_CEP_IES']
dict_dtype = {column : 'str'  for column in colunas_CO}
ies = pd.read_csv('./dados/dados_ies_consolidado.csv', sep='|', 
                  dtype = dict_dtype, low_memory=False)
				 
distr_cat_org_br = ies.groupby(['Tipo_Cat_Admn','Tipo_Org_Acad'])['CO_IES'].count().reset_index()
distr_cat_org_br = distr_cat_org_br.rename(columns={'CO_IES':'Total_IES'})

# ------------------------------------------------------------------------
# Plot01 - Distribuição das IES por Organização Acadêmica e Categoria Administrativa
# ------------------------------------------------------------------------
fig = px.bar(distr_cat_org_br, y='Tipo_Cat_Admn', x='Total_IES', color='Tipo_Org_Acad',
    color_discrete_sequence=px.colors.sequential.Viridis_r,
    barmode = 'stack', width=1100, height=700,
    title='Distribuição das IES por Categoria Administrativa e Organização Acadêmica - Brasil',
    labels=dict(Tipo_Org_Acad = 'Organização Acadêmica'))

fig.update_layout(yaxis=dict(title='', titlefont_size=20, tickfont_size=12),
    xaxis=dict(title=''),      
    legend=dict(x=0.1,y=-0.4)) 
    
fig.update_xaxes(tickangle=0)
st.plotly_chart(fig, use_container_width=True)

 
