import streamlit as st
from pathlib import Path

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()
  
st.set_page_config(page_icon = '🔑',initial_sidebar_state='expanded',menu_items={'Get Help':'gehloth03@gmail.com','Report a bug':'https://github.com/Hg03/Story-Of-ML','About':'Intuition on Algorithms 🖋️'}) 
st.title('Story On ML')
st.sidebar.title('Articles')
articles_path = {'Linear Regression':'Linear-Regression.md','Logistic Regression':'Logistic-Regression.md','Support Vector Machine':'Support-Vector-Machine.md'}
articles = st.sidebar.selectbox('Articles',['About','Linear Regression','Logistic Regression','Support Vector Machine'])

reader = read_markdown_file(article_path[articles])
st.markdown(reader,unsafe_allow_html=True)
