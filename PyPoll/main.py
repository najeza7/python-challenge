# Import modules
import os
import csv


# Set path
csvpath = os.path.join(".","Resources","election_data.csv")

# Open the cvs file
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    print (csvheader)