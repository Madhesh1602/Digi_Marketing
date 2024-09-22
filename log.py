import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('digi-marketing-571c5-8708a4e81857.json')
    firebase_admin.initialize_app(cred)

st.title("Welcome to Digi-Space")
choice = st.selectbox('Login/Signup', ['Login','Sign Up'])

def f():
    try:
        user = auth.get_user_by_email(email)
        print (user.uid)
        st.write('Login Successful')
    except:
        st.warning('Login Failed')


if choice == 'Login':
    email = st.text_input('Email Address')
    password = st.text_input('Password', type='password')

    st.button('Login', on_click = f)

else:
    email = st.text_input('Email Address')
    password = st.text_input('Password', type='password')
    username = st.text_input('Create Username')

    if st.button('Create my account'):
        try:
            user = auth.create_user(email=email, password=password, uid=username)
            st.success('Account created successfully!')
            st.markdown('Please Login using your email and password')
            st.balloons()  # Note: The method is 'st.balloons()' not 'st.ballons()'
        except Exception as e:
            st.error(f"Error creating account: {e}")
