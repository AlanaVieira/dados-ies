import os
import pandas as pd 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly
import plotly.express as px
import streamlit as st


st.set_page_config(layout='wide')

st.title(':school: Mapa das Instituições de Ensino Superior')
st.subheader("Dados de 2022")
st.markdown("---")

# ------------------------------------------------------------------------
# Carrega dados IES
# ------------------------------------------------------------------------

colunas_CO = ['CO_REGIAO_IES',  'CO_UF_IES', 'CO_MESORREGIAO_IES', 'CO_MICRORREGIAO_IES',
 'CO_MANTENEDORA', 'CO_IES', 'COD_IBGE', 'IN_CAPITAL_IES', 'NU_CEP_IES']
dict_dtype = {column : 'str'  for column in colunas_CO}
ies = pd.read_csv('./arquivos/dados_ies_consolidado.csv', sep='|', dtype = dict_dtype, low_memory=False)
				 
distr_cat_org_br = ies.groupby(['Tipo_Cat_Admn','Tipo_Org_Acad'])['CO_IES'].count().reset_index()
distr_cat_org_br = distr_cat_org_br.rename(columns={'CO_IES':'Total_IES'})

#st.dataframe(distr_cat_org_br.head(), use_container_width=True, hide_index=True)

# ------------------------------------------------------------------------
# Carrega dados IES agregados por UF
# ------------------------------------------------------------------------

ies_agg_UF = pd.read_csv('./arquivos/dados_ies_agg_UF.csv', sep='|', 
                   low_memory=False)

# renomear colunas para nomes mais intuitivos
ies_agg_UF = ies_agg_UF.rename(columns={'Total_mun':'Total_mun_IES',
                                        'Total_Pop_IES':'Total_Pop_UF_IES',
                                        'Total_Pop_IBGE_2022':'Total_Pop_UF',
                                        'Total_Mun_IBGE_2022':'Total_Mun_UF',
                                        'Total_Meso':'Total_Meso_UF',
                                        'Total_Micro':'Total_Micro_UF',
                                        'Prop_Mun':'Cob_Mun_com_IES',
                                        'Cob_Meso':'Cob_Meso_com_IES',
                                        'Cob_Micro':'Cob_Micro_com_IES'})

# ordenar as colunas
# desconsiderar 'IES_hab'
ies_agg_UF = ies_agg_UF[['SG_UF_IES', 'Total_Pop_UF', 'Total_Mun_UF', 'Total_Meso_UF', 'Total_Micro_UF',
                         'Total_IES', 'Total_Priv', 'Total_Publ','Total_mun_IES', 'Total_Pop_UF_IES',
                         'Total_Meso_IES','Total_Micro_IES',
                         'Cob_Mun_com_IES','Cob_Meso_com_IES','Cob_Micro_com_IES']]

# total de IES no Brasil
total_ies = ies['NO_IES'].count()

# total de IES por Categoria Adm
total_ies_cat_adm = ies['Tipo_Cat_Admn'].value_counts()#.reset_index().rename(columns={'count':'Total'})

# percentual de IES por Categoria Adm
perc_ies_cat_adm = round(total_ies_cat_adm / total_ies * 100,2) 

# consolidar em dataframe
distr_ies_cat_br = pd.DataFrame({'Total_IES'   : total_ies_cat_adm,
                                 'Total_IES_p':  perc_ies_cat_adm}).reset_index()

# total de IES por UF
tot_ies_uf = ies.groupby('SG_UF_IES')['NO_IES'].count()

# total de IES por Org e UF
tot_ies_org_uf = ies.groupby(['SG_UF_IES','Tipo_Org_Acad'])['NO_IES'].count()

# percentual de IES por Tipo e UF
perc_ies_org_uf = round(tot_ies_org_uf / tot_ies_uf *100,2)

# consolidar em dataframe
distr_ies_org_uf = pd.DataFrame({'Total_Org'   : tot_ies_org_uf,
                                 'Total_Org_p': perc_ies_org_uf}).reset_index()
tot_ies_uf = ies.groupby('SG_UF_IES')['NO_IES'].count()

# total de IES por Tipo e UF
tot_ies_tp_uf = ies.groupby(['SG_UF_IES','TIPO_INST'])['NO_IES'].count()

