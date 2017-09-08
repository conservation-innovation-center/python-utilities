## Import libraries
import os               ## short for "operating system"... lots of utility functions

## Create path to data and set it as our working directory
dataDirectory = '/Users/colin/Desktop/chescon-github/pandas/sample-data'
os.chdir(dataDirectory)

## Create list of files in a directory
files = os.listdir( dataDirectory )

## Print all the files in that list
for file in files:
   print(file)
   

## Print full paths of files in a directory
for root, dirs, files in os.walk( dataDirectory ):
    for name in files:
        print(os.path.join(root, name))
        

## Print only the csv files in a directory
for root, dirs, files in os.walk( dataDirectory ):
    for name in files:
        if name[name.rfind("."):len(name)] == ".csv":
            print(os.path.join(root, name))
        
        