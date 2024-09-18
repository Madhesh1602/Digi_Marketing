import streamlit as st

st.title("Welcome to Digi-Space")
choice = st.selectbox('Login/Signup', ['Login','Sign Up'])
if choice == 'Login':
    email = st.text_input('Email Address')
    password = st.text_input('Password', type = 'password')

    st.button('Login')

else:
    email = st.text_input('Email Address')
    password = st.text_input('Password', type = 'password')

    username = st.text_input('Create Username')

    st.button('Create my account')