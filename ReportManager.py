import xlsxwriter
import parameters as param

def InitExcel(filename):
    workbook = xlsxwriter.Workbook('TodaysResult.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "Symbol" )
    worksheet.write(0, 1, "RSI" )
    worksheet.write(0, 2, "MACD" )
    worksheet.write(0, 3, "J" )
    worksheet.write(0, 4, "Candle" )    

#def CreateHTMLFile(filename, header=None):
#    htmlfile = open(filename, "w")
#    htmlfile.writelines( """<html> <head> <title>Full Report based on today's data</title> </head> <body> <table border="1">""")    
#    htmlfile.close()

def CreateHTMLFile(filename, header = "Full Report based on today's data"):
    htmlfile = open(filename, "w")
    htmlfile.writelines( """<html> <head> <title> """ + header + """ </title> </head> <body> <table border="1">""")    
    htmlfile.close()

def CloseHTMLFile(filename):
    htmlfile = open(filename, "a")    
    htmlfile.writelines("""</table></body></html>""") 
    htmlfile.close()

def AddLineToHTMLTable(*args):
    '''
    Used by FullReport.html
    '''
    filename = args[0]
    line = args[1]
    type = line[1]
    htmlfile = open(filename, "a")    
    htmlfile.writelines("""<tr>""")
    for item in line:
        htmlfile.writelines("""<td """)
        #Get the color code
        if not(isinstance(item, str)):  # skip string items like Symbol
            htmlfile.writelines(GetCellColorCode(type,item))
        if  type == param.RECOMMENDATION_TYPE:
            htmlfile.writelines("""><b>""")
        else:
            htmlfile.writelines(""">""")        
        htmlfile.writelines(str(item))
        if type == param.RECOMMENDATION_TYPE:
            htmlfile.writelines("""</b></td>""")
        else:
            htmlfile.writelines("""</td>""")
        
    htmlfile.writelines("""</tr>""")
    htmlfile.close()
    
def GetCellColorCode(*args):

    '''
        COLOR CODE: 
            
    '''
    type = args[0]
    value = args[1]
    
    if type == param.MACD_TYPE:
        if value == 2:
            bgcolor = param.COLORCODE_OUTSTANDINGSIGN
        elif value == 1 or value == 1.2:
            bgcolor = param.COLORCODE_GOODSIGN
        elif value == 0 or value == 0.5:
            bgcolor = param.COLORCODE_WATCHSIGN
        elif value == -1 or value == -0.5:
            bgcolor = param.COLORCODE_WARNINGSIGN 
        elif value == -2 or value == -1.2:
            bgcolor = param.COLORCODE_QUITSIGN            
        else:
            bgcolor = param.COLORCODE_NEUTURALSIGN
    elif type == param.ADX_TYPE:
        if value == 2:
            bgcolor = param.COLORCODE_OUTSTANDINGSIGN
        elif value == 1:
            bgcolor = param.COLORCODE_GOODSIGN
        elif value == 0:
            bgcolor = param.COLORCODE_WATCHSIGN
        elif value == -1:
            bgcolor = param.COLORCODE_WARNINGSIGN 
        elif value == -2:
            bgcolor = param.COLORCODE_QUITSIGN            
        else:
            bgcolor = param.COLORCODE_NEUTURALSIGN         
    elif type == param.ADX_REC_TYPE:
        if value >= 25:
            bgcolor = param.COLORCODE_GOODSIGN
        else:
            bgcolor = param.COLORCODE_WARNINGSIGN
    elif type == param.ADXR_TYPE:
        if value >= 50:
            bgcolor = param.COLORCODE_WARNINGSIGN
        elif value >= 45:
            bgcolor = param.COLORCODE_WATCHSIGN
        elif value >= 40:
            bgcolor = param.COLORCODE_GOODSIGN
        elif value >= 35:
            bgcolor = param.COLORCODE_OUTSTANDINGSIGN        
        elif value >= 30:
            bgcolor = param.COLORCODE_OUTSTANDINGSIGN
        elif value >= 25:
            bgcolor = param.COLORCODE_GOODSIGN
        elif value >= 20:
            bgcolor = param.COLORCODE_WATCHSIGN
        else:
            bgcolor = param.COLORCODE_WARNINGSIGN                   
    elif type == param.MACD_POS_TYPE:
        if value == 1:
            bgcolor = param.COLORCODE_OUTSTANDINGSIGN
        elif value == 0:
            bgcolor = param.COLORCODE_NEUTURALSIGN
        elif value == -1:
            bgcolor = param.COLORCODE_WARNINGSIGN
        elif value < 1 and value > 0 :
            bgcolor = param.COLORCODE_GOODSIGN        
        else:
            bgcolor = param.COLORCODE_NEUTURALSIGN
    elif type == param.RSI_TYPE:
        if value < 20:
            bgcolor = param.COLORCODE_OUTSTANDINGSIGN
        elif value < 30:
            bgcolor = param.COLORCODE_GOODSIGN
        elif value < 50:
            bgcolor = param.COLORCODE_NEUTURALSIGN
        elif value < 70:
            bgcolor = param.COLORCODE_WATCHSIGN 
        elif value <= 80:
            bgcolor = param.COLORCODE_WARNINGSIGN
        elif value > 80 :
            bgcolor = param.COLORCODE_QUITSIGN            
        else:
            bgcolor = param.COLORCODE_NEUTURALSIGN
    elif type == param.J_TYPE :
        if value < 10:
            bgcolor = param.COLORCODE_OUTSTANDINGSIGN
        elif value < 20:
            bgcolor = param.COLORCODE_GOODSIGN
        elif value < 50:
            bgcolor = param.COLORCODE_NEUTURALSIGN
        elif value < 80:
            bgcolor = param.COLORCODE_WATCHSIGN 
        elif value <= 90:
            bgcolor = param.COLORCODE_WARNINGSIGN
        elif value > 90 :
            bgcolor = param.COLORCODE_QUITSIGN            
        else:
            bgcolor = param.COLORCODE_NEUTURALSIGN
    elif type == param.RECOMMENDATION_TYPE:
        if value >= 2:
            bgcolor = param.COLORCODE_REC_STRONGBUY
        elif value > 1:
            bgcolor = param.COLORCODE_REC_BUY
        elif value >= 0.5:
            bgcolor = param.COLORCODE_REC_MAYBUY
        elif value > 0:
            bgcolor = param.COLORCODE_REC_WATCH 
        elif value > -1:           
            bgcolor = param.COLORCODE_REC_MAYSELL                    
        else:            
            bgcolor = param.COLORCODE_REC_SELL
    else:
        bgcolor = """BGCOLOR=#FFFFFF """
    return bgcolor

def AddLineToHTMLTable2(*args):
    '''
    For TrendReport.html
    '''
    filename = args[0]
    line = args[1]
    rec = line[2]
    htmlfile = open(filename, "a")    
    htmlfile.writelines("""<tr>""")

    for i in range(0, len(line)):
        htmlfile.writelines("""<td """)
        if i == 2:
            if (line[i] == 2) :
                htmlfile.writelines(param.COLORCODE_REC_BUY)                    
            elif (line[i] >= 3):
                htmlfile.writelines(param.COLORCODE_REC_STRONGBUY)            
        elif i >= 3 and i <=12:            
            if(line[i]) :
                htmlfile.writelines(param.COLORCODE_GOODSIGN)
        htmlfile.writelines(""">""")    
        htmlfile.writelines(str(line[i]))
        htmlfile.writelines("""</td>""") 
        
    htmlfile.writelines("""</tr>""")
    htmlfile.close()


    
def WriteResultToText(filename, result):
    symbol = result[0]
    rsi = result[1]
    macd_diff = result[2]
    macd_pos = result[3]
    j = result[4]
    #candle = result[5]
    rec = result[5]
    
    file = open(filename, 'a')
    for item in result:                
        line =  symbol + "\t" + str(item) + "\n"
        file.writelines(line)
    file.close()


