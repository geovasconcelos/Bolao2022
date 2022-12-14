import pandas as pd
import streamlit as st
import datetime
import numpy as np
import openpyxl
import plotly.express as px

# loading data

df = pd.read_excel('https://github.com/geovasconcelos/Bolao2022/blob/main/Copa2022.xlsm?raw=true', engine="openpyxl", sheet_name='Regras')        
df.drop(['Pagto', 'Unnamed: 3', 'Unnamed: 4', 'Resultado', 'Ordem', 'Unnamed: 7', '1ª Fase', 'Unnamed: 9'], axis=1,
        inplace=True)
df.columns = ["Participantes", "Pontos"]
df.dropna(axis=0, inplace=True)
#df['Pontos'] = int(df.Pontos) 
df.set_index('Participantes', inplace=True)
df.sort_values(by=['Pontos','Participantes'], ascending=False, inplace=True)

@st.cache
def Pontuacao():
        return df
df2 = Pontuacao()
#####################################################################################

tab = pd.read_excel('https://github.com/geovasconcelos/Bolao2022/blob/main/Copa2022.xlsm?raw=true', engine="openpyxl", sheet_name='Placar')
tab.drop(['Grupo', 'Local','Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15',
          'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22',
          'Unnamed: 23','Unnamed: 24'], axis=1, inplace=True)
tab.columns=['Jogo', "Dia","Hora", "Equipe1", "Gol1", "X", "Gol2", "Equipe2"]
tab.dropna(subset=['Jogo'], inplace=True)
#tab['Dia'] = pd.to_datetime(tab['Dia'], format="%d/%m/%Y")
#tab['Dia'] = tab.Dia.dt.strftime('%d/%m/%Y')

@st.cache
def Placares():
        return tab
tab2 = Placares()
##########################################################################################

def Pitacos():
        return pd.read_excel('https://github.com/geovasconcelos/Bolao2022/blob/main/Copa2022.xlsm?raw=true', engine="openpyxl", sheet_name='Palpites')
palpites = Pitacos()
palpites.sort_values(by=['Dia', 'Jogo', 'Palpiteiro'], ascending=True, inplace=True)
###########################################################################################
stats = pd.read_excel('https://github.com/geovasconcelos/Bolao2022/blob/main/Copa2022.xlsm?raw=true', engine="openpyxl", sheet_name='stats')        
#stats.set_index('Participante', inplace=True)
stats.sort_values(by=["Acertos"], ascending=False, inplace=True)

################################################################################################
champ = pd.read_excel('https://github.com/geovasconcelos/Bolao2022/blob/main/Copa2022.xlsm?raw=true', engine="openpyxl", sheet_name='campeao')        
champ.set_index('Participantes', inplace=True)

################################################################################################

#Aplicação

image = 'https://jcconcursos.com.br/media/_versions/noticia/copa-do-mundo-2022-catar_widelg.jpg'
st.image(image, use_column_width=True)

st.title('Bolão da Copa 2022')

st.markdown(
    """
    Bolão para participantes do grupo SCA Entrenimento para **Copa 2022**
    """
)

def Pontuacao():
    st.header('Tabela de Pontuação')
    st.table(df2)

def Palpites():
    st.header('Palpites apresentados')
    st.table(palpites)

# Sidebar
if st.checkbox("Mostrar Tabela de jogos"):
    st.table(tab2)

#st.sidebar.header("Opções")

page = st.selectbox('Selecione o que você deseja visualizar', ['Pontuação', 'Palpites'])
if page == 'Pontuação':
        Pontuacao()
else:
        Palpites()

#st.table(stats)
st.header('Quantidade de acertos de placares exatos por participante')
fig = px.bar(stats, x='Participante', y='Acertos')
st.plotly_chart(fig)

st.header('Palpites dos Campeões')
st.table(champ)
