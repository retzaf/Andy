import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.title("aleatorio")
st.sidebar.header("aleatorio")
st.sidebar.write("aleatorio")

st.sidebar.image("logo-clinica-davila.jpg")
if st.sidebar.button("aleatorio"):
    st.sidebar.write("aleatorio")
 
user_input = st.sidebar.text_input("aleatorio")
st.sidebar.write("aleatorio", user_input)
