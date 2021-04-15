import yfinance as yf
import streamlit as st
import pandas as pd
st.write(""" 

# simple Stock Price App

Shown are the stock closing price and volume of Google 

""")
tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start='2010-5-31', end='2020-4-15')


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
