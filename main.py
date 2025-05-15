import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from login_app import show_login
from home_app import show_home

# Data login
USERNAME = "admin"
PASSWORD = "admin"

# Cek status login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def main():
        if st.session_state.logged_in:
            show_home()  # Pindahkan semua logika halaman utama ke home_app.py
        else:
            show_login(USERNAME, PASSWORD)  # Login page ada di login_app.py

if __name__ == "__main__":
    main()


