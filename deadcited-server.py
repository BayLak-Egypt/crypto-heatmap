import yfinance as yf
symbols = ["BTC-USD", "ETH-USD", "SOL-USD", "BNB-USD", "XRP-USD", "ADA-USD", "DOGE-USD", "DOT-USD"]
for symbol in symbols:
    ticker = yf.Ticker(symbol)
    info = ticker.info
    print(f"Found: {info.get('shortName', 'Unknown')} | Current Price: {info.get('regularMarketPrice', 'N/A')}")
