import streamlit as st
import libreria_funciones as lf
st.title("Paradigmas de la Programación")
st.sidebar.image("logo_UCG.png")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Ronald Rodríguez Castro")
capital = st.number_input("Ingrese el capital: ")
tasa_anual_pct = st.number_input("Ingrese tasa anual: ")
dias_mora = st.number_input("Ingrese los días de mora: ")

resultado = lf.calcular_interes_mora()
