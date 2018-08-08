'''
File Name: HW1.property
Created By: Alex Hyman
Created on: 7 Aug 2018
Purpose: To explore a the Donors_Data.csv file and answer some questions relating
to the data and provide some graphics

Questions:
1. How much are people in each zipcode donating to the university, and what does
the distribution look like by gender

Answer: We will create a csv file that outputs the mean of the average gift for
each gender number within each zipcode. We will also create a boxplot of the
average gift for each gender in each of the zip codes to show the spread
'''

import csv                          #Reading the csv
import pandas as pd                 #Pandas for data frames
import matplotlib.pyplot as plt     #For plotting
import seaborn as sns               #More for plotting
import numpy as np                  #For statistics


if __name__ == "__main__":
    keys = ["Row Id", "Row Id.", "zipconvert_2", "zipconvert_3", "zipconvert_4",
        "zipconvert_5", "homeowner dummy", "NUMCHLD", "INCOME", "gender dummy",
        "WEALTH", "HV", "Icmed", "Icavg", "IC15", "NUMPROM", "RAMNTALL",
        "MAXRAMNT", "LASTGIFT", "totalmonths", "TIMELAG", "AVGGIFT", "TARGET_B",
        "TARGET_D"]
    #Converting donor data into data frame
    donors = pd.read_csv("Donors_Data.csv")
    #List of all the dummy zip code columns
    zip_columns = ["zipconvert_2", "zipconvert_3", "zipconvert_4", "zipconvert_5"]
    #Labels we are giving to the different zip codes
    zip_labels = ["Zipcode 1", "Zipcode 2", "Zipcode 3", "Zipcode 4"]
    #for each column name and label in the zipcode columns and labels
    for col, label in zip(zip_columns, zip_labels):
        #Find all rows that have an instance of 1 in that column and in a new column
        #"zip_all", give it the corresponding value specified in zip_labels
        donors.loc[donors[col] == 1, "zip_all"] = label
    #Create a boxplot of the average gift amount by zipcode, separated by
    #the gender dummy variable
    genList = list(set(donors["gender dummy"]))
    #
    meanGift = {}
    for zip in zip_labels:
        meanGift[zip] = {}
        for gender in genList:
            allAvg = donors.loc[(donors["zip_all"] == zip) & \
                (donors["gender dummy"] == gender), "AVGGIFT"]
            meanGift[zip][gender] = np.mean(allAvg)
    outfile = 'genderZipGift.csv'
    with open(outfile, "w") as outcsv:
        csvwriter = csv.writer(outcsv)
        csvwriter.writerow(["Average gift by Gender within Zipcode"])
        csvwriter.writerow([])
        csvwriter.writerow([])
        zip_labels.insert(0, "")
        csvwriter.writerow(zip_labels)
        for gender in genList:
            genAvg = ["gender {:d}".format(gender)]
            for zip in zip_labels:
                try:
                    genAvg.append(meanGift[zip][gender])
                except KeyError:
                    continue
            csvwriter.writerow(genAvg)
        outcsv.close()
    sns.boxplot(x = 'zip_all', y = "AVGGIFT", hue = "gender dummy", data = donors)
    plt.show()
