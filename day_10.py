import yfinance as yf
ticker= yf.Ticker('AAPL')

# print(ticker.info['fullTimeEmployees'])
# print(ticker.analyst_price_targets)
# print(ticker.quarterly_balance_sheet)
# print(ticker.news)
# print(ticker.calendar)
print(ticker.history(period='6d'))