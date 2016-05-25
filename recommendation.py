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
    
def GetMACDRecommendation( diff ):
    if (diff[-3] <=0) and (diff[-2] <= 0) and (diff[-1] > 0):  
        macd_cross = 1 
    elif (diff[-3] >0) and (diff[-2] > 0) and (diff[-1] <= 0):
        macd_cross = -1
    else:
        macd_cross = 0
    return macd_cross; 



def GetCandleRecommendation( quote ):
    if quote.Open < quote.Close:
        upper = quote.High - quote.Close
        lower = quote.Open - quote.Low
        candle = quote.Close - quote.Open
        
    else:
        upper = quote.High - quote.Open
        lower = quote.Close - quote.Low
        candle = quote.Open - quote.Close
    
    
    rec = 0
    return rec;

def GetRecommendation(rsi, macd, kdj, candle):
    rsi_r = GetRSIRecommendation(rsi)
    kdj_r = GetKDJRecommendation(kdj)
    macd_r = GetMACDRecommendation(macd)
    
    recommendation = rsi_r + kdj_r + macd_r + candle_r * 1 / 3
    return recommendation
    
    
    