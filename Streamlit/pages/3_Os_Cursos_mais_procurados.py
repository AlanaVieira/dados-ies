import os
import pandas as pd 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly
import plotly.express as px
import streamlit as st

st.title(':books: Oferta de Cursos :flag-br:')
st.subheader("Dados de 2022")

st.markdown("---")


#subtitle = '<p style="font-family:Courier; color:Green; font-size: 20px;">Distribuição </p>'
#st.markdown(subtitle, unsafe_allow_html=True)	


# ------------------------------------------------------------------------
# Carga dos Dados
# ------------------------------------------------------------------------
colunas_CO = ['CO_REGIAO', 'CO_UF', 'CO_MUNICIPIO', 'CO_IES', 'CO_CURSO', 'CO_CINE_ROTULO', 'CO_CINE_AREA_GERAL',
 'CO_CINE_AREA_ESPECIFICA', 'CO_CINE_AREA_DETALHADA', 'IN_CAPITAL', 'IN_GRATUITO']
 
dict_dtype = {column : 'str'  for column in colunas_CO}
cursos = pd.read_csv('./dados/dados_cursos_escopo_consolidado_2022.csv', sep='|', 
                  dtype = dict_dtype, 
                  low_memory=False)

tot_cursos = cursos.shape[0]
tot_cursos_br = cursos.groupby(['NO_CURSO'])['QT_CURSO'].count()
perc_cursos_br = round((tot_cursos_br / tot_cursos * 100),2)

distr_cursos_br = pd.DataFrame({'Total_Cursos' : tot_cursos_br,
                                'Total_Cursos_p_BR': perc_cursos_br}).reset_index()

top10_BR = distr_cursos_br.sort_values(by='Total_Cursos', ascending=False).head(10)
top10_BR['Perc_top10'] = top10_BR['Total_Cursos'] / (top10_BR['Total_Cursos'].sum()) * 100

st.write('Total de todos os cursos: ', tot_cursos)
st.write('Total de cursos considerando-se a lista dos top 10:', top10_BR['Total_Cursos'].sum())


# ------------------------------------------------------------------------
# Exibir dataframe
# ------------------------------------------------------------------------

display_df = top10_BR.copy()
display_df = display_df.rename(columns={'NO_CURSO':'Nome do Curso', 
                                     'Total_Curso':'Oferta', 
                                     'Total_Cursos_p_BR':'Oferta (% em relação ao Total)',
                                     'Perc_top10': 'Oferta (% em relação aos Top10)'})  
                                    
st.dataframe(display_df, hide_index=True, use_container_width=True)   

st.markdown("---")
  
# ------------------------------------------------------------------------
# Plot01 - Top 10 cursos mais oferecidos no Brasil
# ------------------------------------------------------------------------
fig = plt.figure(figsize =(10, 6))

labels = top10_BR['NO_CURSO'].values
data = top10_BR['Total_Cursos'].values

fracs = top10_BR['Perc_top10'].values
total = sum(fracs)
explode = (0.25, 0.20, 0.15, 0.15, 0.15, 0.15, 0.1, 0, 0.1, 0.15)

plt.title("Top 10 cursos mais oferecidos no Brasil", fontsize=16, loc = 'center', color='b')
st.write("##")

plt.pie(fracs, 
        explode=explode, 
        labels=labels,
        autopct=lambda p: '{:.0f}%'.format(p * total / 100),
        shadow=True, 
        startangle=90)

st.pyplot(fig)

st.markdown("---")

# ------------------------------------------------------------------------
# Plot02 - Top 5 cursos mais oferecidos em cada UF
# ------------------------------------------------------------------------
no_cursos_uf = cursos.groupby(['SG_UF','NO_CURSO'])['QT_CURSO'].count().reset_index().rename(columns={'QT_CURSO':'Total'})
top5 = no_cursos_uf.sort_values(['SG_UF','Total'], ascending=[True, False]).groupby('SG_UF').head(5)

fig = px.bar(top5.sort_values(by='Total', ascending=False),
             x='SG_UF', 
             y='Total', 
             color='NO_CURSO',
             #color_discrete_sequence=px.colors.qualitative.Vivid, #Dark2
             #color_discrete_sequence= px.colors.sequential.Plasma_r,
             color_discrete_sequence= px.colors.diverging.Fall,
             barmode = 'stack', #stack=empilhado; group=barras separadas
             width=1000, height=800,
             title='Top 5 Cursos Presenciais (em quantidade) por UF',
             hover_data = {'NO_CURSO','Total'})

fig.update_layout(yaxis=dict(title='Total Cursos', titlefont_size=30, tickfont_size=12),
                  xaxis=dict(title=''),      # remover titulo no eixo x
                  legend=dict(x=0.6,y=0.9)) # deslocar legenda para dentro do plot


st.plotly_chart(fig, use_container_width=True)

