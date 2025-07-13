import streamlit as st

st.title("Streamlit Text input")
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello {name}")

age =st.slider("Select your age:",0,100,18)
st.write(f"Your age is {age}.")

options = ["Python","Java","Rust","JavaScript"]
choice = st.selectbox("Choose your favorite Language:", options)
st.write(f"You selected {choice}.")

