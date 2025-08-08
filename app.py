import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles.csv')

bulid_hist_1 = st.checkbox('Criar histograma da distribuição da quilometragem')
build_scatter = st.checkbox('Criar gráfico de dispersão da relação entre o preço e a quilometragem')
build_bar_1 = st.checkbox('Criar gráfico de barras do preço médio dos veículos pelo tipo de modelo')
build_bar_2 = st.checkbox('Criar gráfico de barras da quantidade de veículos pelo tipo de combustível')
build_hist_2 = st.checkbox('Criar histograma da condição dos veículos pelo ano do modelo')

if bulid_hist_1:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x = 'odometer')
    st.plotly_chart(fig, use_container_width = True)

if build_scatter:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x = 'odometer', y = 'price')
    st.plotly_chart(fig, use_container_width = True)

if build_bar_1:
    st.write('Criando um gráfico de barras com o preço médio por tipo de modelo')
    avg_price_by_vehicle_type = car_data.groupby('type')['price'].mean().reset_index()
    fig = px.bar(avg_price_by_vehicle_type, x = 'type', y = 'price')
    fig.show()

if build_bar_2:
    st.write('Criando um gráfico de barras da quantidade de veículos disponíveis pelo tipo de combustível')
    fuel_types_count = car_data['fuel'].value_counts().reset_index()
    fuel_types_count.columns = ['fuel_type', 'count']
    fig = px.bar(fuel_types_count, x = 'fuel_type', y = 'count')
    fig.show()

if build_hist_2:
    st.write('Criando histograma das condições dos veículos pelo ano do modelo')
    fig = px.histogram(car_data, x = 'model_year', color = 'condition')
    fig.show()