import xlsxwriter

def InitExcel(filename):
    workbook = xlsxwriter.Workbook('TodaysResult.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "Symbol" )
    worksheet.write(0, 1, "RSI" )
    worksheet.write(0, 2, "MACD" )
    worksheet.write(0, 3, "J" )
    worksheet.write(0, 4, "Candle" )
    
    
def WriteResultToText(filename, result):
    symbol = result[0]
    rsi = result[1]
    macd_diff = result[2]
    macd_pos = result[3]
    j = result[4]
    #candle = result[5]
    rec = result[5]
         
    file = open(filename, 'a')
    line =  symbol + "\t" + str(rsi) + "\t" + str(macd_diff) + "\t" + str(macd_pos) + "\t" + str(j)  + "\t"  + str(rec) + "\n"
    file.writelines(line)
    file.close()
    