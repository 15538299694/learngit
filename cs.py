def ReadExceldata(Sheetname,x,y,z,ExcelPath):#读取excel数据
    import xlrd
    ExcelPath=ExcelPath
    Sheet=xlrd.open_workbook(ExcelPath).sheet_by_name(Sheetname)
    print(str(Sheet.cell_value(x,y)))
    print(Sheet.cell_value(x,z))
    # return Sheet.cell_value(x,y)
def ReadExceldatarow():#读取excel数据
    import xlrd
    Sheetname = "Sheet1"
    ExcelPath = 'C:\\Users\\lenovo\\Desktop\\111111.xls'
    ExcelPath=ExcelPath
    Sheet=xlrd.open_workbook(ExcelPath).sheet_by_name(Sheetname)
    return Sheet.nrows
    # return Sheet.cell_value(x,y)
if __name__ == '__main__':
    row=ReadExceldatarow()
    for i in range(0,row):
        x = i
        y = 0
        z = 1
        Sheetname="Sheet1"
        ExcelPath='C:\\Users\\lenovo\\Desktop\\111111.xls'
        ReadExceldata(Sheetname,x,y,z,ExcelPath)