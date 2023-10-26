import os
import pandas as pd 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly
import plotly.express as px
import streamlit as st

st.title(':classical_building: Mapa das Instituições de Ensino Superior - UFs :cityscape:')
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
# Plot01 - Contagem de IES em cada Estado
# ------------------------------------------------------------------------
ies_agg_UF = pd.read_csv('./dados/dados_IES_agg_UF.csv', sep='|', low_memory=False)
ies_agg_UF = ies_agg_UF.rename(columns={'Total_mun':'Total_mun_IES',
                                        'Total_Pop_IES':'Total_Pop_UF_IES',
                                        'Total_Pop_IBGE_2022':'Total_Pop_UF',
                                        'Total_Mun_IBGE_2022':'Total_Mun_UF',
                                        'Total_Meso':'Total_Meso_UF',
                                        'Total_Micro':'Total_Micro_UF',
                                        'Prop_Mun':'Cob_Mun_com_IES',
                                        'Cob_Meso':'Cob_Meso_com_IES',
                                        'Cob_Micro':'Cob_Micro_com_IES'})

ies_agg_UF = ies_agg_UF[['SG_UF_IES', 'Total_Pop_UF', 'Total_Mun_UF', 'Total_Meso_UF', 'Total_Micro_UF',
                         'Total_IES', 'Total_Priv', 'Total_Publ','Total_mun_IES', 'Total_Pop_UF_IES',
                         'Total_Meso_IES','Total_Micro_IES',
                         'Cob_Mun_com_IES','Cob_Meso_com_IES','Cob_Micro_com_IES']]

fig = px.bar(ies_agg_UF.sort_values(by='Total_IES', ascending=False),
             x='SG_UF_IES', 
             y='Total_IES', 
             color='Total_IES',
             color_continuous_scale='viridis_r',
             width=1100, height=600,
             title='Distribuição IES no Brasil - 2022')

fig.update_layout(title={'text': 'Quantidade total de IES em cada Estado', 'y':0.90, 'x':0.5},
                  yaxis=dict(title='Total IES', titlefont_size=20, tickfont_size=12),
                  xaxis=dict(title=''),
                  coloraxis_showscale=False)

fig.update_xaxes(tickangle = -45)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ------------------------------------------------------------------------
# Plot02 - Distribuição das IES por Categoria Administrativa
# ------------------------------------------------------------------------
tot_ies_uf = ies.groupby('SG_UF_IES')['NO_IES'].count()
tot_ies_tp_uf = ies.groupby(['SG_UF_IES','TIPO_INST'])['NO_IES'].count()
perc_ies_tp_uf = round(tot_ies_tp_uf / tot_ies_uf *100,2)
distr_ies_tp_uf = pd.DataFrame({'Total_IES'   : tot_ies_tp_uf,
                                'Total_IES_p': perc_ies_tp_uf}).reset_index()
fig = px.bar(distr_ies_tp_uf.sort_values(by='Total_IES_p', ascending=False),
             x='SG_UF_IES', 
             y='Total_IES_p', 
             color='TIPO_INST',
             color_discrete_sequence=px.colors.qualitative.Dark2,
             barmode = 'overlay', width=1000, height=600,
             title='Distribuição proporcional de IES por Categoria Administrativa',
             hover_data = {'SG_UF_IES','TIPO_INST','Total_IES',
                           'Total_IES_p'})

fig.update_layout(yaxis=dict(title='% Percentual', titlefont_size=20, tickfont_size=12),
                  xaxis=dict(title=''),      
                  legend=dict(x=0.25,y=-0.2)) 
st.plotly_chart(fig, use_container_width=True)                  

st.markdown("---")

# ------------------------------------------------------------------------
# Plot03 - Distribuição das IES por Organização Acadêmica 
# ------------------------------------------------------------------------
tot_ies_uf = ies.groupby('SG_UF_IES')['NO_IES'].count()
tot_ies_org_uf = ies.groupby(['SG_UF_IES','Tipo_Org_Acad'])['NO_IES'].count()
perc_ies_org_uf = round(tot_ies_org_uf / tot_ies_uf *100,2)

distr_ies_org_uf = pd.DataFrame({'Total_Org'   : tot_ies_org_uf,
                                 'Total_Org_p': perc_ies_org_uf}).reset_index()

fig = px.bar(distr_ies_org_uf.sort_values(by='Total_Org_p', ascending=False),
             x='SG_UF_IES', 
             y='Total_Org_p', 
             color='Tipo_Org_Acad',
             color_discrete_sequence=px.colors.qualitative.Dark2,
             barmode = 'overlay', width=1000, height=700,
             title='Distribuição proporcional de IES por Organização Acadêmica',
             hover_data = {'SG_UF_IES','Tipo_Org_Acad','Total_Org',
                           'Total_Org_p'})

fig.update_layout(yaxis=dict(title='Proporção de organizações', titlefont_size=20, tickfont_size=12),
                  xaxis=dict(title=''),      
                  legend=dict(x=0.25,y=-0.5)) 

