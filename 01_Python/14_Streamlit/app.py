import streamlit as st
import pandas as pd
import numpy as np

## Title of the aplication
st.title("Heloo Streamlit")

## Display a simple Text
st.write("Thise is a imple text")

## Create a simple DataFrame

df = pd.DataFrame({
    'first column' : [1,2,3,4,5],
    'second column' : [10,20,30,40,50]
})

## Display the DataFrame
st.write("Here is the dataframe")
st.write(df)

## create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)