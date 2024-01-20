import streamlit as st
import numpy as np
import statsmodels.api as sm

st.title('A1C to Average Glucose Using Simple Linear Regression')

# Create lists for training
A1C = [5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
avg_gluc = [80, 100, 120, 140, 155, 170, 185, 200, 215, 225, 240]

# Create and train model
ols = sm.OLS(avg_gluc, A1C).fit()

# Get user A1C input for prediction
inputA1C = st.text_input("Enter your A1C level in decimal format, i.e., 7.1: ", 0.0)

# convert inputA1C string to float
testA1C = [float(inputA1C)]

# Make prediction
result = ols.predict(testA1C)

# Display result
st.write("Your average daily glucose is: ", result[0])