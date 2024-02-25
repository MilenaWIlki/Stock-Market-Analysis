import yfinance as yf

def get_stock_data(symbol):
    data = yf.download(symbol, start='2023-01-01', end='2023-12-31')
    return data

# Example usage:
stock_data = get_stock_data('AAPL')
print(stock_data.head())
