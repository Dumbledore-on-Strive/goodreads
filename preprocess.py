
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def minmax_norm(data_column_name):
    x = data_column_name
    mean_norm_ratings = 1+((x-x.min())/(x.max()-x.min()))*9
    return mean_norm_ratings


# Mean normalization
def mean_norm(data_column_name):
    x = data_column_name
    mean_norm_ratings = 1+((x-x.mean())/(x.max()-x.min()))*9
    return mean_norm_ratings


def preprocess():

    df = pd.read_csv("goodreads_1000_books_list.csv")
    df = df.drop(['Unnamed: 0', 'place', 'url'], axis=1)
    df['num_pages'] = pd.to_numeric(df['num_pages'], downcast='integer')

    df['minmax_norm_ratings'] = minmax_norm(
        df['avg_rating']).round(decimals=2)  # little problem

    a = mean_norm(df["avg_rating"])
    a.to_frame()

    df['mean_norm_ratings'] = mean_norm(df['avg_rating']).round(decimals=2)
    df.head()
    cols = df.columns.tolist()
    cols = cols[:8]+cols[-2:]+cols[8:-2]
    df = df[cols]
    df

    df.to_csv('preprocess_data.csv')

    # #                                                                            Analyse

    anay_goup = df.groupby("original_publish_year")[
        'minmax_norm_ratings'].mean().round(decimals=2)

    # In[63]:

    anay_goup.to_frame()

    # In[61]:

    anay_goup.to_frame()

    # #                                         The Best Book Author

    def get_book_author(name, df):
        f = df[df.loc[:, 'author'] == name]
        m = f['minmax_norm_ratings'].max()
        return m

    get_book_author('Cassandra Clare', df)
