import yfinance as yf
import matplotlib.pyplot as plt 


symbol = input("Entrez le symbole boursier (ex : AAPL, TSLA, BTC-USD)")
data = yf.download(symbol,start="2024-01-01", end="2025-01-01")

data['MA20'] = data['Close'].rolling(window=20).mean()

plt.figure(figsize=(12,6))
plt.plot(data['Close'],label='Prix Cloture')
plt.plot(data['MA20'],label='Moyenne des prix 20j')
plt.title(f'prix d{symbol}')
plt.xlabel('Date')
plt.ylabel('Prix')
plt.legend()
plt.show()