# percentual de IES por Tipo e UF
perc_ies_tp_uf = round(tot_ies_tp_uf / tot_ies_uf *100,2)

# consolidar em dataframe
distr_ies_tp_uf = pd.DataFrame({'Total_IES'   : tot_ies_tp_uf,
                                'Total_IES_p': perc_ies_tp_uf}).reset_index()


#--------------------------------------------------------------------------------------------
# Carrega dados IES agregados por Região
#------------------------------------------------------------------------------------------

ies_agg_regiao = pd.read_csv('./arquivos/dados_IES_agg_Regiao.csv', sep='|', 
                   low_memory=False)

ies_agg_regiao = ies_agg_regiao.rename(columns={'Total_mun':'Total_mun_IES',
                                        'Total_Pop_IES':'Total_Pop_UF_IES',
                                        'Total_Pop_IBGE_2022':'Total_Pop_UF',
                                        'Total_Mun_IBGE_2022':'Total_Mun_UF',
                                        'Total_Meso':'Total_Meso_UF',
                                        'Total_Micro':'Total_Micro_UF',
                                        'Prop_Mun':'Cob_Mun_com_IES',
                                        'Cob_Meso':'Cob_Meso_com_IES',
                                        'Cob_Micro':'Cob_Micro_com_IES'})

# ordenar as colunas
# desconsiderar 'IES_hab'
ies_agg_regiao = ies_agg_regiao[['REGIAO', 'NOME_REGIAO', 'Total_Pop_UF', 'Total_Mun_UF', 'Total_Meso_UF', 'Total_Micro_UF',
                         'Total_IES', 'Total_Priv', 'Total_Publ','Total_mun_IES', 'Total_Pop_UF_IES',
                         'Total_Meso_IES','Total_Micro_IES',
                         ]]

tot_ies_regiao = ies.groupby('NO_REGIAO_IES')['NO_IES'].count()

# total de IES por Org e Regiao
tot_ies_org_regiao = ies.groupby(['NO_REGIAO_IES','Tipo_Org_Acad'])['NO_IES'].count()

# percentual de IES por Tipo e Regiao
perc_ies_org_regiao = round(tot_ies_org_regiao / tot_ies_regiao *100,2)

# consolidar em dataframe
distr_ies_org_regiao = pd.DataFrame({'Total_Org'   : tot_ies_org_regiao,
                                 'Total_Org_p': perc_ies_org_regiao}).reset_index()

# total de IES por Região
tot_ies_regiao = ies.groupby('NO_REGIAO_IES')['NO_IES'].count()

# total de IES por Tipo e Regiao
tot_ies_tp_regiao = ies.groupby(['NO_REGIAO_IES','TIPO_INST'])['NO_IES'].count()

# percentual de IES por Tipo e regiao
perc_ies_tp_regiao = round(tot_ies_tp_regiao / tot_ies_regiao *100,2)

# consolidar em dataframe
distr_ies_tp_regiao = pd.DataFrame({'Total_IES'   : tot_ies_tp_regiao,
                                'Total_IES_p': perc_ies_tp_regiao}).reset_index()


# -----------------------------------------------------------------------------------
# Plot 01:  Distribuição IES no Brasil - 2022
# -----------------------------------------------------------------------------------

titulo_plot01 = '<p style="font-family:Courier; color:blue; font-size: 25px;"><b>Distribuição IES no Brasil</b></p>'
st.markdown(titulo_plot01, unsafe_allow_html=True)

fig = px.bar(ies_agg_UF.sort_values(by='Total_IES', ascending=False),
             x='SG_UF_IES', 
             y='Total_IES', 
             color='Total_IES',
             color_continuous_scale='viridis_r',
             width=1100, height=600,
             #title='Distribuição IES no Brasil - 2022')
            )

# inserir titulo 
fig.update_layout(title={'text': "", 'y':0.90, 'x':0.5},
                  yaxis=dict(title='Total IES', titlefont_size=20, tickfont_size=12),
                  xaxis=dict(title=''),
                  coloraxis_showscale=False)

# rotacionar valores no eixo x
fig.update_xaxes(tickangle = -45)

