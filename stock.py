import pandas as pd
from pandas_datareader import data, wb
from pandas_datareader.data import Options
import pandas_datareader.data as web

import datetime
import time
sixty_days = datetime.date.today() - datetime.timedelta(days=60) #Need enough days for MACD calculation

def GetStockQuote( *args ):
    '''
        Read the stock quote by givn stock symbol, and the time frame.
    '''
    try:
        if len(args) == 1:  #default 60 days
            symbol = args[0]
            quote = web.get_data_yahoo(symbol,sixty_days.strftime("%m/%d/%Y"), time.strftime("%m/%d/%Y"))
        elif  len(args) == 2:   #can select days to today
            symbol = args[0]
            startdate = datetime.date.today() - datetime.timedelta(days=args[1]) #Need enough days for MACD calculation
            quote = web.get_data_yahoo(symbol,startdate.strftime("%m/%d/%Y"), time.strftime("%m/%d/%Y"))         
        elif len(args) == 3:  # symbol, start date, end date        
            symbol = args[0]
            startdate = datetime.date.today() - datetime.timedelta(days=args[1]) #Need enough days for MACD calculation
            enddate = datetime.date.today() - datetime.timedelta(days=args[2])            
            quote = web.get_data_yahoo(symbol,startdate.strftime("%m/%d/%Y"), enddate.strftime("%m/%d/%Y"))     
        return quote;    
    except Exception  as identifier:
        symbol = args[0]
        print("Cannot get the quote for ", symbol)
        return "NoQuote"
    

def GetStockSymbol(*args):
    '''
        Read the stock symbol from a file
        input:  filename
                the suffix of stock market, eg: .CO, .ST
        output : A list of symbols        
    '''
    filename = args[0]
    if (len(args) == 2):
        market = args[1]
    else:
        market = ".CO"
    symbols = []
    file = open(filename, 'r')
    for line in file:
        if line.rstrip():
            symbol = line.rstrip().replace(" ", "-") + market
            symbols.append(symbol) 
    return symbols