import streamlit as st  
import requests

# API URL
URL = "https://api.agify.io"

name = st.text_input("Enter your name: ")

# input params
PARAM = {"name":name}

# Get the result from the API
res = requests.get(url=URL, params=PARAM)
data = res.json()

if st.button("Calculate Age"):
    st.write(f"{data['name']} is {data['age']} years old.")