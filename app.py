import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np
from PIL import Image
import plotly.express as px
import plotly.figure_factory as ff


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
    menu = ["Home", "Data Visualisation", "Business Analysis"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":

        ####################################################
        header = st.beta_container()
        team = st.beta_container()
        activities = st.beta_container()
        github = st.beta_container()

        ####################################################
        with header:
            st.title('Dumbledore on Strive!')  # site title h1
            st.text(' ')
            st.markdown(
                "Enjoy the journey and you'll see the magic :sparkles:")
            st.text(' ')
            st.markdown(
                '* **Webscraping:** get the information (data) from the web')
            st.markdown('* **Dataframe:** add the data a spreadsheet file')
            st.markdown(
                '* **Plot:** create plot and graphs for better visualization')
            st.text(' ')
            image = Image.open('imgs/dumbledore-on-strive.jpeg')
            st.image(image, caption="'It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.'")
            st.text(' ')
            with team:
                # meet the team button
                # if st.button("Meet the team"):
                st.header('Team')
                col1, col2, col3, col4 = st.beta_columns(4)
                with col1:
                    image = Image.open('imgs/fabio.jpeg')
                    st.image(image, caption="")
                    st.markdown(
                        '[Fabio Fistarol](https://github.com/fistadev)')
                with col2:
                    image = Image.open('imgs/agathiya.jpeg')
                    st.image(image, caption="")
                    st.markdown(
                        '[Agathiya Raja](https://github.com/AgathiyaRaja)')
                with col3:
                    image = Image.open('imgs/dumbledore-on-strive.jpeg')
                    st.image(image, caption="")
                    st.markdown(
                        '[Camelia Ignat](https://github.com/avocami)')
                with col4:
                    image = Image.open('imgs/nurlan.jpeg')
                    st.image(image, caption="")
                    st.markdown(
                        '[Nurlan Sarkhanov](https://github.com/nsarkhanov)')
                st.text(' ')
                st.text(' ')

        with activities:
            # activities section:
            st.header('Activities')
            st.markdown('* Webscraping')
            st.markdown('* Data Visualisation')
            st.markdown('* Data Analysis ')
            st.markdown('* Analising Business Scenario')
            st.text(' ')

        with github:
            # github section:
            st.header('GitHub / Instructions')
            st.markdown(
                'Check the instruction [here](https://dumbledore-on-strive.github.io/)')
            st.text(' ')


##########################################################################
    elif choice == "Data Scrapping":
        st.subheader("Data Processing")
        data = load_data('raw')
        header = st.beta_container()
        dataset = st.beta_container()
        conclusion = st.beta_container()
        with dataset:
            st.header("1000 books data frame from scrapper")
            book_data = load_data("raw")
            st.write(book_data.head(10))

    elif choice == "Business Analysis":
        st.subheader("Business Analysis")
        conclusion = st.beta_container()
        footer = st.beta_container()

        with conclusion:
            st.title('Time to invest money')
            st.text(' ')
            st.subheader("94.9% of the books are series")
            st.text('This can be a great opportunity to release a Netflix series')
            # st.text('This can be a great opportunity to release a Netflix series')
            st.text(' ')
            st.text(' ')

            st.header('Most watched Netflix movies/series based on books')
            # st.subheader('More than 20 million views')
            st.text(' ')

            st.text(' ')
            st.markdown('* Bridgerton (The Duke And I)')
            st.markdown("* The Queen's Gambit")
            st.markdown('* Tiny Pretty Things')
            st.markdown('* Lupin')
            st.markdown('* The Last Kingdom')
            st.markdown('* The Haunting of Hill House')
            st.markdown('* A Series of Unfortunate Events')
            st.markdown("* To All the Boys I've Loved Before")
            st.markdown("* 1922")
            st.markdown('* The Little Prince')
            st.markdown("* Gerald's Game")
            st.markdown('* The Boy Who Harnessed the Wind')
            st.text('')
            st.text(' ')
            st.text(' ')

            st.header('Best Movies adaptations based on Books of all time')
            st.subheader(
                'All have more than 4.5 average rating on Goodreads')
            st.markdown(
                'All these Movies had a gross income above $50M on the first month after release')
            st.text(' ')
            # image = Image.open('imgs/nurlan.jpeg')
            # st.image(image, caption="")
            st.text(' ')
            st.markdown('* The Godfather (1972) | Gross: $134.97M')
            st.markdown('* The Shawshank Redemption | Gross: $28.34M')
            st.markdown('* The Lord of the Rings(2001) | Gross: $315.54M')
            st.markdown('* The Green Mile (1999) | Gross: $136.80M')
            st.markdown(
                '* Harry Potter and the Half-Blood Prince (2009) | Gross: $301.96M')
            st.markdown(
                '* Charlie and the Chocolate Factory (2005) | Gross: $206.46M')
            st.markdown('* The Silence of the Lambs (1991) | Gross: $130.74M')
            st.markdown('* The Shining (1980) | Gross: $44.02M')
            st.markdown('* Dances with Wolves (1990) | Gross: $184.21M')
            st.markdown('* Forrest Gump (1994) | Gross: $330.25M')
            st.markdown('* Alice in Wonderland')
            st.markdown('* The Da Vinci Code')
            st.markdown('* The Wonderful Wizard of Oz')
            st.markdown('* Romeo and Juliet')
            st.text('')
            st.text(' ')
            st.text(' ')

            st.header('The Top 5 Best Authors to invest in 2021')
            st.subheader(
                'Based on average rating')
            st.text(' ')
            # image = Image.open('imgs/nurlan.jpeg')
            # st.image(image, caption="")
            st.text(' ')
            st.markdown('* Rainbow Rowell')
            st.markdown('* Scott Westerfeld')
            st.markdown('* Neil Gaiman')
            st.markdown('* Kristin Cashore')
            st.markdown('* Mark Haddon')
            st.text('')
            st.text('')
            st.text(' ')
            st.text(' ')

        with footer:
            # Footer
            st.markdown(
                "If you have any questions, checkout our [documentation](https://dumbledore-on-strive.github.io/) ")
            st.text(' ')
            # Add audio

            audio_file = open('data/money.mp3', 'rb')
            audio_bytes = audio_file.read()

            st.audio(audio_bytes, format='audio/ogg')

        ############################################################################################################################
    else:
        st.header("Data Visualisation")
        data = load_data("clean")
        # the all graphic functions
        #  Scatter plots

        def scatter_2D_plot(data):
            st.markdown("")
            st.markdown("")
            st.subheader("Comparison between Number of rating and Awards")
            st.markdown("")
            st.markdown("")
            size_b = data['award']**2*12
            colors = np.random.rand(data.shape[0])
            sns.scatterplot(data['num_pages'], data['num_rating'],
                            s=size_b, c=colors, alpha=0.5, legend=True)

        def group_bar_chart(data):
            st.markdown("")
            st.markdown("")
            st.subheader("The Published Books by Year ")
            st.markdown("")
            st.markdown("")
            tmp = data.groupby("original_publish_year")[
                "award"].mean().sort_values()
            st.bar_chart(tmp)

        def norm_functions(data):
            st.markdown("")
            st.markdown("")
            st.subheader(
                "Average Rating Analysis")
            st.markdown("")

            x1 = data["minmax_norm_ratings"]
            x2 = data["mean_norm_ratings"]
            x3 = data["avg_rating"]
            hist_data = [x1, x2, x3]
            group_labels = ['Min-Max Normalization',
                            'Mean Normalization', 'Before Normalization Avarge rate']

            fig = ff.create_distplot(hist_data, group_labels, bin_size=0.1)
            st.plotly_chart(fig, use_container_width=True)

        def best_book(df):
            st.markdown("")
            st.markdown("")
            st.subheader(
                "The top 15 Best Author")
            st.markdown("")
            st.markdown("")
            df = data.sort_values(by='award', ascending=False).reset_index(
                drop=True).head(15)

            sns.barplot(x="award", y="author", data=df,
                        label='The best author who has more awards')

        # agg_bar_graph
        # def agg_bar_graph(df):
        #     st.markdown("")
        #     st.markdown("")
        #     st.subheader("Comparison between Awards and Year")
        #     st.markdown("")
        #     st.markdown("")
        #     df.groupby('original_publish_year')['award'].agg('max', 'mean').plot(
        #         kind='bar', color=['r', 'pink'], legend='', figsize=(25, 5))
        #     plt.legend(loc='best')
        #     plt.xlabel("original_publish_year ")
        #     plt.ylabel("Total awards")
        #     plt.title("Aggregation plot for awards")
        #     plt.show()

        ######
        st.sidebar.markdown("Which Type of Graph do want?")
        np.select = st.sidebar.selectbox(
            "Graph type", ["Number of rating and Awards", "The top 15 best author", 'Award and Year', "Average Rating Analysis", 'The published books by year',  "Who is the Best Author"], key='1')
        if np.select == "Number of rating and Awards":
            # st.markdown(
            #     '- Create a 2D scatterplot with pages on the x-axis and num_ratings on the y-axis.')
            st.text(" ")
            scatter_2D_plot(data)
            st.pyplot()
        ################################################
            # Bar Charts
        if np.select == "The top 15 best author":
            best_book(data)
            st.pyplot()
            # group_bar_chart(data)
            # st.pyplot()

        ################################################
        if np.select == "Award and Year":
            agg_bar_graph(data)
            st.pyplot()

        ################################################
        if np.select == "Average Rating Analysis":
            norm_functions(data)
            st.pyplot()

        ################################################
        if np.select == "The published books by year":
            group_bar_chart(data)

        ################################################
        if np.select == "Who is the Best Author":
            group_bar_chart(data)


main()
