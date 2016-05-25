import pandas as pd
from pandas_datareader import data, wb
from pandas_datareader.data import Options
import pandas_datareader.data as web

import datetime
import time
sixty_days = datetime.date.today() - datetime.timedelta(days=60) #Need enough days for MACD calculation

def GetStockQuote( symbol ):
    quote = web.get_data_yahoo(symbol,sixty_days.strftime("%m/%d/%Y"), time.strftime("%m/%d/%Y"))
    return quote;

