import numpy as numpy
import talib as ta
import Helpers as helper

def rsi ( quote ):    
    rsi = ta.RSI(numpy.array(quote))
    return rsi[-1];
    
def macd ( quote ):
    '''
    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_convergence_divergence_macd
    MACD Line: (12-day EMA - 26-day EMA)
    Signal Line: 9-day EMA of MACD Line
    MACD Histogram: MACD Line - Signal Line
    '''
    macddiv, macdsignal, macdhist = ta.MACD(numpy.array(quote), fastperiod=12, slowperiod=26, signalperiod=9)            
    return macddiv, macdsignal, macdhist;

def macd_dif ( quote ):
    '''
        calculate the difference between MACD and MACD signal. also based on their value, give the judgement of bullish or bearish market        
    '''
    macddiv, macdsignal, macdhist = macd(quote)
    if (macddiv[-1] >0 and macdsignal[-1] >0):
        pos = 1
    elif (macddiv[-1] <0 and macdsignal[-1] <0):
        pos = -1
    elif (macddiv[-1] >0 and macdsignal[-1] <0):
        pos = 0.5 * min(2, (macddiv[-1] - macdsignal[-1]))
    else:
        pos = 0        
    return macdhist, pos;
    
def J ( quote ):
    STOCH_K, STOCH_D = ta.STOCH(numpy.array(quote.High), numpy.array(quote.Low), numpy.array(quote.Close),slowk_period=14,slowd_period=3)
    j = 3 * STOCH_K - 2 * STOCH_D
    return j[-1];
    
    
def ADX ( quote ) :  
    '''
    Calculate the ADX and its trend (trend calculated by use SMA)
    '''
    high = numpy.array(quote.High)
    low = numpy.array(quote.Low)
    close = numpy.array(quote.Close)
    adx = helper.RemoveNaN(ta.ADX(high, low, close))
    adx_trend = helper.RemoveNaN(ta.SMA(adx))
    
    #print("ADX is ", adx)
    #print("ADX Trend is ", adx_trend)
    return adx, adx_trend
    
def ADXR (quote):
    '''
    Calculate the ADXR and its trend (trend calculated by use SMA)
    '''
    high = numpy.array(quote.High)
    low = numpy.array(quote.Low)
    close = numpy.array(quote.Close)
    #ADXR is (adx + adx_previous)/2, but not in talib, where ADXR is unknown.
    #https://www.linnsoft.com/techind/adxr-avg-directional-movement-rating
    adxr = helper.RemoveNaN(ta.ADXR(high, low, close))    
    #adxr_trend = helper.RemoveNaN(ta.SMA(adxr))
    #print("ADXR is ", adxr)
    #print("ADXR Trend is ", adxr_trend)
    return adxr

def BullBearPower(quote):
    '''
    Calculate the Bullpower and bearpower
    '''     
    close = numpy.array(quote.Close)         
    ema13 = helper.RemoveNaN(ta.EMA(close, timeperiod=13))            
    
    high =  numpy.array(quote.High)[-(len(ema13)+1) :-1]   
    low =  numpy.array(quote.Low)[-(len(ema13)+1) :-1]   
    
    bullpower = high - ema13
    bearpower = low - ema13
    
    print(bullpower)
    print(bearpower)
    return bullpower, bearpower
    

def Minus_DI (quote) : 
    '''
    Calculate -DI
    '''
    
    minus_di = ta.MINUS_DI(numpy.array(quote.High), numpy.array(quote.Low), numpy.array(quote.Close), timeperiod=14)
    
    return minus_di 
    
def Plus_DI (quote) : 
    '''
    Calculate +DI
    '''
    
    plus_di = ta.PLUS_DI(numpy.array(quote.High), numpy.array(quote.Low), numpy.array(quote.Close), timeperiod=14)
    
    return plus_di 
    
        