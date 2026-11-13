import streamlit as st
import requests
import os

API_URL = os.environ.get("API_URL", "http://localhost:8000")

st.title("JurisFlow Dashboard")
st.write("Welcome to JurisFlow")

if st.button("Check API Health"):
    try:
        response = requests.get(f"{API_URL}/health", timeout=5)
        if response.status_code == 200:
            st.success("API is healthy!")
            st.json(response.json())
        else:
            st.error(f"API returned status code {response.status_code}")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")
