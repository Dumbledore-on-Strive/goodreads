import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np
from PIL import Image
import plotly.express as px


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


@st.cache(persist=True)
def load_data(ty):
    if ty == "raw":
        data = pd.read_csv(
            '/home/nsarkhanov/code/github/AI_Course_Exercise/M2/Team_build/goodreads/goodreads_1000_books_list.csv')
    if ty == "clean":
        data = pd.read_csv(
            "/home/nsarkhanov/code/github/AI_Course_Exercise/M2/Team_build/goodreads/preprocess_data.csv")
    return data


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
        data = load_data('raw')
        header = st.beta_container()
        dataset = st.beta_container()

        with dataset:
            st.header("1000 books data frame from scrapper")
            book_data = load_data("raw")
            st.write(book_data.head(10))
            # number_list = book_data.shape[0]
            # st.success("Efficiency percentage of data  Scrapping ")
            # eff_sc = st.button("Show Answer :sunglasses: ", key="1")
            # if eff_sc:
            #     st.write(number_list/10, "%")
            # st.text(
            #     " we extract data from website with  95 percentage  effciency  ")

    elif choice == "Data Processing":
        st.subheader("Data Processing")
        ############################################################################################################################
    else:
        st.subheader("Data Visualisation")
        data = load_data("clean")
        filters = st.sidebar.radio(
            'Selection', ("The most awarded book", "The best Author", "The highest rating book "))
        # st.sidebar.markdown(data.query(""))
        st.sidebar.markdown("Select what kind of Graph you want")
        np.select = st.sidebar.selectbox(
            "Graph type", ['Histogram', 'Pie Chart'], key='1')
#############################################
        sentiment_count = data['series'].value_counts()
        sentiment_count = pd.DataFrame(
            {'Sentiment': sentiment_count.index, 'series': sentiment_count.values})
###########################################################################
        st.write(data.head(10))
        # graph bar chart mean
        tmp = data.groupby("original_publish_year")[
            "award"].mean().sort_values()
        st.bar_chart(tmp)
#############################################################################
        tmp = data.groupby("original_publish_year")[
            "award"].max().sort_values()
        st.bar_chart(tmp)
#########################################################################################


###########################################################
        st.subheader(
            "Avarage rating vs Number of Pages\n   The biggest has more  avards")

        # colors = np.random.rand(data.shape[0])
        # sns.scatterplot(data['num_pages'], data['num_rating'],
        #                 s=size_b, c=colors, alpha=0.7, legend=True, label="the biggest get most  award")
        # st.set_option('deprecation.showPyplotGlobalUse', False)
        # st.pyplot()
        # df = px.data.gapminder()

        t = data.head(100)
        size_b = t['award']**3 + 20
        px.scatter(t, x="num_pages", y="num_rating",  # data.query("year==2007"),
                   size=size_b, color="minmax_norm_ratings",
                   hover_name="series", log_x=True, size_max=60)
        st.pyplot()
################################################################################################################################
        st.subheader(
            "Min-Max Normalization  vs Mean Normalisation  vs before Normalization Distrubtion")
        sns.histplot(data, x="avg_rating", color="skyblue",
                     label="Before Normalization", kde=True)
        sns.histplot(data, x="minmax_norm_ratings", color="skyblue",
                     label="Min-Max Normalization", kde=True)
        sns.histplot(data, x="mean_norm_ratings", color="red",
                     label="Mean Normalization", kde=True)
        sns.set(rc={'figure.figsize': (7, 8)})


###########################################################################################################
main()
