from openpyxl import Workbook
wb = Workbook()
ws1 = wb.create_sheet("Mysheet")

wb.save('balances.xlsx')
