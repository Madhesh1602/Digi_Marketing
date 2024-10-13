import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore

cred = credentials.Certificate('digi-marketing-571c5-8708a4e81857.json')
#firebase_admin.initialize_app(cred)

 # Check if Firebase app is already initialized
st.title("Welcome to Digi-Space")

if 'username' not in st.session_state:
    st.session_state.username = ''
if 'usermail' not in st.session_state:
     st.session_state.usermail = ''

def f():
    try:
        user = auth.get_user_by_email(email)
        st.write('Login Successful')

        st.session_state.username = user.uid
        st.session_state.useremail = user.email

        st.session_state.signedout = True
        st.session_state.signout = True


    except:
        st.warning('Login Failed')
    
def t():
    st.session_state.signedout = False
    st.session_state.signout = False
    st.session_state.username = ''

if 'signedout' not in st.session_state:
    st.session_state.signedout = False
if 'signout' not in st.session_state:
    st.session_state.signout = False
    
if not st.session_state['signedout']:
    choice = st.selectbox('Login/Signup', ['Login', 'Signup'])
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
                st.balloons()  
            except Exception as e:
                st.error(f"Error creating account: {e}")

if st.session_state.signout:
    uploaded_files = st.file_uploader(
    "Choose a file", accept_multiple_files=True)

    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()

        # st.text('Name:' +st.session_state.username)
        # st.text('Email id:'+st.session_state.useremail)
    st.button('Sign out', on_click = t)