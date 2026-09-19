import streamlit as st
import libreria_funciones as lf

st.title("Paradigmas de la Programación")

st.sidebar.image("logocsg.png")

st.sidebar.title("Parámetros")

st.write("Elaborado por Andrés Alvear")

capital = st.number.input ("ingrese el Capital")
tasa_anualpct = st.number_input ("Ingrese la tasa anual")

resultado = lf.calcular_interes_mora()
