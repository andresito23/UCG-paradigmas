import streamlit as st
import libreria_funciones as lf

st.title("Paradigmas de la Programación")

st.sidebar.image("logocsg.png")

st.sidebar.title("Parámetros")

st.write("Elaborado por Andrés Alvear")

capital = st.number_input("Ingrese el capital", value = 1000)
tasa_anual_pct = st.number_input("Ingrese de la tasa anual", value = 0.15)
dias_mora = st.number_input("Ingrese los días de mora",value =30)

resultado = lf.calcular_interes_mora(capital,tasa_anual_pct,dias_mora)

st.write("El reusltado por atraso es:", resultado)
