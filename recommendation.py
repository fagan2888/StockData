import pandas as pd
import time

def GetRSIRecommendation( rsi ):
    if (rsi < param.rsi_lower):
        rec = 1
    elif (rsi < param.rsi_2ndlower):
        rec = 0.5    
    elif (rsi>param.rsi_upper):
        rec = -1 
    elif (rsi > param.rsi_2ndupper):
        rec = -0.5     
    else:
        rec = 0
    print("RSI is ", rsi, " and recommendation is ", rec)    
    return rec;
       
def GetKDJRecommendation( j ):
    if (j < param.j_lower):
        rec = 1
    elif (j < param.j_2ndlower):
        rec = 1         
    elif (j > param.j_upper):
        rec = -1  
    elif (j > param.j_2ndupper):
        rec = -0.5  
    else:
        rec = 0
    print("J is ", j, " and recommendation is ", rec)
    return rec;
    
import numpy as numpy
import parameters as param

def GetMACDRecommendation( diff, pos):
    if (diff[-3] <=0) and (diff[-2] <= 0) and (diff[-1] > 0) and pos == 1:  
        macd_cross = 1   # Gold Cross,  both are positive,  Turn to Bullish
    if (diff[-3] <=0) and (diff[-2] <= 0) and (diff[-1] > 0) and pos != 1:  
        macd_cross = 0.5   # Gold cross, not both are positive Ready to Bullish    
    elif (diff[-3] >0) and (diff[-2] > 0) and (diff[-1] <= 0) and pos == 1:
        macd_cross = -0.5  # Death cross, both are positive, May to Bearish
    elif (diff[-3] >0) and (diff[-2] > 0) and (diff[-1] <= 0) and pos != 1:
        macd_cross = -1  # Death cross, not both are positive, Turn to Bearish,     
    elif (diff[-3] <=0) and (diff[-2] <= 0) and (diff[-1] <= 0) and pos !=1:  
        macd_cross = -1.5 # no cross, macd under signal, not both are positive, deep in a bearish market
    elif (diff[-3] <=0) and (diff[-2] <= 0) and (diff[-1] <= 0) and pos ==1:  
        macd_cross = 0.5 # no cross, macd under signal, both are positive, May turn to a bearish market     
    elif (diff[-3] >0) and (diff[-2] > 0) and (diff[-1] > 0) and pos == 1:
        macd_cross = 1.5  # no cross, macd over signal, both are positive, deep in Bullish market
    elif (diff[-3] >0) and (diff[-2] > 0) and (diff[-1] > 0) and pos != 1:
        macd_cross = -0.5  # no cross, macd over signal, not both are positive, may turn to a Bullish market    
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

def GetRecommendation(rsi, macd, macd_pos, kdj, quote):
    rsi_r = GetRSIRecommendation(rsi)
    macd_r = GetMACDRecommendation(macd, macd_pos)
    kdj_r = GetKDJRecommendation(kdj)
    candle_r = GetCandleRecommendation(quote)
    
    recommendation = rsi_r + kdj_r + macd_r + candle_r * 1/5
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