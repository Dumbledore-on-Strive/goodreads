import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np
from PIL import Image
import plotly.express as px


# st.title("  Dumblodere Team  ")

# st.markdown(" Team members")
# frame1, frame2, frame3, frame4 = st.beta_columns(4)

# with frame1:
#     st.header("Nurlan Sarkhanov")
#     # st.image("https://static.streamlit.io/examples/cat.jpg")
# with frame2:
#     st.header("Fabio Fistarol")
# with frame3:
#     st.header("Agathiya Raja")
# with frame4:
#     st.header("Camelia Ignat")


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
        ####################################################
        header = st.beta_container()
        team = st.beta_container()
        activities = st.beta_container()
        dataset = st.beta_container()
        conclusion = st.beta_container()
        footer = st.beta_container()
        ####################################################
        with header:
            st.title('Dumbledore on Strive!')  # site title h1
            st.text(' ')
            image = Image.open('cartoon.png')
            st.image(image, caption='Dumbledore')
            st.markdown(
                "Enjoy the journey and you'll see the magic :sparkles:")
            st.text(' ')
            st.markdown(
                '* **Webscraping:** get the information (data) from the web')
            st.markdown('* **Dataframe:** add the data a spreadsheet file')
            st.markdown(
                '* **Plot:** create plot and graphs for better visualization')
            st.text(' ')
            st.text(' ')
            with team:
                # meet the team button
                if st.button("Meet the team"):
                    st.header('Team')
                    st.markdown(
                        '* [Fabio Fistarol](https://github.com/fistadev)')
                    st.markdown(
                        '* [Agathyia Raja](https://github.com/AgathiyaRaja)')
                    st.markdown(
                        '* [Camelia Ignat](https://github.com/avocami)')
                    st.markdown(
                        '* [Nurlan Sarkhanov](https://github.com/nsarkhanov)')
                    st.text(' ')
                    st.text(' ')
        #     'About The project .What we did, What we will do to imporve code :sunglasses:')
        agree = st.checkbox("I agree")
        if agree:
            st.checkbox("Great", value=True)

        with activities:
            if st.button("Activities"):
                to_do1 = st.checkbox("Web Scrapping ")
                to_do2 = st.checkbox("Data Analysis")
                to_do3 = st.checkbox("Data Prosessing")
                to_do4 = st.checkbox("Data Visualization")
                to_do5 = st.checkbox("* Business Scenario")
                st.text(' ')

        with dataset:
            st.header('Goodreads - Books That Should Be Made Into Movies')
            df = load_data('raw')
            if st.button("View Full Data"):
                st.write(df)

##########################################################################
    elif choice == "Data Scrapping":
        st.subheader("Data Processing")
        data = load_data('raw')
        header = st.beta_container()
        dataset = st.beta_container()

        with dataset:
            st.header("1000 books data frame from scrapper")
            book_data = load_data("raw")
            st.write(book_data.head(10))

    elif choice == "Data Processing":
        st.subheader("Data Processing")
        ############################################################################################################################
    else:
        st.subheader("Data Visualisation")
        data = load_data("clean")
        # the all graphic functions
        #  Scatter plots

        def scatter_2D_plot(data):
            size_b = data['award']**2*12
            colors = np.random.rand(data.shape[0])
            sns.scatterplot(data['num_pages'], data['num_rating'],
                            s=size_b, c=colors, alpha=0.5, legend=True)

        def group_bar_chart(data):
            st.markdown("")
            st.markdown("")
            st.subheader("The published Book by year ")
            st.markdown("")
            st.markdown("")
            tmp = data.groupby("original_publish_year")[
                "award"].mean().sort_values()

            st.bar_chart(tmp)

        def norm_functions(data):
            st.markdown("")
            st.markdown("")
            st.subheader(
                "Min-Max Normalization vs Mean Normalisation vs before Normalization Distrubtion\n")
            st.markdown("")
            # sns.histplot(data, x="avg_rating", color="green",
            #              label="Before Normalization", kde=True)
            # sns.histplot(data, x="minmax_norm_ratings", color="skyblue",
            #              label="Min-Max Normalization", kde=True)
            # sns.histplot(data, x="mean_norm_ratings", color="red",
            #              label="Mean Normalization", kde=True)
            x1 = data["minmax_norm_ratings"]
            x2 = data["mean_norm_ratings"]
            x3 = data["avg_rating"]
            hist_data = [x1, x2, x3]
            group_labels = ['Min-Max Normalization',
                            'Mean Normalization', 'Before Normalization Avarge rate']
            fig = ff.create_distplot(
                hist_data, group_labels, bin_size=[.1, .25, .5])


# >>> # Create distplot with custom bin_size
# >>> fig = ff.create_distplot(
# ...         hist_data, group_labels, bin_size=[.1, .25, .5])
# >>>
# >>> # Plot!
# >>> st.plotly_chart(fig, use_container_width=True)

        def best_book(df):
            st.markdown("")
            st.markdown("")
            st.subheader("The top 15 best Author ")
            st.markdown("")
            st.markdown("")
            df = data.sort_values(by='award', ascending=False).reset_index(
                drop=True).head(15)

            sns.barplot(x="award", y="author", data=df,
                        label='The best author who has more awards')

        ########################################################################################################
            # tthe side bar for visalization
        # filters = st.sidebar.radio(
        #     'Selection', ("The most awarded book", "The best Author", ))

        ######
        st.sidebar.markdown("Which Type of Graph do want?")
        np.select = st.sidebar.selectbox(
            "Graph type", ["Scatter plot", "Bar Chart", 'Histogram',  'Pie Chart'], key='1')
        if np.select == "Scatter plot":
            st.markdown(
                '- Create a 2D scatterplot with pages on the x-axis and num_ratings on the y-axis.')
            st.text(" ")
            scatter_2D_plot(data)
            st.pyplot()
###########################################################################
            # Bar Charts
        if np.select == "Bar Chart":

            group_bar_chart(data)
            st.pyplot()
            norm_functions(data)
            st.pyplot()
            best_book(data)
            st.pyplot()
###########################################################################

#############################################################################

#########################################################################################


###########################################################

################################################################################################################################

###########################################################################################################

###########################################################################################################


main()
