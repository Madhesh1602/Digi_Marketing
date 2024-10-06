import streamlit as st
from streamlit_option_menu import option_menu


import log, uploader

st.set_page_config(
    page_title = "Digi-Space",
)

class MultiApp:

    def __init__(self):
        self.apps = []
    def add_add(self, title, function):
        self.apps.append({
            "title": title,
            "function": function,
        })

    def run():
        with st.sidebar:        
            app = option_menu(
                menu_title='Digi-Space',
                options=['log','uploader'],
                icons=['house-fill','arrow-bar-up'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'}, "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
        )

        if app == "log":
            log.app()
        if app == "uploader":
            uploader.app()    
        
             
             
    run()               