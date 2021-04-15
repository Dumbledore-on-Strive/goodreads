import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np
from PIL import Image


st.title("  Dumblodere Team  ")

st.markdown(" Team members")
frame1, frame2, frame3, frame4 = st.beta_columns(4)

with frame1:
    st.header("Nurlan Sarkhanov")
    # st.image("https://static.streamlit.io/examples/cat.jpg")
with frame2:
    st.header("Fabio Fistarol")
with frame3:
    st.header("Agathiya Raja")
with frame4:
    st.header("Camelia Ignat")


def main():
    menu = ["Home", "Data Scrapping", "Data Processing", "Data Visualisation"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home")
        to_do1 = st.checkbox("Web Scrapping ")
        to_do2 = st.checkbox("Data Analysis")
        to_do3 = st.checkbox("Data Prosessing")
        to_do4 = st.checkbox("Data Visualization")
        to_do5 = st.checkbox("about dumbloder")
        # if to_do1:
        #     st.checkbox(value=True)
        # if to_do2:
        #     st.checkbox(value=True)
        # if to_do3:
        #     st.checkbox(value=True)
        # if to_do4:
        #     st.checkbox(value=True)
        # if to_do5:
        #     st.checkbox(value=True)
        image = Image.open('cartoon.png')
        st.image(image, caption='Dumbledore')
        st.success("Scrapping 1000 books details from www.goodreads.com")
        st.button("Project Github timeline ")
        st.success("Scrapping 1000 books details from www.goodreads.com")
        st.write(
            'About The project .What we did, What we will do to imporve code :sunglasses:')
        agree = st.checkbox("I agree")
        if agree:
            st.checkbox("Great", value=True)
    elif choice == "Data Scrapping":
        st.subheader("Data Processing")

    elif choice == "Data Processing":
        st.subheader("Data Processing")
    else:
        st.subheader("Data Visualisation")


main()
