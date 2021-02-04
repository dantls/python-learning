import altair as alt
import streamlit as st
import pandas as pd

from vega_datasets import data

source = data.barley()

dados = [
['25.12.20', 'Novak', 12000, 1] ,
['25.12.20', 'Andy', 11000, 3] ,
['25.12.20', 'Roger', 10500, 4] ,
['25.12.20', 'Nadal', 11500, 2] ,
['25.12.23', 'Novak', 12225, 3] ,
['25.12.23', 'Andy', 11500, 4] ,
['25.12.23', 'Roger', 12500, 2] ,
['25.12.23', 'Nadal', 13500, 1] ,
['25.12.25', 'Novak', 12805, 4] ,
['25.12.25', 'Andy', 14200, 3] ,
['25.12.25', 'Roger', 15500, 1] ,
['25.12.25', 'Nadal', 14500, 2] ,
]

df_dados = pd.DataFrame(data=dados, columns=['week_title','full_name','ranking_points','rank_number'])

st.dataframe(df_dados)
bars = alt.Chart(df_dados).mark_bar().encode(
  x=alt.X('ranking_points:Q'),
  y=alt.Y('full_name:N',sort='-x')
).properties(
       width=650, 
       height=400
  )

bar_plot = st.altair_chart(bars)





st.dataframe(source)
bars = alt.Chart(source).mark_bar().encode(
    x='sum(yield):Q',
    y=alt.Y('site:N', sort='-x')
)

st.altair_chart(bars)

