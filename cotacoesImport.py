import yfinance as yf
import pandas as pd
from datetime import datetime

ticker = "BBAS3.SA"
dateStart = '2022-12-20'
dateEnd = '2022-12-23'

stock_info=yf.Ticker(ticker).history(start=dateStart, end=dateEnd)

df = pd.DataFrame(stock_info)

for index, row in df.iterrows():
    date_string = index.strftime("%d-%m")
    print(f"Data: {date_string}")
    price_format = "{:.2f}".format(row["Close"])
    print(f'Fechamento: {price_format}')
    print("")
