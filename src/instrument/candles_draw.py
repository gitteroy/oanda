import os
from oanda_candles import CandleClient, Pair, Gran
from accesstoken import TOKEN

# Initialize Client with token, real as False for practice account.
client = CandleClient(TOKEN, real=False)

# Initialize collector for Euro/US Dollar 4 hour candles.
collector = client.get_collector(Pair.EUR_USD, Gran.H4)

# Print the opening and closing bid price of the most recent 100 candles.
candles = collector.grab(100)
for candle in candles:
    print(f"{candle.time.get_pretty()}: Open bid: {candle.bid.o} Close bid: {candle.bid.c}")

# Get list of 300 candles from 8000 candles back
special_300 = collector.grab_offset(8000, 300)