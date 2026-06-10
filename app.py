import streamlit as st
import yfinance as yf
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Set the page title
st.title("Market Sentiment Bot 🤖")

# Create an input box for the user to type the Ticker
ticker = st.text_input("Enter a stock ticker (e.g., AAPL, SSNLF):", "AAPL")

if st.button("Analyze"):
    # Reuse your existing pipeline logic here
    stock = yf.Ticker(ticker)
    price = stock.history(period="1d")['Close'].iloc[-1]
    
    st.write(f"### Current Price for {ticker}: ${price:.2f}")
    
    # Placeholder for headlines (or your API call)
    headlines = ["Strong growth for " + ticker, ticker + " faces market pressure"]
    analyzer = SentimentIntensityAnalyzer()
    data = [{'Headline': h, 'Sentiment': analyzer.polarity_scores(h)['compound']} for h in headlines]
    
    df = pd.DataFrame(data)
    st.write("### Sentiment Analysis Table")
    st.dataframe(df) # This turns your DataFrame into a pretty web table
    
    st.write(f"### Average Sentiment Score: {df['Sentiment'].mean():.2f}")