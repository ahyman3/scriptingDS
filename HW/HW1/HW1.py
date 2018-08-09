'''
File Name: HW1.property
Created By: Alex Hyman
Created on: 7 Aug 2018
Purpose: To explore a the Donors_Data.csv file and answer some questions relating
to the data and provide some graphics

Questions:
1. How much are people in each zipcode donating to the university, and what does
the distribution look like by gender

Approach: We will create a csv file that outputs the mean of the average gift for
each gender number within each zipcode. We will also create a boxplot of the
average gift for each gender in each of the zip codes to show the spread

2. Does homeownership have an effect on the independent income variable in terms
in terms of the the response variable of lifetime donations to the school?

Approach: create a table for each of the income levels and produce a table that
includes the min, max, mean, median, sd of RAMNTALL for both categories of
homeowners and provide a boxplot
'''

import csv                          #Reading the csv
import pandas as pd                 #Pandas for data frames
import matplotlib.pyplot as plt     #For plotting
import seaborn as sns               #More for plotting
import numpy as np                  #For statistics


if __name__ == "__main__":

    ##Question 1

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
    #Creating a dictionary to organize the means for each zip and gender
    meanGift = {}
    #For each of the zip codes in the zip code list
    for zip in zip_labels:
        #with the zip code as the key, create an empty dictionary
        meanGift[zip] = {}
        #For each gender in the gender list
        for gender in genList:
            #find all the rows that have the same zip code as zip and the
            #same gender as the gender and retrieve the AVGGIFT
            allAvg = donors.loc[(donors["zip_all"] == zip) & \
                (donors["gender dummy"] == gender), "AVGGIFT"]
            #In the dictionary index the zipcode and gender and place the
            #average of the number in the dictionary
            meanGift[zip][gender] = np.mean(allAvg)
    #initializing the name of the output file
    outfile = 'genderZipGift.csv'
    #write a new csv file called genderZipGift
    with open(outfile, "w") as outcsv:
        #initializing the csv writer with the opened out file
        csvwriter = csv.writer(outcsv)
        #Writing the title on the first row
        csvwriter.writerow(["Average gift by Gender within Zipcode"])
        #Skipping two rows
        csvwriter.writerow([])
        csvwriter.writerow([])
        #in the zip_labels list, insert an empty string in the 0 index
        #to format the headers of the zip code
        zip_labels.insert(0, "")
        #write the labels for the zip code skipping the first column
        csvwriter.writerow(zip_labels)
        #For each of the genders in the gender list
        for gender in genList:
            #creating the gender label for the table in the list
            genAvg = ["gender {:d}".format(gender)]
            #For each zip code
            for zip in zip_labels:
                #There is an error with the empty string, so catching error
                try:
                    #Appending the mean AVGGIFT for each gender to the genAvg list
                    genAvg.append(meanGift[zip][gender])
                except KeyError:
                    #If there is an error, next in the zip_label
                    continue
            #After looping through the zip codes write the row in the csv file
            #that has the averages for that gender dummy
            csvwriter.writerow(genAvg)
        #After looping through the genders, close the file
        outcsv.close()
    #Create the boxplot with the zip code as the x-axis and the average gift
    #as the y-axis in the order of the zip_labels (except the ""). For each
    #zip code, also separate out by the gender in the zip code and use the
    #donors data frame as the source
    sns.boxplot(x = 'zip_all', y = "AVGGIFT", order = zip_labels[1:], \
        hue = "gender dummy", data = donors)
    #Saving the figure
    plt.savefig("zipBoxplot.png")

    ##Question 2
    #Create a dictionary for keeping track of statisitcs
    incomeHoStats = {}
    #list of stats we will calculate
    stats = ["count", "min", "max", "median", "mean", "sd", "Total Donations"]
    #List of all unique income levels
    incomeLevels = list(set(donors["INCOME"]))
    #categories for homeowners
    homeowner = [0,1]
    #Looping through incomeLevels
    for level in incomeLevels:
        #Create a dictionary inside of the dictionary with the income level as
        #the key to that dictionary
        incomeHoStats[level] = {}
        #inner looping through the homewoner status creating a dictionary for
        #each level of homeownership inside the dictionary created for the income
        #level main dict -> income level -> homeowner status
        for HOStatus in homeowner:
            #Creating an empty dictionary in the homeowner status dict to
            #contain the statisitcs income level -> homestatus -> statisitc
            incomeHoStats[level][HOStatus] = {}
            #indexing in pandas the rows that have the have the same income
            #and same homeowner status as specified by the loop above
            tempFrame = donors.loc[(donors["INCOME"] == level) & \
                (donors["homeowner dummy"] == HOStatus)]
            #Storing the count of instances in the count key
            incomeHoStats[level][HOStatus]["count"] = len(tempFrame)
            #Storing the minimum of instances in the min key
            incomeHoStats[level][HOStatus]["min"] = min(tempFrame["RAMNTALL"])
            #Storing the maximum of instances in the max key
            incomeHoStats[level][HOStatus]["max"] = max(tempFrame["RAMNTALL"])
            #Storing the mean of instances in the mean key
            incomeHoStats[level][HOStatus]["mean"] = np.mean(tempFrame["RAMNTALL"])
            #Storing the median of instances in the median key
            incomeHoStats[level][HOStatus]["median"] = np.median(tempFrame["RAMNTALL"])
            #Storing the sd of instances in the sd key
            incomeHoStats[level][HOStatus]["sd"] = np.std(tempFrame["RAMNTALL"])
            #Storing the total $ amount of donations in that class to the Total
            #Donations key
            incomeHoStats[level][HOStatus]["Total Donations"] = sum(tempFrame["RAMNTALL"])
    #initializing the name of the second out file
    outfile2 = "incomeHomeownerDonations.csv"
    #writing the csv file for an output
    with open(outfile2, "w") as csvout2:
        #initializing the csv writer
        csvwriter = csv.writer(csvout2)
        #Creating a title for the file
        csvwriter.writerow(["Lifetime Donation Statistics"])
        #Leaving a space
        csvwriter.writerow([""])
        #Writing a title for the table
        csvwriter.writerow(["Lifetime Donations for Non-Homeowners"])
        #initializing the header for the table
        header = ["Income Levels"]
        #extending the header list to include the income levels
        header.extend(incomeLevels)
        #Writing the header
        csvwriter.writerow(header)
        #for each of the statistics in stats
        for stat in stats:
            #Start an empty list
            statRow = []
            #for each income level
            for income in incomeLevels:
                #in the dictionary using income level -> homeowner status -> statistic
                #find the statisitc for the group and append it to the statRow
                #list
                statRow.append(incomeHoStats[income][0][stat])
            #Add the name of the statvto the 0 index of the statRow list
            statRow.insert(0, stat)
            #Write the row in the csv file
            csvwriter.writerow(statRow)
        #Leaving a blank row to separate the table for homeowner table
        csvwriter.writerow([""])
        #writing the title in the csv file
        csvwriter.writerow(["Lifetime Donations for Homeowners"])
        #Writing the header for the second table
        csvwriter.writerow(header)
        #looping through each statisitc
        for stat in stats:
            #Create an empty list to place the statistic for each income level
            statRow = []
            #for each income level
            for income in incomeLevels:
                #find the statistic using income level -> homeownership -> stat
                #and append it to the statRow list
                statRow.append(incomeHoStats[income][1][stat])
            #add the statistic name to the 0 index of the list
            statRow.insert(0, stat)
            #Write the row in the csv file that has the statistic name followed by
            #the statistic for the omeowners in  the corresponding income level
            csvwriter.writerow(statRow)
        #close the file
        csvout2.close()
    #Create a boxplot that has the distribution of total donations for each level
    #of INCOME separated by homeowner status
    bp = sns.boxplot(x = "INCOME", y = "RAMNTALL", hue = "homeowner dummy", data = donors)
    #getting the handle and labels for the legend
    handles, labels = bp.get_legend_handles_labels()
    #Getting rid of the duplicates and settingt the labels
    l = plt.legend(handles[0:2], ["Non-Homeowner", "Homeowner"], loc=0, borderaxespad=0.)
    #Saving the figure
    plt.savefig("LifetimeDonations_Income.png")
