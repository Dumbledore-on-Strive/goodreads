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
            "Graph type", ['Histogram', 'Pie Chart', "Scatter plot"], key='1')
        if np.select == "Scatter plot":
            st.markdown(
                '- Create a 2D scatterplot with pages on the x-axis and num_ratings on the y-axis.')
            st.text(" ")
            data = load_data("clean")

            def scatter_2D_plot(data):
                # fig, ax = plt.subplots()
                # ax.scatter([1, 2, 3], [1, 2, 3])
                size_b = data['award']**2*12
                colors = np.random.rand(df.shape[0])
                sns.scatterplot(data['num_pages'], data['num_rating'],
                                s=size_b, c=colors, alpha=0.5, legend=True)
            scatter_2d = scatter_2D_plot(data)
            st.pyplot(scatter_2d)

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
            "Min-Max Normalization vs Mean Normalisation vs before Normalization Distrubtion\n")
        st.markdown("")
        sns.histplot(data, x="avg_rating", color="green",
                     label="Before Normalization", kde=True)
        sns.histplot(data, x="minmax_norm_ratings", color="skyblue",
                     label="Min-Max Normalization", kde=True)
        sns.histplot(data, x="mean_norm_ratings", color="red",
                     label="Mean Normalization", kde=True)
        sns.set(rc={'figure.figsize': (7, 8)})

        st.pyplot()
###########################################################################################################
        d_f = data.sort_values(
            by='award', ascending=False).reset_index(drop=True).head(15)
        g = sns.countplot(y=d_f['award'], order=d_f['author'])
        g.set_ylabel('authers')
        g.set_title('The Top 15 Authors ')
        st.pyplot
###########################################################################################################
   # sns.histplot(data=df, y="award", color="red", label="the top most awards have ")
#     sns.barplot(x="award", y="author", data=df,
#                 label='The best author who has more awards')
#     plt.legend()
#     plt.show()
# best_book(best)


main()
