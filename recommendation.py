import pandas as pd
import time
import math

def GetRSIRecommendation( rsi ):   
    '''
        Use linear between the lower and upper limitation. 
    '''
    if (rsi < param.rsi_lower):
        rec = 1    
    elif (rsi > param.rsi_upper):
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
 
         
def GetADXRecommendation( adx, adx_trend):
    '''
    Get the recommendation from ADX indicator, and the trend of ADX (SMA of ADX)
    http://www.tradingsetupsreview.com/secret-using-adx-indicator/
    '''    
    if (adx[-1] >= 25):   
        #In Bullish market     
        if (adx[-2] < 25): 
            # Up-Cross: 25 line 
            if adx_trend[1] < adx_trend[-1] and max(adx_trend) == adx_trend[-1]:
                #indicate a strong rising , Strong Buy
                adx_rec = 2
            if adx_trend[1] < adx_trend[-1] :
                #indicate a possible rising , Buy
                adx_rec = 1
            else:          
                #undecisive, possible in the decrese trend. better to hold.
                adx_rec = 0
        else: 
            #Already in Bullish market
            if adx_trend[1] > adx_trend[-1] : 
                # Trend is down, sell signal.
                adx_rec = -1
            elif adx_trend[1] < adx_trend[-1] and max(adx_trend) == adx_trend[-1]:
                #still indicate a strong rising , but already in bullish market Buy
                adx_rec = 1     
            else:
                # Trend is still up, but not clear, hold now.
                adx_rec = 0                                     
    else:       
        # In berish market
        if adx[-2] >= 25:
            # Down Cross 25 line
            if adx_trend[1] > adx_trend[-1] and min(adx_trend) == adx_trend[-1]:
                #indicate a strong down treand , Strong sell
                adx_rec = -2
            elif adx_trend[1] > adx_trend[-1] :
                #indicate a possible down treand , sell
                adx_rec = -1    
            else:         
                #may in the wave, not clear trend, undecisive.          
                adx_rec = 0  
        else:
            #Already in bearish 
            if adx_trend[1] < adx_trend[-1] and max(adx_trend) == adx_trend[-1]:
                #indicate a strong rising now , buy
                adx_rec = 1           
            elif adx_trend[1] < adx_trend[-1] :
                #indicate a possible rising now , hold
                adx_rec = 0               
            else:
                # indicate in bearish market, and going down. Quit
                adx_rec = -2       
    return adx_rec    

def GetADXRRecommendation (adxr):
    '''
    Only conside the absolute value of ADX, but use ADXR to consider a bit trend. 
    Based on http://www.swing-trade-stocks.com/ADX-indicator.html
    '''
    if (adxr >= param.adxr_toohot):
        #too hot, sell
        adxr_r = -1
    elif (adxr >= param.adxr_hot):
        #hot, may sell
        adxr_r = 0 - (adxr - param.adxr_hot) / (param.adxr_toohot - param.adxr_hot)       
    elif (adxr >= param.adxr_warm):
        #a bit warming, hold and watch
        adxr_r = 1 - (adxr - param.adxr_warm) / (param.adxr_hot - param.adxr_warm)
    elif adxr >= param.adxr_best:        
        #Buy
        adxr_r = 2 - (adxr - param.adxr_best) / (param.adxr_warm - param.adxr_best)
    elif adxr >= param.adxr_good:        
        #Buy
        adxr_r = 1 + (adxr - param.adxr_good) / (param.adxr_best - param.adxr_good)
    elif adxr >= param.adxr_watch:
        #Still cold, hold and watch
        adxr_r = 0 + (adxr - param.adxr_watch) / (param.adxr_good - param.adxr_watch)
    elif adxr >= param.adxr_warning:
        #cold, may sell
        adxr_r = -1 + (adxr - param.adxr_watch) / (param.adxr_watch - param.adxr_warning)
    else:
        #No touch
        adxr_r = -1
    return adxr_r*0.5 #normalize

def GetElderRayRecommendation(bullpower, bearpower):
    '''
    http://www.investopedia.com/articles/trading/03/022603.asp    
    '''
    
    return 0
    
import numpy as numpy
import parameters as param

def GetMACDRecommendation( diff, pos):
    ''' 
    Caclulate the recommendation from the MACD diff
    return : macd_cross, macd_pos        
    '''         
    if (diff[-3] <=0) and (diff[-2] <= 0) and (diff[-1] > 0):  
        macd_cross = 1.2   # Gold Cross,            
    elif (diff[-3] >0) and (diff[-2] > 0) and (diff[-1] <= 0):
        macd_cross = -1.2  # Death cross
    elif (diff[-3] <=0) and (diff[-2] <= 0) and (diff[-1] <= 0):
        if  math.fabs(diff[-1]) >= math.fabs(diff[-3]) :
            macd_cross = -2   #diff increase in negitive side, the worst case
        elif math.fabs(diff[-1]) < math.fabs(diff[-3]):
            macd_cross = -0.5    #diff decrease in negitive side may turn to good.    
        else:
            macd_cross = -2    
    elif (diff[-3] >0) and (diff[-2] > 0) and (diff[-1] > 0):        
        if  diff[-1] >= diff[-3] : #difference increase in positive side, the best case
            macd_cross = 2  
        elif diff[-1] < diff[-3]:  #difference decrease in positive side, 
            macd_cross = 0.5        
        else:
            macd_cross = 1  #
    elif (diff[-3] >0) and (diff[-2] < 0) and (diff[-1] > 0):
        macd_cross = 1 #Gold cross but ossilation
    elif (diff[-3] <0) and (diff[-2] > 0) and (diff[-1] < 0):
        macd_cross = -1  #Gold cross but ossilation                 
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

def GetRecommendation(*args):    
    rsi = args[0]
    macd = args[1]
    macd_pos = args[2]
    kdj = args[3]
    #adx = args[4]
    #adx_trend = args[5]
    adxr = args[4]
    quote = args[5]    
    
    rsi_r = GetRSIRecommendation(rsi)
    macd_r, macd_pos = GetMACDRecommendation(macd, macd_pos)
    kdj_r = GetKDJRecommendation(kdj)
    adxr_r = GetADXRRecommendation(adxr)
    #adx_r = GetADXRecommendation(adx, adx_trend)
    #candle_r = GetCandleRecommendation(quote)
    
    #indicator = (macd_r + adx_r) / 2
    
    recommendation = Strategy_indicator_times_confidence(macd_r, macd_pos, rsi_r, kdj_r, adxr_r)
        
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
    
def Strategy_indicator_times_confidence( *args):
    '''
    Recommendation = indicator * confidence 
    
    Value from [-2 : 2]
    
    Use MACD as main indicator. 
    The shape of MACD is important, 
    the value of MACD and MACD signal use are main contributor of confidence. 
    RSI, J% in KDJ, and ADXR provide additional confidence. 
    RSI, J%, ADXR use linear distribute to calculate.  
    '''
    macd_r = args[0]
    macd_pos = args[1]
    rsi_r = args[2]
    kdj_r = args[3]
    adxr_r = args[4]
    
    indicator = macd_r
    confidence = macd_pos + (rsi_r + kdj_r + adxr_r) / 3
    
    recommendation = indicator * confidence 
    return recommendation
    
def Strategy_Ongoing(*args):
    
    return 0