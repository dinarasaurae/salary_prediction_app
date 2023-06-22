import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('mergeddff_app')
df3 = pd.read_csv('df3.csv')
def show_explore_page():
    st.title('От чего зависит доход специалистов?')
    st.write('''### *по данным исследования зп по европейским странам 2019-2020 ''')
    st.write(df)
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

    fig = go.Figure(data=go.Scatter(x=df3['age'], y=df3['net_salary'], mode='markers', marker=dict(color='blue')))


    fig.update_layout(
        title='Сравнение Зарплаты и Возраста',
        xaxis=dict(title='Возраст'),
        yaxis=dict(title='Зарплата', range=[0, 250000])
    )

    st.plotly_chart(fig)

    salary_avg = df.groupby('company_type')['net_salary'].mean().reset_index()

    # Фильтрация нулевых значений
    salary_avg = salary_avg[salary_avg['company_type'] != 0]

    # Сортировка данных по усредненной зарплате
    salary_avg = salary_avg.sort_values('net_salary', ascending=False)

    # Создание столбчатой диаграммы
    fig = go.Figure(data=go.Bar(x=salary_avg['company_type'], y=salary_avg['net_salary'], marker=dict(color='blue')))

    # Настройка макета
    fig.update_layout(
        title='Сравнение зарплаты и типа компании',
        xaxis=dict(title='Тип компании'),
        yaxis=dict(title='Зарплата')
    )

    # Показать график с использованием Streamlit
    st.plotly_chart(fig)

    salary_avg = df.groupby(['seniority_level', 'gender'])['net_salary'].mean().reset_index()

    # Создание столбчатой диаграммы
    fig = go.Figure()

    # Добавление данных для мужчин
    fig.add_trace(go.Bar(x=['Junior', 'Middle', 'Senior'], y=salary_avg[salary_avg['gender'] == 'Male']['net_salary'],
                     name='Male', marker=dict(color='blue')))

    # Добавление данных для женщин
    fig.add_trace(go.Bar(x=['Junior', 'Middle', 'Senior'], y=salary_avg[salary_avg['gender'] == 'Female']['net_salary'],
                     name='Female', marker=dict(color='orange')))

    # Настройка макета
    fig.update_layout(
        title='Сравнение зарплаты по полу и уровню старшинства',
        xaxis=dict(title='Уровень старшинства'),
        yaxis=dict(title='Зарплата')
    )

    # Показать график с использованием Streamlit
    st.plotly_chart(fig)

    salary_avg = df.groupby('company_business_sector')['net_salary'].mean().reset_index()

    # Сортировка данных по усредненной зарплате
    salary_avg = salary_avg.sort_values('net_salary', ascending=False)

    # Создание bar plot
    fig = go.Figure(data=go.Bar(x=salary_avg['company_business_sector'], y=salary_avg['net_salary'], marker=dict(color='blue')))

    # Настройка макета
    fig.update_layout(
        title='Сравнение зарплаты и бизнес сектора компании',
        xaxis=dict(title='Бизнес сектор'),
        yaxis=dict(title='Зарплата')
    )

    # Показать график с использованием Streamlit
    st.plotly_chart(fig)

    salary_avg = df.groupby('position')['net_salary'].mean().reset_index()
    salary_avg = salary_avg.sort_values('net_salary', ascending=False)  # Сортировка по усредненной зарплате

    # Создание графика
    fig = go.Figure(data=go.Bar(x=salary_avg['position'], y=salary_avg['net_salary'], marker=dict(color='blue')))

    # Настройка макета графика
    fig.update_layout(
        title='Сравнение усредненной зарплаты по должностям',
        xaxis=dict(title='Должность'),
        yaxis=dict(title='Усредненная зарплата')
    )
    st.plotly_chart(fig)