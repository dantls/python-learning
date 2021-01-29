import streamlit as st
import pandas as pd
import time
import altair as alt
from altair import Chart, X, Y, Axis, SortField, OpacityValue

data = pd.read_excel('dados.xlsx')

df_br = pd.DataFrame(data)

df_br.reset_index()

columns = ['Data de Fim da Consulta', 'Data de Início da Consulta', 'Link do Jogo','Turno','Estádio','Cidade' ]
df_br = df_br.drop(columns, axis=1)

df_mandante = df_br[(df_br['Série'] == 'A')][['Temporada', 'Mandante','Visitante','Gol Mandante','Gol Visitante','Série','Rodada','Resultado']]
df_visitante = df_br[(df_br['Série'] == 'A')][['Temporada','Mandante','Visitante','Gol Mandante','Gol Visitante','Série','Rodada','Resultado']]

def result(x, y):
    if x < y: 
      return 0
    elif x > y:
      return 3
    else:
      return 1

df_mandante['Resultado'] = df_mandante.apply(lambda row: result(row['Gol Mandante'], row['Gol Visitante']), axis=1)
df_visitante['Resultado'] = df_visitante.apply(lambda row: result(row['Gol Visitante'], row['Gol Mandante']), axis=1)
frames =[df_mandante ,df_visitante ]
result = pd.concat(frames, keys=["Mandante", "Visitante"])

result = result.sort_index()
result = result.reset_index()

result.rename( {'level_0': 'Jogo', 'level_1': 'Nro'}, axis=1, inplace=True) 

def news(x):
    if x['Jogo'] == 'Mandante':
      return x['Mandante']
    elif x['Jogo'] == 'Visitante': 
      return x['Visitante']

result['Time'] = result.apply(lambda row: news(row) , axis=1)

df_dados = result.loc[:][['Rodada','Temporada','Time','Resultado']].copy()

df_dados.sort_values(by=['Rodada'] ,ascending=True , inplace=True)

df_dados['Acumulado'] = df_dados.groupby(['Temporada','Time'])[['Time','Resultado']].cumsum()

x = st.slider('Selecione o ano',2012, 2019, (2012))

df_dados = df_dados[df_dados['Temporada'] == x].reset_index(drop=True)

st.dataframe(df_dados)

bars = alt.Chart(df_dados).mark_bar().encode(
    x=X('2:Q',axis=Axis(title='Brasileirao')),
    y=Y('0:Q',axis=Axis(title='Times'))
    ).properties(
        width=650, 
        height=400
    )

bar_plot = st.altair_chart(bars)

def plot_bar_animated_altair(df,week):
    bars = alt.Chart(df, title="Ranking por Rodada :"+week)

for week in range(1,39):
  teste = str(week)
  bars = plot_bar_animated_altair(df_dados[df_dados['Rodada']== teste],teste)
  time.sleep(0.01) 
  
  bar_plot.altair_chart(bars)