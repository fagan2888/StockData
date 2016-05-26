import pandas as pd
from pandas_datareader import data, wb
from pandas_datareader.data import Options
import pandas_datareader.data as web

import datetime
import time
sixty_days = datetime.date.today() - datetime.timedelta(days=60) #Need enough days for MACD calculation

def GetStockQuote( *args ):
    try:
        if len(args) == 1:
            symbol = args[0]
            quote = web.get_data_yahoo(symbol,sixty_days.strftime("%m/%d/%Y"), time.strftime("%m/%d/%Y"))
        elif  len(args) == 2:
            symbol = args[0]
            back = datetime.date.today() - datetime.timedelta(days=args[1]) #Need enough days for MACD calculation
            quote = web.get_data_yahoo(symbol,back.strftime("%m/%d/%Y"), time.strftime("%m/%d/%Y"))         
        return quote;    
    except Exception  as identifier:
        symbol = args[0]
        print("Cannot get the quote for ", symbol)
        return "NoQuote"
    

def GetStockSymbol(filename):
    symbols = []
    file = open(filename, 'r')
    for line in file:
        if line.rstrip():
            symbol = line.rstrip() + ".CO"
            symbols.append(symbol) 
    return symbols