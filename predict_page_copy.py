import streamlit as st
import pickle
import numpy as np
import pandas as pd

def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()


def show_predict_page():
    st.title('Давай узнаем, в рынке ли твоя зарплата')
    st.write('''### Укажи бэкграунд для предсказания зп ''')

    seniority_levels = (
        'Junior',
        'Middle',
        'Senior',
        'Lead',
        'No level'
    )

    main_langs = (
        'German',
        'English',
        'Russian',
        'French',
        'Polish',
        'Spanish',
        'Italian',
        'Dutch',
        'Ukrainian',
        'Czech'
    )

    genders = (
        'Male',
        'Female',
        'Diverse'
    )

    positions = (
        'QA',
        'Software Engineer'
    )

    experience = st.slider('опыт', 0.0, 40.0, 0.2)
    age = st.slider('возраст', 0.0, 60.0, 0.2)
    seniority = st.selectbox('уровень', seniority_levels)
    main_lang = st.selectbox('основной язык общения с коллегами', main_langs)
    gender = st.selectbox('гендер', genders)
    position = st.selectbox('позиция', positions)
    

    flag = st.button('Рассчитать')
    if flag:
        X = pd.DataFrame(data=[[experience, age, seniority, main_lang, gender, position]], columns=['experience', 'age', 'seniority_level', 'main_language', 'gender', 'position'])
        salary = data.predict(X)
        st.subheader(f'Твоя зарплата €{salary[0]:2f}')