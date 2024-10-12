import pickle
from pathlib import Path

import streamlit_authenticator as stauth

# --- USER AUTHENTICATION ---

names = ["Madhesh", "Vijay"]
usernames = ["madds1606", "vijay2607"]

# Load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file: 
    hashed_passwords = pickle.load(file)


authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "our next page", "abcdef", cookie_expiry_days = 30 )


name, authenticator, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your name and password")

if authentication_status:
    


    #--- SIDEBAR ---
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")


