import streamlit as st
import pandas as pd
import yfinance as yf


st.write("""
         # My Stock Price App
         you can see the stocks ***closing price*** and ***volume*** of **Nifty 50** Stocks!
         
         """)

#define the ticker symbol

tickerSymbol = "^NSEI"

#get the data for this ticker

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = '1d', start = '2022-02-10', end = '2023-10-01')

# Open High Low Close Volume Dividends Stock Splits

st.write("""
         # Closing Value""")
st.line_chart(tickerDf.Close)

st.write("""
         # Volume""")
st.line_chart(tickerDf.Volume)

st.write("""
         # High Value""")
st.line_chart(tickerDf.High)

st.write("""
         # Low""")
st.line_chart(tickerDf.Low)