import altair as alt
import streamlit as st
import pandas as pd
import time

data = [
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

df_dados = pd.DataFrame(data=data, columns=['week_title','full_name','ranking_points','rank_number'])

week_list = df_dados['week_title'].unique()


bars = alt.Chart(df_dados).mark_bar().encode(
  x=alt.X('1:Q',axis=alt.Axis(title='ATP Ranking Points')),
  y=alt.Y('0:N',axis=alt.Axis(title='The Big Four'))
  ).properties(
      width=750,
      height=400
  )

bar_plot = st.altair_chart(bars)

def plot_bar_animated_altair(df, week):
  bars = alt.Chart(df, title="Ranking as of week: "+week).mark_bar().encode(
    x=alt.X('ranking_points:Q', axis=alt.Axis(title='ATP Ranking Points')),
    y=alt.Y('full_name:N',axis=alt.Axis(title='The Big Four'),sort='-x'),
    color=alt.Color('full_name:N', title='Players',  legend=alt.Legend(orient="left")), 
    ).properties(
        width=750, 
        height=400
    )
  text = bars.mark_text(
    align='left',
    baseline='middle',
    dx=0, # Nudges text to right so it doesn't appear on top of the bar
    fontSize=20,
    color='black'
  ).encode(
        text='ranking_points:Q'
  )


  return bars + text


if st.button('Plot'):
  for week in week_list:
    weekly_df = df_dados[df_dados['week_title']==week]       
    bars = plot_bar_animated_altair(weekly_df, week)
    time.sleep(0.8) 
    bar_plot.altair_chart(bars)
