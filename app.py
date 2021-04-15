import yfinance as yf
import streamlit as st
import pandas as pd
st.write(""" 

# simple Stock Price App

Shown are the stock closing price and volume of Google 

""")
tickerSymbol = 'Google'
tickerData = yf.ticker(tickerSymbol)

tickerDf = tickerData
