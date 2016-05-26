import xlsxwriter

def InitExcel(filename)
    workbook = xlsxwriter.Workbook('TodaysResult.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "Symbol" )
    worksheet.write(0, 1, "RSI" )
    worksheet.write(0, 2, "MACD" )
    worksheet.write(0, 3, "J" )
    worksheet.write(0, 4, "Candle" )
    
    
