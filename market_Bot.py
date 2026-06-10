# import yfinance as yf
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import nltk
# import requests 
# from bs4 import BeautifulSoup
# # print("Testing yfinance...")
# # ticker="AAPL"
# # data=yf.Ticker(ticker)
# # price= data.history(period="1d")['Close'].iloc[-1]
# # print("Successfully connected to "+ ticker+ "Current price: "+str(round(price,2)))

# # print("\nTesting NLTK sentiment...")
# # nltk.download('vader_lexicon')
# # analyzer=SentimentIntensityAnalyzer()
# # text="The stock market is growing rapidly and making great profits!"
# # score=analyzer.polarity_scores(text)
# # print("Sentiment Analysis Test (Compound Score): "+ str(score['compound']))

# # url="https://finance.yahoo.com/quote/AAPL/news"
# # response=requests.get(url)
# # soup=BeautifulSoup(response.text, 'html.parser')

# # # for all headlines
# # headlines=soup.find_all('h3')
# # for h in headlines:
# #     print(h.text)
# # defining agent to look like browser
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT10.0; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/120.0.0 Safari/537.36"
# }
# url="https://finance.yahoo.com/quote/AAPL/news"

# # now passing the headers into the requsts
# response=requests.get(url, headers=headers)
# soup=BeautifulSoup(response.text, 'html.parser')

# # looking for titles
# headlines= soup.find_all('h3')
# # for h in headlines:
# #     if h.text.strip():
# #         print(h.text.strip())
# print(soup.text[:500])




import yfinance as yf
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# # 1. Setup the Sentiment Analyzer
# nltk.download('vader_lexicon', quiet=True)
# analyzer = SentimentIntensityAnalyzer()

# # 2. Get the Price
# ticker = "AAPL"
# stock = yf.Ticker(ticker)
# price = stock.history(period="1d")['Close'].iloc[-1]
# print(f"Current Price for {ticker}: {price:.2f}")

# # 3. Simulated News Headlines (We use these because live scraping is blocking)
# headlines = [
#     "Apple revenue grows significantly this quarter",
#     "Investors worried about Apple's new product launch",
#     "Apple stock hits an all-time high amidst strong demand",
#     "Lawsuit filed against Apple for privacy concerns"
# ]

# # 4. Analyze Sentiment
# data = []
# for h in headlines:
#     score = analyzer.polarity_scores(h)['compound']
#     data.append({'Headline': h, 'Sentiment': score})

# # 5. Display as a Table
# df = pd.DataFrame(data)
# print("\nNews Sentiment Analysis:")
# print(df)

# # 6. Simple calculation: Average sentiment
# avg_sentiment = df['Sentiment'].mean()
# print(f"\nAverage Market Sentiment Score: {avg_sentiment:.2f}")

# import matplotlib.pyplot as plt
# import seaborn as sns

# # 7. Get recent stock history for plotting
# stock_history = stock.history(period="1mo")

# # attach dates to the sentiment dataframe (use last N days)
# dates = stock_history.index[-len(df):]
# df['Date'] = dates

# # 1. Setup the figure
# fig, ax1 = plt.subplots(figsize=(12, 6))

# # 2. Plot Stock Price on the left axis
# ax1.plot(stock_history.index, stock_history['Close'], color='blue', label='Stock Price')
# ax1.set_xlabel('Date')
# ax1.set_ylabel('Price ($)', color='blue')

# # 3. Create a second y-axis for Sentiment
# ax2 = ax1.twinx()
# ax2.bar(df['Date'], df['Sentiment'], color='red', alpha=0.3, label='Sentiment')
# ax2.set_ylabel('Sentiment Score', color='red')

# # 4. Final touches
# plt.title(f"{ticker} Price vs. News Sentiment")
# fig.tight_layout()
# plt.show()


import requests
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_live_news(ticker_name, api_key):
    # This URL connects to the live NewsAPI servers
    url = f"https://newsapi.org/v2/everything?q={ticker_name}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    
    # Extract only the headlines
    headlines = [article['title'] for article in data['articles']]
    return headlines

# --- MAIN ENGINE ---
API_KEY = "e2d005e0bf0a443aa12d3a0a359f2cbe" # Put your key from the website here
ticker = "Samsung"

# Get live news and run the same sentiment pipeline
headlines = get_live_news(ticker, API_KEY)
analyzer = SentimentIntensityAnalyzer()
data = [{'Headline': h, 'Sentiment': analyzer.polarity_scores(h)['compound']} for h in headlines]

df = pd.DataFrame(data)
print(f"Live Sentiment for {ticker}: {df['Sentiment'].mean():.2f}")
print(df.head())
# e2d005e0bf0a443aa12d3a0a359f2cbe