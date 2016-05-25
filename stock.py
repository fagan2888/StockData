import pandas as pd
from pandas_datareader import data, wb
from pandas_datareader.data import Options
import pandas_datareader.data as web

import datetime
import time
thirty_days = datetime.date.today() - datetime.timedelta(days=30)

def GetStockQuote( symbol ):
    quote = web.get_data_yahoo(symbol,thirty_days.strftime("%m/%d/%Y"), time.strftime("%m/%d/%Y"))
    return quote;

