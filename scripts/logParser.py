#
# Python script that parses all log files and inputs them into a
# .txt data file. Optionally, it can also continue to do update it live in
# real time.
#
# Author: Jakub Wlodek
# Created on: Dec 28, 2018
#

import os
import shutil
import argparse


# Function that creates the base for the data text file
def create_data_file():
    dataFile = open("data.txt", "w+")
    dataFile.write("NAME OF SAMPLE\t\tRESOLUTION LIMIT\t\t\tR VALUE\t\t\t\t\t\tCOMPLETENESS\t\t\t\tI/SIGI\t\t\t\t\t\tMultiplicity\t\t\t\tCC 1/2\t\t\t\t\t\tSPACE\t\t\tUNIT CELL\n")
    dataFile.write("(fastDP worked)\t\tAll\t\tLow\t\tHigh\t\tAll\t\tLow\t\tHigh\t\tAll\t\tLow\t\tHigh\t\tAll\t\tLow\t\tHigh\t\tAll\t\tLow\t\tHigh\t\tAll\t\tLow\t\tHigh\t\tGROUP\n")
    return dataFile


# Function that gets the length of a log file to filter out unsuccessful tests
def log_file_len(logFilePath):
    logFile = open(logFilePath, "r+")
    line = logFile.readline()
    counter = 0
    while line:
        counter = counter + 1
        line = logFile.readline()
    return counter


# file that actually parses the log file and writes the line to the data file
def parse_log_file(logFilePath, dataFile):
    if log_file_len(logFilePath) < 20:
        return
    else:
        experimentLine = logFilePath.split('-')[5] + "-fastDP\t\t"
        logFile = open(logFilePath, "r+")
        line = logFile.readline()
        while line:
            line.strip()
            if "High resolution" in line:
                values = line.split(' ')





def run_script():
    dataFile = create_data_file()
    dataFile.close()




run_script()