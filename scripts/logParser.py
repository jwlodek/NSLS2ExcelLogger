#
# Python script that parses all log files and inputs them into a
# .txt data file. Optionally, it can also continue to do update it live in
# real time.
#
# Author: Jakub Wlodek
# Created on: Dec 28, 2018
#

import os
import argparse


# Function that creates the base for the data text file. Uses tabulations to keep values inline
def create_data_file(pathName):
    dataFile = open(pathName, "w+")
    dataFile.write("NAME OF SAMPLE\t\t\tRESOLUTION LIMIT\t\t\tR VALUE\t\t\t\t\t\tI/SIGI\t\t\t\t\t\tCOMPLETENESS\t\t\t\tMultiplicity\t\t\t\tCC 1/2\t\t\t\t\t\tSPACE\t\tUNIT CELL\n")
    dataFile.write("(fastDP worked)\t\t\tAll\t\tLow\t\tHigh\t\tAll\t\tLow\t\tHigh\t\tAll\t\tLow\t\tHigh\t\tAll\t\tLow\t\tHigh\t\tAll\t\tLow\t\tHigh\t\tAll\t\tLow\t\tHigh\t\tGROUP\n")
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
    # disregard unsuccessful experiments
    if log_file_len(logFilePath) < 20:
        return
    else:
        # this will be the line added to the data file
        experimentLine = logFilePath.split('-')[4] + "-fastDP\t\t"
        logFile = open(logFilePath, "r+")
        line = logFile.readline()
        while line:
            # remove unused whitespace
            line = line.strip()
            oldLine = line
            line = ' '.join(line.split())
            values = line.split(' ')
            # for lines that have extra space, remove first string
            if "High resolution" in line:
                values.remove("High")
            elif "CC 1/2" in line:
                values.remove("CC")
            # These are lines with three values that need to be tabulated
            if "High resolution" in line or "Rmerge" in line or "Completeness" in line or "Multiplicity" in line or "I/sigma" in line or "CC 1/2" in line:      
                if "Anom." not in line:
                    if len(values[1]) < 4:
                        experimentLine = experimentLine + values[1] + "\t\t"
                    else:
                        experimentLine = experimentLine + values[1] + "\t"
                    if len(values[2]) < 4:
                        experimentLine = experimentLine + values[2] + "\t\t"
                    else:
                        experimentLine = experimentLine + values[2] + "\t"
                    if len(values[3]) < 4:
                        experimentLine = experimentLine + values[3] + "\t\t\t"
                    else:
                        experimentLine = experimentLine + values[3] + "\t\t"
            # two remaining lines
            elif "Merging point group:" in line:
                experimentLine = experimentLine + line[21:] + "\t\t"
            elif "Unit cell" in line:
                experimentLine = experimentLine + oldLine[10:] + "\n"
            # go to next line
            line = logFile.readline()
        # close the log file and write to the data file
        logFile.close()
        dataFile.write(experimentLine)


# Function used to discover .log files in a specified directory
def find_all_log_files(directoryPath):
    logFilePaths = []
    # check if it exists
    if os.path.exists(directoryPath):
        #check if it is a dir
        if os.path.isdir(directoryPath):
            for file in os.listdir(directoryPath):
                # if .log, add to list
                if file.endswith(".log"):
                    logFilePaths.append(directoryPath + "/"+ file)
            if len(logFilePaths) == 0:
                print "Error, no log files found in directory specified"
            return logFilePaths
        else:
            print "Error, specified path leads to file not directory\n"
    else:
        print "Error, specified directory does not exist\n"


# Function that iterates over discovered .log files in specified
# directory and parses each one
def process_logs_by_path(directoryPath, dataFile):
    logFilePaths = find_all_log_files(directoryPath)
    for file in logFilePaths:
        parse_log_file(file, dataFile)


# Function that iterates over discovered .log files and
# parses each one
def process_logs_here(dataFile):
    logFilePaths = find_all_log_files(".")
    for file in logFilePaths:
        parse_log_file(file, dataFile)


# function that parses command line arguments
def parse_user_input():
    parser = argparse.ArgumentParser(description = 'Experiment log data collection script')
    parser.add_argument('-e', '--external', help = 'File path for output data file')
    parser.add_argument('-d', '--directory', help = 'Directory in which to search for .log files to parse')
    arguments = vars(parser.parse_args())
    if arguments["external"] is not None:
        dataFile = create_data_file(arguments["external"])
    else:
        dataFile = create_data_file("data.txt")
    if arguments["directory"] is not None:
        process_logs_by_path(arguments["directory"], dataFile)
    else:
        process_logs_here(dataFile)


# Main driver function for the script. First creates a data file, then parses log files in the specified location
def run_script():
    parse_user_input()


# Function used to test parsing on a single log file
def run_script_debug():
    dataFile = create_data_file("data.txt")
    parse_log_file("../TestData/mx302490-2-VIVA019p02-2-VIVA019_2-fastDPOutput-fast_dp.log", dataFile)
    dataFile.close()


run_script()