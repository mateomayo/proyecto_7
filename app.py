import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

st.header('Mi primera app web')

st.write('Esta aplicación es mi proyecto del Sprint 7 del Bootcamp de Ciencia de Datos')

# Botón para el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Solo se ejecuta si se presiona el botón de histograma
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para el gráfico de dispersión
disp_button = st.button('Construir Gráfico de Dispersión')

if disp_button:  # Solo se ejecuta si se presiona el botón de gráfico de dispersión
    st.write('Creación de un Gráfico de Dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
