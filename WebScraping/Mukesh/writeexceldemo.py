import openpyxl
from openpyxl import Workbook
#create new Excel sheet

wb=Workbook()


wb['Sheet'].title="Report of Automation"
sh1=wb.active
sh1['A1'].value = "Name"
sh1['B1'].value = "Status"
sh1['A2'].value = "Python"
sh1['B2'].value = "Active"
sh1['A3'].value = "Java"
sh1['B3'].value = "Active"
wb.save("FinalReport.xlsx")



