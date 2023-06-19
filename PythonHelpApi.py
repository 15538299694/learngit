import os
class FUBTAPI():
    def ReadExceldata(self,Sheetname,x,y,ExcelPath):#读取excel数据
        import xlrd
        ExcelPath=ExcelPath
        Sheet=xlrd.open_workbook(ExcelPath).sheet_by_name(Sheetname)
        return Sheet.cell_value(x,y),Sheet.nrows
    def WriteExceldata(self,x,y,z,pwd,name,num):#写入excel数据
        import xlrd
        from xlutils.copy import copy
        ExcelPath = 'C:\\Users\\Administrator\\Desktop\\token.xls'
        sheetname=xlrd.open_workbook(ExcelPath,formatting_info=True)
        a=sheetname.sheet_by_name('Sheet1').nrows
        wb=copy(sheetname)
        sheet=wb.get_sheet(0)
        sheet.write(a,x,name)
        sheet.write(a,y,pwd)
        sheet.write(a,z,num)
        os.remove(ExcelPath)
        wb.save(ExcelPath)

    def CreatHtmlreport(self,HTMLname,revTitle,revD,revTest):#生成测试报告
        import HTMLTestRunner
        HtmlPath='..\\FUTBTestReport\\'+HTMLname+'.html'
        with open(HtmlPath,'wb') as HTMLStearm:
            HTMLTestRunner.HTMLTestRunner(
                stream=HTMLStearm,
                verbosity=2,
                title=revTitle,
                description=revD
            ).run(revTest)
