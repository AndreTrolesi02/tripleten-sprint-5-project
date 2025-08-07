import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles.csv')

bulid_hist = st.checkbox('Criar histograma')
build_scatter = st.checkbox('Criar gráfico de dispersão')

if bulid_hist:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x = 'odometer')
    st.plotly_chart(fig, use_container_width = True)

if build_scatter:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x = 'odometer', y = 'price')
    st.plotly_chart(fig, use_container_width = True)