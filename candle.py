import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots, draw
from matplotlib.finance import candlestick


df = pd.read_csv('tick', names=['Time', 'Price', 'Qty'], error_bad_lines=False, index_col=0)
df.index = pd.to_datetime((df.index.values*1e9).astype(int))
bars = df.Price.resample('D', how="ohlc")
volume = df.Qty.resample('D', how='sum')

barsa = bars.fillna(method='ffill')
fig = plt.figure()
fig.subplots_adjust(bottom=0.1)
ax = fig.add_subplot(111)
plt.title("Candlestick chart")
# value = ticks.prod(axis=1).resample('1min', how='sum')
# vwap = value / volume
Date = range(len(barsa))
print barsa
DOCHLV = zip(Date , barsa.open, barsa.close, barsa.high, barsa.low, volume)
candlestick(ax, DOCHLV, width=0.6, colorup='g', colordown='r', alpha=1.0)
plt.show()


