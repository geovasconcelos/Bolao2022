import pandas as pd
import streamlit as st
import datetime
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


# loading data
caminho = r'https://github.com/geovasconcelos/Bolao2022/blob/main/'
Participantes = ['George', 'Adriano', 'Andrea', 'Eduardo', 'Germano', 'Priscilla', 'Rubiane', 'Aurea',
                 'Denise', 'Girlayne', 'Silvia', 'Laurindo', 'Marcus', 'Adalberto', 'Albenice', 'Claudio', 'Flavio']
Datas = ['20_nov', '21_nov', '22_nov', '23_nov', '24_nov', '25_nov', '26_nov', '27_nov', '28_nov', '29_nov', '30_nov',
         '01_dez', '02_dez']

########################################################################################

df = pd.read_excel(f'{caminho}\Copa2022.xlsm')
df.drop(['Pagto', 'Unnamed: 3', 'Unnamed: 4', 'Resultado', 'Ordem', 'Unnamed: 7', '1ª Fase', 'Unnamed: 9'], axis=1,
        inplace=True)
df.columns = ["Participantes", "Pontos"]
df.dropna(axis=0, inplace=True)
#df['Pontos'] = int(df.Pontos)
df.set_index('Participantes', inplace=True)
df.sort_values(by=['Pontos','Participantes'], ascending=True, inplace=True)
#####################################################################################


tab = pd.read_excel(f'{caminho}\Copa2022.xlsm', sheet_name='Placar')
tab.drop(['Grupo', 'Local','Unnamed: 24',
       'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13',
       'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17',
       'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21',
       'Unnamed: 22', 'Unnamed: 23'],axis=1, inplace=True)
tab.columns=['Jogo', "Dia","Hora", "Equipe1", "Gol1", "X", "Gol2", "Equipe2"]
tab.dropna(subset=['Equipe2'], inplace=True)
tab['Dia'] = pd.to_datetime(tab['Dia'], format="%d/%m/%Y")

##########################################################################################

palpites = pd.read_excel(f'{caminho}\Copa2022.xlsm', sheet_name='Palpites')
palpites.sort_values(by=['Dia', 'Jogo', 'Palpiteiro'], ascending=True, inplace=True)

#Aplicação

st.title('Bolão da Copa 2022')

st.markdown(
    """
    Bolão para participantes do grupo SCA Entrenimento para **Copa 2022**
    """
)

def Pontuacao():
    st.header('Tabela de Pontuação')
    st.table(df.style.highlight_max(axis=0))

def Palpites():
    st.header('Palpites apresentados')
    st.table(palpites)

# Sidebar
if st.sidebar.checkbox("Mostrar Tabela de jogos"):
    st.table(tab)

st.sidebar.header("Opções")

page = st.sidebar.selectbox('Selecione', ['Pontuação', 'Palpites'])
if page == 'Pontuação':
        Pontuacao()
else:
        Palpites()






# tabelas Pontuação


# SIDEBAR





#jogos de hoje

#st.subheader("Jogos de Hoje")
#today = tab['Dia'].unique()
#today = pd.to_datetime(today)
#option = st.sidebar.multiselect(
#    label='Escolha a data',
#    options=today,
#    default='2022-11-20 00:00:00')

#filtered_df = tab[tab.Dia == option]

#st.table(filtered_df)






#    dia = st.sidebar.slider('selecione o dia dos jogos', 1, 15, 30)
#    filtered_df = tab[tab.Dia.dt.day == dia]
#    st.subheader('Tabela de Jogos')
#    st.table(filtered_df)










# tabelas fixas


# multiselect dos dias
# dias = tab['Dia'].unique().tolist()
# option = st.sidebar.multiselect(
#    label='Escolha a data',
#    options=dias,
#    default=dias)

#labels = tab['Dia'].unique().tolist()

# Filtro de seleção do dia
#date_to_filter: object = st.sidebar.multiselect(
#    label='Escolha a data',
#    options=labels,
#    default=labels)

#filtered_df = tab[(tab.Dia == date_to_filter)]


# streamlit run main.py