st.plotly_chart(fig, use_container_width=True)


st.markdown("---")

# ------------------------------------------------------------------------
# Plot04 - Distribuição das IES - Comparativo com População e Cobertura de Mun 
# ------------------------------------------------------------------------
st.caption('O gráfico abaixo disponibiliza a informação de cobertura dos Municípios contemplados com a existência de IES.')

fig = plt.figure(figsize=(20, 15))
axes = fig.add_subplot(111)

cores = sns.color_palette("mako", 27) # magma
interval_x = np.arange(0,625,25) # intervalo eixos população
interval_y = np.arange(0,60000000,5000000) # intervalo eixos população

g = sns.barplot(x='SG_UF_IES', 
                y='Total_IES', 
                data=ies_agg_UF.sort_values(by='Total_IES', ascending=False),
                palette = cores, 
                label='Total_IES')

axes.set_title('Distribuição IES no Brasil - Cobertura de Municipios', fontsize=35)
axes.set_ylabel('Total IES', fontsize=20)
axes.yaxis.set_ticks(interval_x)
axes.set(xlabel='') 

ax2 = axes.twinx()
ax2.plot(ies_agg_UF.sort_values(by='Total_IES', ascending=False)['SG_UF_IES'], 
         ies_agg_UF.sort_values(by='Total_IES', ascending=False)['Total_Pop_UF_IES'],
        color='#ffff00', label='Total_Pop_IES')
ax2.set_ylabel("População dos municipios com IES", fontsize=20)

ax3 = axes.twinx()
ax3.plot(ies_agg_UF.sort_values(by='Total_IES', ascending=False)['SG_UF_IES'], 
         ies_agg_UF.sort_values(by='Total_IES', ascending=False)['Total_Pop_UF'],
        color='#ff8000', label='Total_Pop_IBGE')
#ax3.set_ylabel("População total da UF")

axes.grid(visible=False)

ax2.grid(visible=True, linestyle = "dashed", color='white')
ax2.yaxis.set_ticks(interval_y)
#ax2.yaxis.set_visible(False) # remove yticks

ax3.grid(visible=False)
ax3.yaxis.set_ticks(interval_y)
ax3.yaxis.set_visible(True) # remove yticks

lines1, labels1 = axes.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax3.legend(lines1 + lines2 + lines3, labels1 + labels2 + labels3, loc="upper center", fontsize=18)

valores_prop_mun =  ies_agg_UF.sort_values(by='Total_IES', ascending=False)['Cob_Mun_com_IES'].values
for i, p in enumerate(axes.patches):
        axes.annotate('{:,.0f}%'.format(valores_prop_mun[i]), 
                      (p.get_x()+0.1, p.get_height()+10) , 
                     fontsize=16, weight='bold', color='#730099')
st.pyplot(fig)

st.markdown("---")

# ------------------------------------------------------------------------
# Plot05 - Distribuição das IES - Comparativo com População e Cobertura de Regioes 
# ------------------------------------------------------------------------
colunas_int = ['SG_UF_IES','Total_IES', 'Cob_Mun_com_IES','Cob_Meso_com_IES','Cob_Micro_com_IES']
df_coberturas = ies_agg_UF[colunas_int]
df_coberturas_m = df_coberturas.melt(id_vars=['SG_UF_IES'])
dados = df_coberturas_m[df_coberturas_m['variable'].isin(['Cob_Mun_com_IES','Cob_Micro_com_IES'])]

f, axes = plt.subplots(1, 1,  figsize=(20, 8))
cores = sns.color_palette("Paired")
my_order = list(df_coberturas.sort_values(by='Total_IES', ascending=False)['SG_UF_IES'])

st.caption('O gráfico abaixo disponibiliza a informação de cobertura de Microrregiões contempladas com a existência de IES.')

sns.barplot(x='SG_UF_IES', y='value', hue='variable', 
            data=dados,
            ax=axes, 
            palette=cores, 
            order=my_order,
            hue_order=['Cob_Micro_com_IES','Cob_Mun_com_IES'])

axes.set_title('Distribuição IES no Brasil - Cobertura Microrregiões', fontsize=35)
axes.set_xlabel('')
axes.set_ylabel("Percentual (%)", fontsize = 30)
xlocs, xlabels = plt.xticks()
ylocs, ylabels = plt.yticks()
plt.setp(xlabels, rotation=0, fontsize=20)
plt.setp(ylabels, fontsize=20)

dados2 = df_coberturas[['SG_UF_IES','Total_IES']].sort_values(by='Total_IES', ascending=False)
x=dados2['SG_UF_IES']
y=dados2['Total_IES']
axes2 = axes.twinx()
axes2.plot(x, y, color='#cc0000', label='Total IES')
axes2.set_ylabel("Total de IES na UF", fontsize=20)
axes2.grid(visible=False)

for i, j in zip(x, y):
    axes2.text(i,j, str(j), ha='center', va='bottom', color='#cc0000', fontsize=14)

axes.legend(loc='best', fontsize=18)
st.pyplot(f)
