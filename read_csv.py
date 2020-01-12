import xlrd
workbook=xlrd.open_workbook('test.xls')
number = sheet.cell(1,1).value
email  = sheet.cell(1,2).value
name = sheet.cell(1,0).value
print(name,number,email)
