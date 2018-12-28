#
# Simple script that tests if xlsxwriter was installed correctly
#
# Author: Jakub Wlodek
# Created on: Dec 28, 2018

import xlsxwriter

# Creates new excel workbook
workbook = xlsxwriter.Workbook('testSpreadsheet.xlsx')

# Adds worksheet to workbook
worksheet = workbook.add_worksheet()

# writes 'Hello NSLS2' to the A-1 cell 
worksheet.write('A1', 'Hello NSLS2')

# Closes and saves the workbook
workbook.close()
