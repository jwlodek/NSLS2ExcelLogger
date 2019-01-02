# NSLS2 17MX log parsing

This repository contains a collection of scripts that can be used to parse log files for NSLS-2 17MX experiments into a more
condensed data file, and from there to an excel spreadsheet.

### Installation

To install the scripts, first clone this repository with:

```
git clone https://github.com/jwlodek/NSLS2ExcelLogger
cd NSLS2ExcelLogger/scripts
```
then, from inside the scripts directory, run 
```
sudo bash installDependancies.sh
```

this will install python pip and xlsx parser, all  required to run the scripts

### Usage

To run the scripts, first locate the directory with the .log files you wish to collect. Then
run:
```
python logParser.py -e $PATH_TO_DATA_FILE -d $PATH_TO_DIR_WITH_LOGS
```
where the path to the data file can be something like ~/Documents/data.txt.

If you do not have the -e flag, the script will default to data.txt in the current directory.

To run the excel script:
```
python data2excel.py -d $PATH_TO_DATA_FILE -e $PATH_TO_EXCEL_FILE
```
where PATH_TO_DATA_FILE is the path to a data file generated with logParser.py.
PATH_TO_EXCEL_FILE must be a legal path that ends in a .xlsx file, or if the -e flag
is omitted, the script will default to 'outputSheet.xlsx' in the current directory