#fig.show()

st.plotly_chart(fig, use_container_width=True)


st.markdown("---")

#--------------------------------------------------------------------------------------
# Plot 02 - Número de Instituições de Ensino Superior por região do Brasil
#--------------------------------------------------------------------------------------

titulo_plot02 = '<p style="font-family:Courier; color:Blue; font-size: 25px;"><b>Número de Instituições de Ensino Superior por região do Brasil</b></p>'
st.markdown(titulo_plot02, unsafe_allow_html=True)


fig = px.bar(ies_agg_regiao.sort_values(by='Total_IES', ascending=False),
             x='NOME_REGIAO', 
             y='Total_IES', 
             color='Total_IES',
             color_continuous_scale='viridis_r',
             width=1100, height=600)
             #title='Distribuição IES no Brasil - 2022')

# inserir titulo 
fig.update_layout(title={'text': "", 'y':0.90, 'x':0.5},
                  yaxis=dict(title='Total IES', titlefont_size=20, tickfont_size=12),
                  xaxis=dict(title=''),
                  coloraxis_showscale=False)

# rotacionar valores no eixo x
fig.update_xaxes(tickangle = -45)

st.plotly_chart(fig, use_container_width=True)
#fig.show()


st.caption('As IES estão presentes em todos os estados do território nacional, em maior número nos estados da região sudeste do país (1.098 IES, 42,31%), condizente com a proporção populacional da região que é de aproximadamente 40 % da população total do país.')


st.markdown("---")

# ------------------------------------------------------------------------
# Plot 03: Distribuição das IES por Org Acadêmica e Cat Administrativa 
# ------------------------------------------------------------------------

#st.title('Total IES por  Organização Acadêmica e Categoria Administrativa - Brasil')
#st.header('Total IES por  Organização Acadêmica e Categoria Administrativa - Brasil')
#st.caption('Total IES por  Organização Acadêmica e Categoria Administrativa - Brasil')

# Incluir titulos aqui
titulo_plot03 = '<p style="font-family:Courier; color:Blue; font-size: 25px;"><b>Número de IES por  Organização Acadêmica e Categoria Administrativa - Brasil</b></p>'
st.markdown(titulo_plot03, unsafe_allow_html=True)


fig = px.bar(distr_cat_org_br,
             y='Tipo_Cat_Admn', 
             x='Total_IES', 
             color='Tipo_Org_Acad',
             color_discrete_sequence=px.colors.sequential.Viridis_r,
             #px.colors.qualitative.Pastel1,
             barmode = 'stack', width=1100, height=700,
             # lembrar de ocultar titulos
			 #title='Total IES por  Organização Acadêmica e Categoria Administrativa - Brasil',
             labels=dict(Tipo_Org_Acad = 'Organização Acadêmica')
             #hover_data = {''}
             )

fig.update_layout(yaxis=dict(title='', titlefont_size=20, tickfont_size=12),
                  xaxis=dict(title=''),      # remover titulo no eixo x
                  legend=dict(x=0.1,y=-0.4, font = dict(size = 15))) # deslocar legenda para dentro do plot

fig.update_xaxes(tickangle=0)

#fig.show() # ocultar

st.plotly_chart(fig, use_container_width=True) # precisa incluir

# plot do Matplotlib
# st.pyplot(fig)

st.caption('Observa-se a predominância de organizações privadas no país, tendo as públicas 11% do total de IES. Das 2.595 Instituições de Ensino Superior (IES) do Brasil, há uma predominância de Faculdades (75,84%) e Centros Universitários (14,68%), totalizando 2.349 IES, ou seja, 90,52% do total de instituições no país. Ainda que dentre essas organizações estejam algumas públicas, o resultado é condizente com o encontrado na distribuição das IES por categoria administrativa, em que as instituições privadas (com e sem fim lucrativo) ocupam a proporção de 87,98% do total de IES no Brasil.')


st.markdown("---")

# -----------------------------------------------------------------------------------
# Plot 04:  Proporção de IES por Tipo de Organização Acadêmica - 2022
# -----------------------------------------------------------------------------------

