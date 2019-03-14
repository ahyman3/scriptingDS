'''
filename: cleaning.property
created by: alex hyman
created on: 16 Aug 2018
Purpose: The purpose of this program is to provide a function that will read
in a text body file and a header file, and substitute the | for a "," and then
output the file into a csvfile. This was created because the FEC website provides
a text file for bulk download, and a separate header file for a download. This
program simplifies the process of merging the two files and outputting into a
structured data set.
'''

import csv
import pandas as pd
import numpy as np

#Takes body file, header file, and the name for the output file
def convert_txt(file, header, fileout):
    #Empty to save as csv
    linesOut = []
    #Staring with the header file
    with open(header, "r") as headerCSV:
        #readeing the header csv
        csvreader = csv.reader(headerCSV, delimiter = ",")
        #putting the first and only line in the empty list
        linesOut.append(next(csvreader))
        #Close header file
        headerCSV.close()

    #open the text file with all of the data
    with open(file, "r") as txtRead:
        #For each line of data
        for line in txtRead:
            #Create a list and split the elements at the |
            newLine = line.split("|")
            #append the line to the lines out list
            linesOut.append(newLine)
        #Close the text file
        txtRead.close()

    #Open the file for writing named as provided
    with open(fileout, "w") as csvout:
        #Creatinf the csvwriter object
        csvwriter = csv.writer(csvout)
        #For each line in the saved list
        for line in linesOut:
            #write the line in the csv
            csvwriter.writerow(line)
        #Close the file
        csvout.close()

if __name__ == "__main__":
    pass
