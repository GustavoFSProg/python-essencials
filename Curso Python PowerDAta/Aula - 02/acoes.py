import streamlit as st
import yfinance
import matplotlib 
import plotly.express as px
import pyautogui
import pyperclip




st.set_page_config(layout="wide")

# st.set_page_config(page_title="Meu Site Streamlit")

bb = "BANCO DO BRASIL:   BBAS3.SA"
petrobras = "PETROBRAS:   PETR4.SA"

bb
petrobras

# acao = st.text_input("Código da Acão:")

# acao = input("Codigo da Acao: ")
# acao = "PETR4.SA"
acao = "BBAS3.SA"

dados = yfinance.Ticker(acao).history("6mo")


# matplotlib.pyplot.plot(dados.Close)
 

# fechamento = px.line(x=dados, y=dados.Close, title="Vendas x Ano", height=400, width=1000, line_shape='spline')
fechamento = (dados.Close)


maximo = fechamento.max()
min = fechamento.min()
atual = fechamento[-1]
acao

fechamento

"Cotação Mínima:", round(min, 2)
"Cotação Máxima:", round(maximo, 2)


"Cotação Atual:", round(atual, 2)


# pyautogui.PAUSE= 2

# pyautogui.hotkey("ctrl","t")

# pyperclip.("www.gmail.com")
# pyperclip.tex("OKKK")

# pyautogui.hotkey("ctrl","v")
# pyautogui.hotkey("enter")




st.line_chart(dados.Close)


# fechamento.plot()


