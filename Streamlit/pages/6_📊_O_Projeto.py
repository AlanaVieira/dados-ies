import streamlit as st
from PIL import Image



# Título e Logo
st.title("Análise de Instituições de Ensino Superior no Brasil")
col1, col2, col3 = st.columns(3)

with col1:
   st.header(" ")
with col2:
   st.header(" ")
#with col3:
  # image = Image.open("./Midia/enap.png")
  # st.image(image)


# Introdução ao Projeto
st.header("Introdução ao Projeto")
# Breve descrição do propósito e objetivo do projeto.
st.write(" O Projeto visa analisar às Instituições de Ensino Superior (IES) no Brasil utilizando Dados Abertos disponibilizados por estruturas do Governo Federal. ")
st.write("A educação é considerada como uma estrutura social determinante para o desenvolvimento do país, da sociedade e dos indivíduos. O ensino superior, para além da formação de profissionais qualificados, proporciona o desenvolvimento de avanços científicos oriundos da pesquisa e a disseminação de conhecimentos para a sociedade, mediante ações de extensão, com grande impacto social. Portanto, a análise das Instituições de Ensino Superior no Brasil pode fornecer subsídios para fundamentação de políticas públicas e insights para problemas, bem como para divulgação de dados visando transparência na ação estatal")

# Metodologia
st.header("Metodologia")
st.write("Foi realizada uma análise descritiva de dados relacionados à distribuição geográfica das iES no Brasil, por tipo de organização e categoria administrativa. Também foram analisados os dados e distribuição geográfica dos cursos ofertados por estas instituições, oferta de matrículas e características do corpo docente e discente")
st.write("Para a realização do projeto, foram obtidos dados do Censo da Educação Superior, Indicadores Sociais do Brasil, UF e municípios e dados do Atlas do Desenvolvimento Humano. Os dados foram carregados em formato .csv e, posteriormente, passaram por um processo de limpeza e preparação, com transformação de dados, manipulação de dados ausentes e renomeação de variáveis. Após esta etapa, realizou-se a combinação e mesclagem de conjunto de dados, conforme as necessidades identificadas na etapa anterior e os objetivos do projeto.")
st.write("Os dataframes criados passaram a ser analisados de modo exploratório e plotagens, por eixos temáticos: IES, cursos, matrículas, discentes, docentes e técnicos-administrativos. Para alguns dados, foram criadas séries temporais e plotagens com dados agregados.")

# Fonte de Dados
st.header("Fonte de Dados")
st.write("**Censo da Educação Superior** - Inep, 2023 - microdados 2012 a 2022. Link: https://download.inep.gov.br/microdados/microdados_censo_da_educacao_superior_2022.zip ")
st.write("**Indicadores sociais - IBGE**. Link: https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html")
st.write("**Atlas do Desenvolvimento Humano** - AtlasBR - 2010. Link: http://www.atlasbrasil.org.br/acervo/biblioteca") 
#st.write("Descrição das variáveis e o que elas representam.")

# Resultados Principais
st.header("Resultados Principais")
st.write("**Instituições** - As IES estão presentes em todos os estados do território nacional, em maior número nos estados da região sudeste do país (1.098 IES, 42,31%), condizente com a proporção populacional da região que é de aproximadamente 40 % da população total do país.")
st.write("Observa-se que das 2.595 Instituições de Ensino Superior (IES) do Brasil, há uma predominância de Faculdades (75,84%) e Centros Universitários (14,68%), totalizando 2.349 IES, ou seja, 90,52% do total de instituições no país. Ainda que dentre essas organizações estejam algumas públicas, o resultado é condizente com o encontrado na distribuição das IES por categoria administrativa, em que as instituições privadas (com e sem fim lucrativo) ocupam a proporção de 87,98% do total de IES no Brasil.")
st.write("**Cursos** - ")
st.write("**Matrículas e discentes** - ")
st.write("**Servidores Docentes e Técnico-administrativos** - ")
#st.write("Breve explicação dos resultados.")

# Conclusões e Recomendações
st.header("Conclusões e Recomendações")
st.write("Nesta primeira etapa foram analisados os dados sobre as IES de forma a proporcionar um painel visual descritivo sobre as informações disponíveis em relação às instituições, cursos, matrículas e servidores.")
st.write("Recomenda-se estudos futuros que possibilitem um estudo mais complexo, como correlações e outras análises estatíticas que possam ser realizadas com os dados disponíveis.")

# Agradecimentos
st.header("Agradecimentos")
st.write("Agradecimentos especiais ao Hélio Bomfim de Macêdo Filho, Kalina Rabbani, Thais Salzer, Bruno Garcia, Fabio Paim, Ricardo de Lima, Ricardo Ferreira da Silva Cunha, Josilene Aires Moreira, Ana Lúcia Ferraz Amstalden e demais integrantes da ENAP.")


