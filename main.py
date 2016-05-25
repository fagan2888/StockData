#Get the main flow. 

#Defin the symbols

symbols = ['SIM.CO','GEN.CO', 'AAPL']

# Get the stock quote 


from stock import GetStockQuote
import ta_indicator_calc as ind_calc
#from ta_indicator_calc import rsi
for symbol in symbols:
    quote = GetStockQuote(symbol)
    print(symbol)
    rsi_today = ind_calc.rsi(quote.Close)
    macd_diff = ind_calc.macd_dif(quote.Close)
    print(macd_diff)
    
    
    
    