import yfinance as yf
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

ticker = "BBAS3.SA"
dateStart = '2022-10-10'
dateEnd = '2022-11-10'
listaData = []
listaPreco = []

stock_info=yf.Ticker(ticker).history(start=dateStart, end=dateEnd)

df = pd.DataFrame(stock_info)

for index, row in df.iterrows():
    date_string = index.strftime("%d-%m")
    listaData.append(date_string)
    listaPreco.append(row["Close"])

plt.plot(listaData, listaPreco)
plt.title(ticker)
plt.xlabel('Data')
plt.ylabel('Fechamento')
plt.show()