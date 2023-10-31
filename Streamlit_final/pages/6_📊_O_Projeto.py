import streamlit as st
from PIL import Image

# Título e Logo
st.title("Análise de Instituições de Ensino Superior no Brasil")
col1, col2, col3 = st.columns(3)

with col1:
   st.header(" ")
with col2:
   st.header(" ")
with col3:
   image = Image.open("./Midia/enap.png")
   st.image(image)


# Introdução ao Projeto
st.header("Introdução ao Projeto")
# Breve descrição do propósito e objetivo do projeto.
st.write(" O Projeto visa analisar às Instituições de Ensino Superior no Brasil Utilizando Dados Abertos disponibilizados por Entidades do Governo Federal. ")
st.write("Contextualização sobre a importância da análise de instituições de ensino.")

# Metodologia
st.header("Metodologia")
st.write("Explicação sobre as técnicas e métodos utilizados na análise de dados.")
st.write("Destaque para as bibliotecas Python e ferramentas utilizadas.")

# Fonte de Dados
st.header("Fonte de Dados")
st.write("Informações sobre a fonte dos dados utilizados para a análise.")
st.write("Descrição das variáveis e o que elas representam.")

# Resultados Principais
st.header("Resultados Principais")
st.write("Gráficos e visualizações destacando os principais insights obtidos.")
st.write("Breve explicação dos resultados.")

# Conclusões e Recomendações
st.header("Conclusões e Recomendações")
st.write("Conclusões tiradas a partir da análise de dados.")
st.write("Recomendações para possíveis ações futuras.")

# Agradecimentos
st.header("Agradecimentos")
st.write("Agradecimentos especiais a mentores, colaboradores ou fontes de apoio.")


