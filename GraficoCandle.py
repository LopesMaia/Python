import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import yfinance as yf

ticker = "BBAS3.SA"
dateStart = '2022-01-10'
dateEnd = '2023-01-10'
listaData = []

stock_info=yf.Ticker(ticker).history(start=dateStart, end=dateEnd)
df = pd.DataFrame(stock_info)

for index, row in df.iterrows():
    date_string = index.strftime("%y-%m-%d")
    listaData.append(date_string)

fig = go.Figure(data=[go.Candlestick(
                x=listaData,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                increasing_line_color= 'green', 
                decreasing_line_color= 'gray')])

fig.show()