titulo_plot04 = '<p style="font-family:Courier; color:Blue; font-size: 25px;"><b>Proporção de IES por tipo de Organização Acadêmica nas unidades da federação - 2022</b></p>'
st.markdown(titulo_plot04, unsafe_allow_html=True)

fig = px.bar(distr_ies_org_uf.sort_values(by='Total_Org_p', ascending=False),
             x='SG_UF_IES', 
             y='Total_Org_p', 
             color='Tipo_Org_Acad',
             color_discrete_sequence=px.colors.qualitative.Dark2,
             barmode = 'group', width=1000, height=600,
             #title='Distribuição IES no Brasil por UF e Tipo Organização Acadêmica - 2022',
             #hover_data = {'SG_UF_IES','Tipo_Org_Acad','Total_Org',
                          # 'Total_Org_p'}
             
            )

fig.update_layout(yaxis=dict(title='%', titlefont_size=20, tickfont_size=12),
                 xaxis=dict(title=''),      # remover titulo no eixo x
                # legend=dict(x=0.25,y=0.9)) # deslocar legenda para dentro do plot
                 legend=dict(x=0.4,y=-0.5, font = dict(size = 15)))

#fig.show()

st.plotly_chart(fig, use_container_width=True)
             
st.caption('A distribuição das IES nos estados, por tipo de organização, segue o mesmo padrão encontrado nos dados agrupados em nível nacional, com predominância significativa de instituições do tipo faculdade. Contudo, essa proporção tem variação entre os estados: enquanto a maioria dos estados possuem majoritariamente faculdades e centros universitários; os estados de Roraima, Rio Grande do Sul, Mato Grosso do Sul e Amapá destacam-se por possuir universidades como o segundOtipo de IES mais prevalente.')  


st.markdown("---")

# -----------------------------------------------------------------------------------
# Plot 05:  Proporção de IES, por tipo de Organização Acadêmica, nas regiões do país. 
# -----------------------------------------------------------------------------------             
             
titulo_plot05 = '<p style="font-family:Courier; color:Blue; font-size: 25px;"><b>Proporção de IES, por tipo de Organização Acadêmica, nas regiões do país.</b></p>'
st.markdown(titulo_plot05, unsafe_allow_html=True)
    
    
    
fig = px.bar(distr_ies_org_regiao.sort_values(by='Total_Org_p', ascending=False),
             x='NO_REGIAO_IES', 
             y='Total_Org_p', 
             color='Tipo_Org_Acad',
             color_discrete_sequence=px.colors.qualitative.Dark2,
             barmode = 'group', width=1000, height=600,
             #title='Distribuição IES no Brasil por Região e Tipo Organização Acadêmica - 2022',
             #hover_data = {'NO_REGIAO_IES','Tipo_Org_Acad','Total_Org',
                           #'Total_Org_p'}
             )

fig.update_layout(yaxis=dict(title='%', titlefont_size=20, tickfont_size=12),
                  xaxis=dict(title=''),      # remover titulo no eixo x
                  legend=dict(x=0.25,y=0.9)) # deslocar legenda para dentro do plot

st.plotly_chart(fig, use_container_width=True)


st.caption('Quando analisa-se a distribuição das IES pelas regiões do país, em função do tipo de organização acadêmica, é possível observar que a maior prevalência de faculdades e centros universitários está presente em todas as regiões. Quando estratifica-se a análise retirando as faculdades, pode-se observar que a região sul possui, entre os tipos, a maior proporção de universidades que as demais regiões do país. Ainda assim, em todas as regiões a ordem proporcional é sempre a mesma: faculdades, centro-universitários, universidades, Institutos Federais e Cefet.')


st.markdown("---")


# -----------------------------------------------------------------------------------
# Plot 06: Número de IES por tipo de categoria administrativa, por Unidade da Federação  
# -----------------------------------------------------------------------------------   

titulo_plot06 = '<p style="font-family:Courier; color:Blue; font-size: 25px;"><b>Número de IES por tipo de categoria administrativa, por Unidade da Federação</b></p>'
st.markdown(titulo_plot06, unsafe_allow_html=True)

