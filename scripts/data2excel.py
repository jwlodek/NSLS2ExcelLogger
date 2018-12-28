#
# Script that will convert data file from logs into an Excel Spreadsheet
# 
# Author: Jakub Wlodek
# Created on: Dec 28, 2018

# import libs
import os
import argparse
import xlsxwriter


# Function that enters the basic information for the spreadsheet
def prep_worksheet(worksheet):
    # First row
    worksheet.write('A1', 'NAME OF SAMPLE')
    worksheet.write('B1', 'RESOLUTION LIMIT')
    worksheet.write('E1', 'R VALUE')
    worksheet.write('H1', 'I/SIGI')
    worksheet.write('K1', 'COMPLETENESS')
    worksheet.write('N1', 'MULTIPLICITY')
    worksheet.write('Q1', 'CC 1/2')
    worksheet.write('T1', 'SPACE')
    worksheet.write('U1', 'UNIT CELL')
    # second row
    worksheet.write('A2', '(fastDP worked)')
    worksheet.write('B2', 'All')
    worksheet.write('C2', 'Low')
    worksheet.write('D2', 'High')
    worksheet.write('E2', 'All')
    worksheet.write('F2', 'Low')
    worksheet.write('G2', 'High')
    worksheet.write('H2', 'All')
    worksheet.write('I2', 'Low')
    worksheet.write('J2', 'High')
    worksheet.write('K2', 'All')
    worksheet.write('L2', 'Low')
    worksheet.write('M2', 'High')
    worksheet.write('N2', 'All')
    worksheet.write('O2', 'Low')
    worksheet.write('P2', 'High')
    worksheet.write('Q2', 'All')
    worksheet.write('R2', 'Low')
    worksheet.write('S2', 'High')
    worksheet.write('T2', 'GROUP')


# Inserts line from data log file into the spreadsheet
def insertIntoSpreadsheet(values, counter, worksheet):
    worksheet.write('A{}'.format(counter), values[0])
    worksheet.write('B{}'.format(counter), values[1])
    worksheet.write('C{}'.format(counter), values[2])
    worksheet.write('D{}'.format(counter), values[3])
    worksheet.write('E{}'.format(counter), values[4])
    worksheet.write('F{}'.format(counter), values[5])
    worksheet.write('G{}'.format(counter), values[6])
    worksheet.write('H{}'.format(counter), values[7])
    worksheet.write('I{}'.format(counter), values[8])
    worksheet.write('J{}'.format(counter), values[9])
    worksheet.write('K{}'.format(counter), values[10])
    worksheet.write('L{}'.format(counter), values[11])
    worksheet.write('M{}'.format(counter), values[12])
    worksheet.write('N{}'.format(counter), values[13])
    worksheet.write('O{}'.format(counter), values[14])
    worksheet.write('P{}'.format(counter), values[15])
    worksheet.write('Q{}'.format(counter), values[16])
    worksheet.write('R{}'.format(counter), values[17])
    worksheet.write('S{}'.format(counter), values[18])
    worksheet.write('T{}'.format(counter), values[19] + " " + values[20] + " " + values[21]+ " " + values[22])
    temp = ""
    for i in range(23, len(values)):
        temp = temp + values[i] + " "
    worksheet.write('U{}'.format(counter), temp)


# function that contains the main loop that iterates over the dat file and places values into 
# the excel spreadsheet
def parse_to_excel(dataFilePath, excelFilePath):
    print "Parsing to excel file"
    if not os.path.isfile(dataFilePath):
        print "Error data file is invalid"
        return
    elif not excelFilePath.endswith(".xlsx"):
        print "Error, excel file name is invalid, must end in .xlsx"
        return
    dataFile = open(dataFilePath, "r+")
    workbook = xlsxwriter.Workbook(excelFilePath)
    worksheet = workbook.add_worksheet()
    prep_worksheet(worksheet)
    line = dataFile.readline()
    counter = 1
    while line:
        # turn into space delimited line
        line = line.strip()
        line = line.replace('\t', ' ')
        line = ' '.join(line.split())
        values = line.split(' ')
        if len(values) > 25:
            insertIntoSpreadsheet(values, counter, worksheet)
        counter = counter + 1
        line = dataFile.readline()
            
    workbook.close()


# function that parses user arguments to get path to data file and excel sheet
def parse_user_args():
    parser = argparse.ArgumentParser(description = 'Experiment log data collection script')
    parser.add_argument('-d', '--data', help = 'File path for output data file')
    parser.add_argument('-e', '--excel', help = 'name to use for excel file')
    arguments = vars(parser.parse_args())
    if arguments["data"] is not None:
        dataFilePath = arguments["data"]
    else:
        print "ERROR, please specify data file with -d flag\n"
        return
    if arguments["excel"] is not None:
        parse_to_excel(dataFilePath, arguments["excel"])
    else:
        parse_to_excel(dataFilePath, "outputSheet.xlsx")


# Program driver
def run_script():
    parse_user_args()


run_script()
