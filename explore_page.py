import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('mergeddff_app')

def show_explore_page():
    st.title('От чего зависит доход специалистов?')
    st.write('''### *по данным исследования зп по европейским странам 2019-2020 ''')
    st.write(':blue[Зависимомть зарплаты от количества лет опыта]')
    fig = px.scatter(
        df, 
        x = 'experience', 
        y = 'net_salary')
    st.plotly_chart(fig)

    fig = go.Figure(data=[
        go.Histogram(
            x=df['company_business_sector'],
            y=df['net_salary'],
            marker={'color': 'blue'}
                        )
                            ])

    # Настройка макета графика
    fig.update_layout(
    title='Сравнение зарплаты и типа компании',
    xaxis_title='Тип компании',
    yaxis_title='Зарплата',
    bargap=0.1
                        )
    st.plotly_chart(fig)




    