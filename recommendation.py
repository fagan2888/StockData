def GetRSIRecommendation( rsi ):
    if (rsi < 30):
        rec = 1
    elif (rsi>70):
        rec = -1  
    else:
        rec = 0
    return rec;
        

def GetKDJRecommendation( kdj ):
    if (kdj < 20):
        rec = 1
    elif (kdj > 80):
        rec = -1  
    else:
        rec = 0
    return rec;
    
def GetMACDRecommendation( macd ):
    if (macd < 20):
        rec = 1
    elif (macd > 80):
        rec = -1  
    else:
        rec = 0
    return rec;

def GetCandleRecommendation( candle ):
    rec = 0
    return rec;

def GetRecommendation(rsi, macd, kdj, candle):
    rsi_r = GetRSIRecommendation(rsi)
    kdj_r = GetKDJRecommendation(kdj)
    macd_r = GetMACDRecommendation(macd)
    
    recommendation = rsi_r + kdj_r + macd_r + candle_r * 1 / 3
    return recommendation
    
    
    