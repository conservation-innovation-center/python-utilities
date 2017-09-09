## Import libraries
import os   ## short for "operating system"... lots of utility functions

## Create path to data and set it as our working directory
dataDirectory = '/Users/colin/Desktop/chescon-github/pandas/sample-data'
os.chdir(dataDirectory)

## Open csv file
hucs = open('huc_table.csv')

## Get comma separated string of columns
header = hucs.readline()
print(type(header))     ## Prove this is a string

## Create a comma separated list of columns
columns = header.split(",")
print(type(columns))    ## Prove this is a list

## Loop through the list and print the names
for column in columns:
    print(column)