fig = px.bar(distr_ies_tp_uf.sort_values(by='Total_IES', ascending=False),
             x='SG_UF_IES', 
             y='Total_IES', 
             color='TIPO_INST',
             color_discrete_sequence=px.colors.qualitative.Dark2,
             barmode = 'group', width=1000, height=600,
             #title='Distribuição IES no Brasil por UF e Categoria Administrativa - 2022',
             #hover_data = {'SG_UF_IES','TIPO_INST','Total_IES',
                           #'Total_IES_p'}
             )

fig.update_layout(yaxis=dict(title='Total IES', titlefont_size=20, tickfont_size=12),
                  xaxis=dict(title=''),      # remover titulo no eixo x
                  legend=dict(x=0.25,y=0.9)) # deslocar legenda para dentro do plot



st.plotly_chart(fig, use_container_width=True)


st.caption('Em nível nacional, as instituições privadas (com e sem fins lucrativos) ocupam a proporção de 87,98% do total de IES no Brasil. Pode-se observar um cenário aproximado com predominância de instituições privadas quando analisado por UF, destacando-se o estado de MT com a maior proporção de instituições privadas (94,44%) e Roraima com a menor proporção (66.67%).')


st.markdown("---")


# -----------------------------------------------------------------------------------
# Plot 07:  Proporção de IES por tipo de Categoria Administrativa, por Unidade da Federação 
# -----------------------------------------------------------------------------------   

titulo_plot07 = '<p style="font-family:Courier; color:Blue; font-size: 25px;"><b> Proporção de IES por tipo de Categoria Administrativa, por Unidade da Federação</b></p>'
st.markdown(titulo_plot07, unsafe_allow_html=True)

fig = px.bar(distr_ies_tp_uf.sort_values(by='Total_IES_p', ascending=False),
             x='SG_UF_IES', 
             y='Total_IES_p', 
             color='TIPO_INST',
             color_discrete_sequence=px.colors.qualitative.Dark2,
             barmode = 'stack', width=1000, height=600,
             #title='Distribuição proporcional de IES no Brasil por UF e Categoria Administrativa - 2022',
             #hover_data = {'SG_UF_IES','TIPO_INST','Total_IES',
                          # 'Total_IES_p'}
             
            )

fig.update_layout(yaxis=dict(title='%', titlefont_size=20, tickfont_size=12),
                  xaxis=dict(title=''),      # remover titulo no eixo x
                  legend=dict(x=0.25,y=0.9)) # deslocar legenda para dentro do plot



st.plotly_chart(fig, use_container_width=True)


st.caption('Observa-se que a proporção entre IES público e privadas em cada estado possui um variação, como por exemplo, as IES públicas que tem uma prevalência entre 5,56%  em MT e 33,33% em RR. Ainda assim, é possível identificar que na maioria dos estados (67%) a proporção de IES públicas não chega a 10%. ')


st.markdown("---")



# -----------------------------------------------------------------------------------
# Plot 08:  Número de IES por tipo de categoria administrativa, por Região do país 
# -----------------------------------------------------------------------------------   

titulo_plot08 = '<p style="font-family:Courier; color:Blue; font-size: 25px;"><b>Número de IES por tipo de categoria administrativa, por Região do país .</b></p>'
st.markdown(titulo_plot08, unsafe_allow_html=True)

fig1 = px.bar(distr_ies_tp_regiao.sort_values(by='Total_IES', ascending=False),
             x='NO_REGIAO_IES', 
             y='Total_IES', 
             color='TIPO_INST',
             color_discrete_sequence=px.colors.qualitative.Dark2,
             barmode = 'group', width=1000, height=600,
             #title='Distribuição IES no Brasil por Regiao e Categoria Administrativa - 2022',
             #hover_data = {'NO_REGIAO_IES','TIPO_INST','Total_IES',
                          # 'Total_IES_p'}
             
            )

fig1.update_layout(yaxis=dict(title='Total IES', titlefont_size=20, tickfont_size=12),
                  xaxis=dict(title=''),      # remover titulo no eixo x
                  legend=dict(x=0.25,y=0.9)) # deslocar legenda para dentro do plot



st.plotly_chart(fig1, use_container_width=True)



