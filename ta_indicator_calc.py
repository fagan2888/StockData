import numpy as numpy
import talib as ta

def rsi ( quote ):
    print(quote)
    rsi = ta.RSI(numpy.array(quote))
    return rsi[-1];
    
def macd ( quote ):
    macddiv, macdsignal, macdhist = ta.MACD(numpy.array(quote), fastperiod=12, slowperiod=26, signalperiod=9)
    return macddiv, macdsignal, macdhist;
    
    
def K ( quote ):
       
    
'''
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

 
'''