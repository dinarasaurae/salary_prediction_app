import streamlit as st
from predict_page_copy import show_predict_page
from explore_page import show_explore_page

page_bar = st.sidebar.selectbox('люблю_Белобрыса', ('Предсказать зп', 'Узнать, как заработать больше'))
if page_bar == 'Предсказать зп':
    show_predict_page()
if page_bar == 'Узнать, как заработать больше':
    show_explore_page()