st.caption(' Em números absolutos, quando analisado por categoria administrativa, o que se observa é o mesmo comportamento da distribuição geral das IES nas regiões do país. Uma hierarquização em que a região Sudeste apresenta o maior número de instuições, tanto públicas quanto privadas, seguido das regiões Nordeste, Sul, Centro-Oeste e Norte. Mas números absolutos podem enganar. O gráfico a seguir, com as mesmas informações do ponto de vista proporcional em cada região, demonstra que o Sudeste passa a ser a região com a menor proporção de IES privadas e, consequentemente, a maior proporção de IES públicas. Ou seja, ainda que em termos absolutos a região apresente o maior número de IES privadas do país, também é a região com a menor proporção. Isso provavelmente se explica pelos estados do RJ e SP, que possuem uma proporção de IES públicas mais alta do que a maioria dos estados.')


#st.markdown("---")


# -----------------------------------------------------------------------------------
# Plot 09:  Proporção de IES por tipo de Categoria Administrativa, por Unidade da Federação  
# -----------------------------------------------------------------------------------   

titulo_plot09 = '<p style="font-family:Courier; color:Blue; font-size: 25px;"><b>Proporção de IES por tipo de Categoria Administrativa, por Unidade da Federação.</b></p>'
st.markdown(titulo_plot09, unsafe_allow_html=True)

fig2 = px.bar(distr_ies_tp_regiao.sort_values(by='Total_IES_p', ascending=False),
             x='NO_REGIAO_IES', 
             y='Total_IES_p', 
             color='TIPO_INST',
             color_discrete_sequence=px.colors.qualitative.Dark2,
             barmode = 'group', width=1000, height=600,
             #title='Distribuição IES no Brasil por Regiao e Categoria Administrativa - 2022',
             #hover_data = {'NO_REGIAO_IES','TIPO_INST','Total_IES',
               #            'Total_IES_p'}
             
            )

fig2.update_layout(yaxis=dict(title='%', titlefont_size=20, tickfont_size=12),
                  xaxis=dict(title=''),      # remover titulo no eixo x
                  legend=dict(x=0.25,y=0.9)) # deslocar legenda para dentro do plot

st.plotly_chart(fig2, use_container_width=True)


st.caption('Com as mesmas informações do ponto de vista proporcional em cada região, este gráfico demonstra que o Sudeste passa a ser a região com a menor proporção de IES privadas e, consequentemente, a maior proporção de IES públicas. Ou seja, ainda que em termos absolutos a região apresente o maior número de IES privadas do país, também é a região com a menor proporção. Isso provavelmente se explica pelos estados do RJ e SP, que possuem uma proporção de IES públicas mais alta do que a maioria dos estados.')

st.markdown("---")

# Colocando os títulos dos gráficos em colunas

col1, col2 = st.columns(2)

with col1:
        st.subheader('Número de IES por tipo de categoria administrativa, por Região do país.')
      #  st.write("Gráfico 1")

with col2:
        st.subheader('Proporção de IES por tipo de Categoria Administrativa, por Unidade da Federação.')
       # st.write("Gráfico 2")

#Colocando os gráficos 8 e 9 em colunas

col1, col2 = st.columns(2)

# Adicione os gráficos às colunas

col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig2, use_container_width=True)

# Colocando as legendas dos gráficos em colunas

col1, col2 = st.columns(2)

with col1:
        st.caption(' Em números absolutos, quando analisado por categoria administrativa, o que se observa é o mesmo comportamento da distribuição geral das IES nas regiões do país. Uma hierarquização em que a região Sudeste apresenta o maior número de instuições, tanto públicas quanto privadas, seguido das regiões Nordeste, Sul, Centro-Oeste e Norte. Mas números absolutos podem enganar.')
      #  st.write("Gráfico 1")

with col2:
        st.caption('Com as mesmas informações do ponto de vista proporcional em cada região, este gráfico demonstra que o Sudeste passa a ser a região com a menor proporção de IES privadas e, consequentemente, a maior proporção de IES públicas. Ou seja, ainda que em termos absolutos a região apresente o maior número de IES privadas do país, também é a região com a menor proporção. Isso provavelmente se explica pelos estados do RJ e SP, que possuem uma proporção de IES públicas mais alta do que a maioria dos estados.')
       # st.write("Gráfico 2"