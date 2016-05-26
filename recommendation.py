import pandas as pd
import time

def GetRSIRecommendation( rsi ):
    if (rsi < 30):
        rec = 1
    elif (rsi>70):
        rec = -1  
    else:
        rec = 0
    print("RSI is ", rsi, " and recommendation is ", rec)    
    return rec;
       
def GetKDJRecommendation( j ):
    if (j < 20):
        rec = 1
    elif (j > 80):
        rec = -1  
    else:
        rec = 0
    print("J is ", j, " and recommendation is ", rec)
    return rec;
    
import numpy as numpy

def GetMACDRecommendation( diff ):
    if (diff[-3] <=0) and (diff[-2] <= 0) and (diff[-1] > 0):  
        macd_cross = 1 
    elif (diff[-3] >0) and (diff[-2] > 0) and (diff[-1] <= 0):
        macd_cross = -1
    else:
        macd_cross = 0
    print("macd recommendation is ", macd_cross)    
    return macd_cross; 

def GetCandleRecommendation( quote ):
    open = quote.Open.apply(pd.to_numeric, errors='coerce')
    high = quote.High.apply(pd.to_numeric, errors='coerce')
    close = quote.Close.apply(pd.to_numeric, errors='coerce')
    low = quote.Low.apply(pd.to_numeric, errors='coerce')    
    
    if (open.item() < close.item()):
        upper = high.item() - close.item()
        lower = open.item() - low.item()
        candle = close.item() - open.item()  
        candle_list = [upper, candle, lower]
                
        if max(candle_list) == candle:   
            rec = 3
        elif (max(candle_list) == lower) and (lower / (upper+0.0001) > 1.5):
            rec = 2
        elif (max(candle_list) == upper) and (upper / (lower+0.0001) > 1.5):
            rec = 1
        else:
            rec = 0         
    else:
        upper = high.item() - open.item()
        lower = close.item() - low.item()
        candle = open.item() - close.item()
        candle_list = [upper, candle, lower]
        
        if max(candle_list) == candle:   
            rec = -3
        elif (max(candle_list) == upper) and (upper / (lower+0.0001) > 1.5):
            rec = -2
        elif (max(candle_list) == lower) and (lower / (upper+0.0001) > 1.5):
            rec = -1
        else:
            rec = 0       
    print("Candle recommendation is ", rec)
    return rec;

def GetRecommendation(rsi, macd, kdj, quote):
    rsi_r = GetRSIRecommendation(rsi)
    macd_r = GetMACDRecommendation(macd)
    kdj_r = GetKDJRecommendation(kdj)
    candle_r = GetCandleRecommendation(quote)
    
    recommendation = rsi_r + kdj_r + macd_r + candle_r * 1 / 3
    return recommendation        
    
    
def WriteRecommendation(symbol, rec, filename):
    ''' 
    If recommendation larger than 2, write to a text file
    '''     
    file = open(filename, 'a')
    line = time.strftime("%Y/%m/%d") + "\t" + symbol + " has the recommendation of "  + str(rec) + "\n"
    file.writelines(line)
    file.close()
    
def CleanRecommendation(filename):
    file = open(filename, 'w')
    file.close()