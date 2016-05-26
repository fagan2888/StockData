#Get the main flow. 
'''
https://cryptotrader.org/talib

TODO:
Implement the volumn detect
Implement ADX and DI check
'''
#Defin the symbols
from recommendation import CleanRecommendation
CleanRecommendation("today_recommendation_to_buy.txt")
CleanRecommendation("today_recommendation_to_sell.txt")


from stock import GetStockSymbol
# Get the stock quote
symbols = GetStockSymbol("stocklist.txt") +  GetStockSymbol("stocklist_sto.txt", ".ST")
#symbols = ['GEN.CO', 'SIM.CO']

from stock import GetStockQuote
import ta_indicator_calc as ind_calc
from recommendation import GetRecommendation
from recommendation import WriteRecommendation

#from ta_indicator_calc import rsi

for symbol in symbols:
    quote = GetStockQuote(symbol)
    print(symbol)
    
    if not(isinstance(quote, str)):         
        rsi_today = ind_calc.rsi(quote.Close)
        macd_diff, macd_pos = ind_calc.macd_dif(quote.Close)   
        j = ind_calc.J(quote)
        quote_lastday = GetStockQuote(symbol,1)
        if not(isinstance(quote_lastday, str)):
            rec = GetRecommendation(rsi_today,macd_diff,macd_pos, j, quote_lastday)  
            print("Final recommendation of ", symbol , " is ", rec)             
        else:
            print("No last day quote, no recommendation.")        
            rec = 0
        
        
        
        if (rec > 2):
            WriteRecommendation(symbol, rec, "today_recommendation_to_buy.txt")
        elif (rec<=-2):
            WriteRecommendation(symbol, rec, "today_recommendation_to_sell.txt")
        
    else:
        print("No Quote for ", symbol)
