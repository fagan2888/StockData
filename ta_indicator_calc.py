import numpy as numpy
import talib as ta

def rsi ( quote ):    
    rsi = ta.RSI(numpy.array(quote))
    return rsi[-1];
    
def macd ( quote ):
    macddiv, macdsignal, macdhist = ta.MACD(numpy.array(quote), fastperiod=12, slowperiod=26, signalperiod=9)        
    return macddiv, macdsignal, macdhist;

def macd_dif ( quote ):
    '''
        calculate the difference between MACD and MACD signal. also based on their value, give the judgement of bullish or bearish market        
    '''
    macddiv, macdsignal, macdhist = macd(quote)
    diff = macddiv - macdsignal
    if (macddiv[-1] >0 and macdsignal[-1] >0):
        pos = 1
    elif (macddiv[-1] <0 and macdsignal[-1] <0):
        pos = -1
    elif (macddiv[-1] >0 and macdsignal[-1] <0):
        pos = 0.5 * min(2, (macddiv[-1] - macdsignal[-1]))
    else:
        pos = 0        
    return diff, pos;
    
def J ( quote ):
    STOCH_K, STOCH_D = ta.STOCH(numpy.array(quote.High), numpy.array(quote.Low), numpy.array(quote.Close),slowk_period=14,slowd_period=3)
    j = 3 * STOCH_K - 2 * STOCH_D
    return j[-1];