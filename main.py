#Get the main flow. 

#Defin the symbols

symbols = ['SIM.CO','GEN.CO', 'AAPL']

# Get the stock quote 


from stock import GetStockQuote
from ta_indicator_calc import rsi
for symbol in symbols:
    quote = GetStockQuote(symbol)
    print(symbol)
    rsi_today = rsi(quote.Close)
    print(rsi_today)
    
    
    
    
    