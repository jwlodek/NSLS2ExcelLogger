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


# Function that creates the base for the data text file. Uses tabulations to keep values inline
def create_data_file():
    dataFile = open("data.txt", "w+")
    dataFile.write("NAME OF SAMPLE\t\tRESOLUTION LIMIT\t\t\tR VALUE\t\t\t\t\t\tI/SIGI\t\t\t\t\t\tCOMPLETENESS\t\t\t\tMultiplicity\t\t\t\tCC 1/2\t\t\t\t\t\tSPACE\t\tUNIT CELL\n")
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
        experimentLine = logFilePath.split('-')[4] + "-fastDP\t"
        logFile = open(logFilePath, "r+")
        line = logFile.readline()
        while line:
            line = line.strip()
            oldLine = line
            line = ' '.join(line.split())
            values = line.split(' ')
            if "High resolution" in line:
                values.remove("High")
            elif "CC 1/2" in line:
                values.remove("CC")
            if "High resolution" in line or "Rmerge" in line or "Completeness" in line or "I/sigma" in line or "CC 1/2" in line:      
                if "Anom." not in line:
                    experimentLine = experimentLine + values[1] + "\t" + values[2] + "\t" + values[3] + "\t\t"
            elif "Multiplicity" in line and "Anom." not in line:
                experimentLine = experimentLine + values[1] + "\t" + values[2] + "\t" + values[3] + "\t\t"
            elif "Merging point group:" in line:
                experimentLine = experimentLine + line[21:] + "\t\t"
            elif "Unit cell" in line:
                experimentLine = experimentLine + oldLine[10:] + "\n"
            #print experimentLine
            line = logFile.readline()
        logFile.close()
        dataFile.write(experimentLine)



def find_all_log_files(directoryPath):
    logFilePaths = []
    if os.path.exists(directoryPath):
        if os.path.isdir(directoryPath):
            for file in os.listdir(directoryPath):
                if file.endswith(".log"):
                    logFilePaths.append(directoryPath + "/"+ file)
            if logFilePaths.__len__() == 0:
                print "Error, no log files found in directory specified"
            return logFilePaths
        else:
            print "Error, specified path leads to file not directory\n"
    else:
        print "Error, specified directory does not exist\n"


def process_logs_by_path(directoryPath, dataFile):
    logFilePaths = find_all_log_files(directoryPath)
    for file in logFilePaths:
        parse_log_file(file, dataFile)


def process_logs_here(dataFile):
    logFilePaths = find_all_log_files(".")
    for file in logFilePaths:
        parse_log_file(file, dataFile)

# function that parses command line arguments
def parse_user_input(dataFile):
    parser = argparse.ArgumentParser(description = 'Experiment log data collection script')
    parser.add_argument('-d', '--directory', help = 'Directory in which to search for .log files to parse')
    arguments = vars(parser.parse_args())
    if arguments["directory"] is not None:
        process_logs_by_path(arguments["directory"], dataFile)
    else:
        process_logs_here(dataFile)

def run_script():
    dataFile = create_data_file()
    #parse_log_file("mx302490-1-HR00105p06-2-HR00105_6-fastDPOutput-fast_dp.log", dataFile)
    parse_user_input(dataFile)
    dataFile.close()




run_script()