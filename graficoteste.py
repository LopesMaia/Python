import yfinance as yf
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from tkinter import *

janela = Tk()
janela.geometry("400x400")

texto1 = Label(janela, text="Papel").pack()
t2 = Entry(janela)
t2.pack()
t=t2.get()


texto2 = Label(janela, text="Data Inicio").pack()
s2 = Entry(janela)
s2.pack()
s=s2.get()

texto3 = Label(janela, text="Data Fim").pack()
e2 = Entry(janela)
e2.pack()
e=e2.get()


def cotacao(t,s,e):
    print(t)
    print(s)
    print(e)
    ticker = t
    dateStart = s
    dateEnd = e
    #if ticker is None:
    #    ticker = "BBAS3.SA"
    #    dateStart = '2022-10-10'
    #    dateEnd = '2022-11-10'      
    
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

#def obter():
#    ticker=t
#    dateStart=s
#    dateEnd=e
#    cotacao(ticker,dateStart,dateEnd)

botao1 = Button(janela, text="Ver grafico", command= lambda: cotacao(t,s,e))
botao1.pack()
janela.mainloop()





