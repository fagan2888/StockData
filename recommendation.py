import pandas as pd
import time
import math

def GetRSIRecommendation( rsi ):   
    '''
        Use linear between the lower and upper limitation. 
    '''
    if (rsi < param.rsi_lower):
        rec = 1    
    elif (rsi>param.rsi_upper):
        rec = -1          
    else:
        rec = (rsi - param.rsi_lower) / (param.rsi_upper - param.rsi_lower) * -2  + 1         
    #print("RSI is ", rsi, " and recommendation is ", rec)    
    return rec;
       
def GetKDJRecommendation( j ):
    '''
        Use linear between the lower and upper limitation. 
    '''
    if (j < param.j_lower):
        rec = 1        
    elif (j > param.j_upper):
        rec = -1        
    else:
        rec = (j - param.j_lower) / (param.j_upper - param.j_lower) * -2  + 1
    #print("J is ", j, " and recommendation is ", rec)
    return rec;
    
import numpy as numpy
import parameters as param

def GetMACDRecommendation( diff, pos):
    ''' 
    Caclulate the recommendation from the MACD diff
    return : macd_cross, macd_pos        
    '''         
    if (diff[-3] <=0) and (diff[-2] <= 0) and (diff[-1] > 0):  
        macd_cross = 1   # Gold Cross           
    elif (diff[-3] >0) and (diff[-2] > 0) and (diff[-1] <= 0):
        macd_cross = -1  # Death cross
    elif (diff[-3] <=0) and (diff[-2] <= 0) and (diff[-1] <= 0):
        if  math.fabs(diff[-1]) >= math.fabs(diff[-3]) :
            macd_cross = -2   #diff increase in negitive side, the worst case
        elif math.fabs(diff[-1]) < math.fabs(diff[-3]):
            macd_cross = 0    #diff decrease in negitive side may turn to good.    
        else:
            macd_cross = -2    
    elif (diff[-3] >0) and (diff[-2] > 0) and (diff[-1] > 0):        
        if  diff[-1] >= diff[-3] : #difference increase in positive side, the best case
            macd_cross = 2  
        elif diff[-1] < diff[-3]:  #difference decrease in positive side, 
            macd_cross = 0        
        else:
            macd_cross = 1  #   
    else:
        macd_cross = 0
    
    #print("macd recommendation is ", macd_cross)       
    
    if pos == 1:
        pos_rec = 1
    elif pos <= 0:
        pos_rec = 0
    else:
        pos_rec = pos
    #print("macd position recommentdation is ", pos_rec)    
    return macd_cross, pos_rec; 

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
    macd_r, macd_pos = GetMACDRecommendation(macd, macd_pos)
    kdj_r = GetKDJRecommendation(kdj)
    #candle_r = GetCandleRecommendation(quote)
    
    indicator = macd_r
    confidence = macd_pos + (rsi_r + kdj_r) / 2
    
    recommendation = indicator * confidence 
    
    return recommendation, macd_r, macd_pos        
    
    
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