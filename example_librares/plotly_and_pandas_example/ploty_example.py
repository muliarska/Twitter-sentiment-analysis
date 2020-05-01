import plotly
import plotly.express as px
import pandas as pd
import os

data = pd.read_fwf('data.txt')

fig = px.bar(data, x='year', y='pop',
             hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
             labels={'pop': 'population of Canada'}, height=400)

plotly.offline.plot(fig, filename=f, auto_open=False)
