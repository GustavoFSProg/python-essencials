from fpdf import FPDF # type: ignore
# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.set_page_config(layout="wide")

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")
pdf.image("template.png", x=0, y=0)

descricao = input("Descrição do Projeto:")
horas_previstas = input("Horas Prevsitas:")
valor_hora = input("Valor Horas:")
prazo = input("Prazo: ")

valor_total = int(valor_hora) * int(horas_previstas)

pdf.text(115, 145, descricao)
pdf.text(115, 160, horas_previstas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output("Orcamento.pdf")

print("Orçamento criado com Sucesso!")

# df = print(valor_total)

