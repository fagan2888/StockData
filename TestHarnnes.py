 
'''
Use to quickly test 
'''

import ta_indicator_calc as ind_calc
from recommendation import GetRecommendation

def CalculateRecommendation(*args):
    '''
        Calculation the recommendation based on the quote input
        input:  1. quote of symbol
                2. option: data shift from today, to calculate recommendation of previous days. default 1
        output:  macd, macd_pos, rsi, j, recommendation        
    '''
    
    quote = args[0]
    if (len(args) == 2):
        data_shife = args[1]
    else:
        data_shife = 1
    rec = 0 
    macd_r = 0
    macd_pos = 0
    rsi_today = 0
    j = 0    
    if not(isinstance(quote, str)):         
        rsi_today = ind_calc.rsi(quote.Close)
        macd_diff, macd_pos = ind_calc.macd_dif(quote.Close)   
        j = ind_calc.J(quote)
        quote_lastday = GetStockQuote(symbol,data_shife, data_shife)
        if not(isinstance(quote_lastday, str)):
            rec, macd_r, macd_pos = GetRecommendation(rsi_today,macd_diff,macd_pos, j, quote_lastday)  
            print("Final recommendation of ", symbol , " is ", rec)             
        else:
            print("No last day quote, no recommendation.") 
                                                     
    else:
        print("No Quote for ", symbol)
    
    return macd_r, macd_pos, rsi_today, j, rec    


#Create a blank file
#from recommendation import CleanRecommendation
#CleanRecommendation("today_recommendation_to_buy.txt")
#CleanRecommendation("today_recommendation_to_sell.txt")


# Get the symbols from the text files.
#from stock import GetStockSymbol
#symbols = GetStockSymbol("stocklist.txt", ".CO") +  GetStockSymbol("stocklist_as.txt")
symbols = ['GEN.CO', 'SIM.CO']

from stock import GetStockQuote
from recommendation import WriteRecommendation
import ReportManager as rm
import parameters as param
import recommendation as reccalc
#rm.CreateHTMLFile(param.HTML_REPORT_FILENAME)   #Create the header part of HTML report
for symbol in symbols:    
    print(symbol)        
    # Get the stock quote
    quote = GetStockQuote(symbol, param.QUOTE_LENGTH, 0)
    #adx, adx_trend = ind_calc.ADX(quote)
    #adx_rec = reccalc.GetADXRecommendation(adx, adx_trend)
    #print(adx_rec)
    
    #di_m = ind_calc.Minus_DI(quote)
    #print(di_m)
    #di_p = ind_calc.Plus_DI(quote)
    #print(di_p)
    print(quote)
    
    ind_calc.macd_dif(quote.Close)
    
    
    
    #macd_r, macd_pos, rsi, j, rec = CalculateRecommendation(quote)  # Today's recommendation
    
    #if (rec > 1):
    #    WriteRecommendation(symbol, rec, "today_recommendation_to_buy.txt")   # Only write those may buy
    #elif (rec<=-1):
    #    WriteRecommendation(symbol, rec, "today_recommendation_to_sell.txt")  # only write those need sell.         

    #quote_1 = GetStockQuote(symbol, param.QUOTE_LENGTH + 1, 1)
    #macd_r_1, macd_pos_1, rsi_1, j_1, rec_1 = CalculateRecommendation(quote_1, 2)
    #quote_2 = GetStockQuote(symbol,param.QUOTE_LENGTH + 2, 2)
    #macd_r_2, macd_pos_2, rsi_2, j_2, rec_2 = CalculateRecommendation(quote_2, 3)
    #quote_3 = GetStockQuote(symbol,param.QUOTE_LENGTH + 3, 3)
    #macd_r_3, macd_pos_3, rsi_3, j_3, rec_3 = CalculateRecommendation(quote_3, 4)
    #quote_4 = GetStockQuote(symbol, param.QUOTE_LENGTH + 4, 4)
    #macd_r_4, macd_pos_4, rsi_4, j_4, rec_4 = CalculateRecommendation(quote_4, 5)
    #quote_5 = GetStockQuote(symbol,65, 5)
    #macd_r_5, macd_pos_5, rsi_5, j_5, rec_5 = CalculateRecommendation(quote_5, 6)
    #quote_6 = GetStockQuote(symbol,66, 6)
    #macd_r_6, macd_pos_6, rsi_6, j_6, rec_6 = CalculateRecommendation(quote_6, 5)
    
    
    #line = [symbol, param.MACD_TYPE, macd_r , macd_r_1, macd_r_2 , macd_r_3 , macd_r_4]
    #rm.AddLineToHTMLTable(param.HTML_REPORT_FILENAME, line)
    #line = [symbol, param.MACD_POS_TYPE, macd_pos , macd_pos_1 , macd_pos_2 , macd_pos_3,macd_pos_4]
    #rm.AddLineToHTMLTable(param.HTML_REPORT_FILENAME, line)
    #line = [symbol, param.RSI_TYPE, rsi , rsi_1 , rsi_2 , rsi_3 , rsi_4]          
    #rm.AddLineToHTMLTable(param.HTML_REPORT_FILENAME, line)    
    #line = [symbol, param.J_TYPE, j , j_1 , j_2 , j_3 , j_4]
    #rm.AddLineToHTMLTable(param.HTML_REPORT_FILENAME, line)
    #line = [symbol, param.RECOMMENDATION_TYPE, rec , rec_1 , rec_2 , rec_3 , rec_4]
    #rm.AddLineToHTMLTable(param.HTML_REPORT_FILENAME, line)    
    
#rm.CloseHTMLFile(param.HTML_REPORT_FILENAME)  # write the rest of HTML.  