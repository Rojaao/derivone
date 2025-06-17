
import streamlit as st

st.title("Robô Deriv - BOTGPT")
st.write("Este é um painel web simples para conectar à Deriv e iniciar o robô.")

token = st.text_input("Insira seu token da Deriv", type="password")
valor_inicial = st.number_input("Valor Inicial", value=0.35)
fator_martingale = st.number_input("Fator Martingale", value=1.65)
limite_lucro = st.number_input("Limite de Lucro", value=10.0)
limite_perda = st.number_input("Limite de Perda", value=10.0)
numero_candles = st.number_input("Número de Candles para Análise", value=2)
usar_martingale = st.checkbox("Usar Martingale", value=True)

if st.button("Iniciar Robô"):
    if token:
        st.success("Robô iniciado com sucesso (simulado).")
    else:
        st.error("Por favor, insira o token da Deriv.")
