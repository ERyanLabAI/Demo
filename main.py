import streamlit as st
# Get user A1C input for prediction
inputA1C = st.text_input("Enter your A1C level in decimal format, i.e., 7.1: ", 0.0)

# Display result
st.write("Your average daily glucose is: ", inputA1C)
