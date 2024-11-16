import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

# ped = pd.read_excel("vendas.xlsx")
ped = pd.read_excel("gente.xlsx")

dados = ped.head()
# dados = ped.tail()
# dados = ped.preco

dados

ped

