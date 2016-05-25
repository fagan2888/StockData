

##############################################################################
#
# An example of converting a Pandas dataframe with stock data taken from the
# web to an xlsx file with a line chart using Pandas and XlsxWriter.
#
# Copyright 2013-2016, John McNamara, jmcnamara@cpan.org
#

import pandas as pd
import numpy as numpy

#import pandas.io.data as web
from pandas_datareader import data, wb
from pandas_datareader.data import Options
import pandas_datareader.data as web

import talib as ta
import matplotlib.pyplot as plt

##Own test
#from pandas.io.data import Options
print(ta.get_functions())

close = numpy.random.random(100)
#print(ta.SMA(close))

import time
import datetime
thirty_days = datetime.date.today() - datetime.timedelta(days=30)
def GetStockQuote(symbol) :
    quote = web.get_data_yahoo(symbol,thirty_days.strftime("%m/%d/%Y"), time.strftime("%m/%d/%Y"))
    return quote

#from talib import MA_Type
from talib import MA_Type
upper, middle, lower = ta.BBANDS(close, matype=MA_Type.T3)

# Own test end

aapl = web.get_data_yahoo("GEN.CO",'1/1/2016', '5/20/2016')
#appl = web.get_data_google("GEN",'1/1/2016', '5/20/2016')
#print(aapl.Close) # get all close price

print(numpy.array(aapl.Close))
#closeprice = ta.SMA(numpy.array(aapl.Close)) # Avoid Argument 'real' has incorrect type (expected numpy.ndarray, got Series) error. 
sma = ta.SMA(numpy.array(aapl.Close))
print(sma)
rsi = ta.RSI(numpy.array(aapl.Close))
print(rsi)

macddiv, macdsignal, macdhist = ta.MACD(numpy.array(aapl.Close), fastperiod=12, slowperiod=26, signalperiod=9)

cross = macdsignal - macddiv

print("MACD cross is ")
print(cross)

 


print("stop")

aapl = Options('aapl', 'yahoo')
data = aapl.get_all_data()
data.iloc[0:5, 0:5]

#MyYahoo = web.yahoo.quotes.YahooQuotesReader('AAPL', '5/1/2014', '5/2/2014')
#MyYahoo = web.yahoo.quotes('AAPL', '5/1/2014', '5/2/2014')

print ("AAPL is " + MyYahoo )

# Create some sample data to plot.
all_data = {}
for ticker in ['AAPL', 'GOOGL', 'IBM', 'YHOO', 'MSFT']:
    all_data[ticker] = web.get_data_yahoo(ticker, '5/1/2014', '5/1/2015')

# Create a Pandas dataframe from the data.
df = pd.DataFrame({tic: data['Adj Close']
                   for tic, data in all_data.items()})

# Create a Pandas Excel writer using XlsxWriter as the engine.
sheet_name = 'Sheet1'
writer     = pd.ExcelWriter('pandas_chart_stock.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name)

# Access the XlsxWriter workbook and worksheet objects from the dataframe.
workbook  = writer.book
worksheet = writer.sheets[sheet_name]

# Adjust the width of the first column to make the date values clearer.
worksheet.set_column('A:A', 20)

# Create a chart object.
chart = workbook.add_chart({'type': 'line'})

# Configure the series of the chart from the dataframe data.
max_row = len(df) + 1
for i in range(len(['AAPL', 'GOOGL'])):
    col = i + 1
    chart.add_series({
        'name':       ['Sheet1', 0, col],
        'categories': ['Sheet1', 2, 0, max_row, 0],
        'values':     ['Sheet1', 2, col, max_row, col],
        'line':       {'width': 1.00},
    })

# Configure the chart axes.
chart.set_x_axis({'name': 'Date', 'date_axis': True})
chart.set_y_axis({'name': 'Price', 'major_gridlines': {'visible': False}})

# Position the legend at the top of the chart.
chart.set_legend({'position': 'top'})

# Insert the chart into the worksheet.
worksheet.insert_chart('H2', chart)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
