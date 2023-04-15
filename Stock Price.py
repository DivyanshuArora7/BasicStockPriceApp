import yfinance as yf
import streamlit as st

st.write("""
Basic Stock Price App
======
> ### Shown are the stock **closing price** and **volume** of Amazon.com
> [Amazon.com](https://www.amazon.com)
""")

#  Source: https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
#You can change the tickerSymbol(We used 'AMZN' here)(Search on Google for tickerSymbols of different companies like Apple)
tickerSymbol = 'AMZN'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
st.write("""
> #### PROJECT BY: **DIVYANSHU ARORA**
""")
