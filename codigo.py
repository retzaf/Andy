import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.title("clinica davila won")
st.sidebar.header("va pegao el loco")
st.sidebar.write("va pegao")

st.sidebar.image("logo-clinica-davila.jpg")
if st.sidebar.button("va pegao loco won"):
    st.sidebar.write("fue el loco")
 
user_input = st.sidebar.text_input("ya fue")
st.sidebar.write("iba pegao el", user_input)
