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
        'Software Engineer',
        'Frontend Developer',
        'Designer',
        'PM',
        'Engineering manager',
        'Network Engineer',
        'Hardware Engineer',
        'IOS Developer'
    )

    company_types = (
        'Pharma',
        'E-commerce',
        'Consulting',
        'Product',
        'Fintech',
        'Media',
        'Personal Ltd',
        'Cloud',
        'FAANG',
        'Enterprise',
        'Manufacturing',
        'Education'
    )

    cities = (
        'Kiev',
        'Oslo',
        'Berlin',
        'Saint-Petersburg',
        'Munich',
        'Karlsruhe',
        'Hamburg',
        'Augsburg ', 
        'Bremen' ,
        'Frankfurt',
        'Regensburg', 
        'Lisbon', 
        'Leipzig', 
        'Stuttgart',
        'Amsterdam',
        'Luxembourg',
        'Bern',
        'Bonn', 
        'Köln',
        'London',
        'Moscow'
    )

    company_size = st.slider('размер компании', 10.0, 10000.0, 10.0)
    experience = st.slider('опыт', 1.0, 40.0, 0.2)
    age = st.slider('возраст', 16.0, 60.0, 0.2)
    seniority = st.selectbox('уровень', seniority_levels)
    main_lang = st.selectbox('основной язык общения с коллегами', main_langs)
    gender = st.selectbox('гендер', genders)
    position = st.selectbox('позиция', positions)
    company_type = st.selectbox('тип_компании', company_types)
    city = st.selectbox('город', cities)
    

    flag = st.button('Рассчитать')
    if flag:
        X = pd.DataFrame(data=[[company_size, experience, age, seniority, main_lang, gender, position, company_type, city]], columns=['company_size', 'experience', 'age', 'seniority_level', 'main_language', 'gender', 'position', 'company_type', 'city'])
        salary = data.predict(X)
        st.subheader(f'Твоя зарплата €{salary[0]:2f}')