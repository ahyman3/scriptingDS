'''
filename: transforming_candidates.py
created on: 20 Aug 2018
Created by: Alex hyman
Purpose: to read in the cleaned candidate information as well as the committees
and individual donations files and create a merged summary file that has the
itemized candiate donations from individuals broken down into total itemized
donations, in-state donation amount and count, as well as out of state donation
amounts and counts. This will all be saved to as tsv file named
candidateSummary2.tsv 
'''

import pandas as pd
import numpy as np
import csv
import os


if __name__ == "__main__":
    #Reading a csv of the candidates
    candidates = pd.read_csv("data/cleaned/candidates.csv")
    #Reading in a data frame of the committees
    committees = pd.read_csv("data/cleaned/committees.csv")
    #Reading in the data frame that connects candidates to committees
    fk = pd.read_csv("data/cleaned/cand_committee.csv")

    #Merging the committees with the connecting df and keeping all of the connecting
    #rows
    com_fk = pd.merge(fk, committees, "left", on = "CMTE_ID")
    #Dropping the duplicated column names
    com_fk = com_fk.drop(["CAND_ID_y", "CMTE_TP_x", "CMTE_DSGN_x"], axis =1)
    #Renameing transformed column names
    com_fk = com_fk.rename(columns={"CAND_ID_x":"CAND_ID", "CMTE_TP_y":"CMTE_TP", "CMTE_DSGN_y":"CMTE_DSGN"})

    #Creating data frame that merges the candidates with the committees and keeping
    #all the candidates
    candidatesCom = pd.merge(candidates, com_fk, "left", on = "CAND_ID")
    #creating a final data frame that has all the candidates connected to their
    #committees
    candidates = candidatesCom[["CAND_ID", "CAND_NAME", "CAND_ICI", "CAND_PTY_AFFILIATION","CAND_OFFICE_ST",
                             "CAND_OFFICE_DISTRICT", "FEC_ELECTION_YR", "CMTE_ID", "CMTE_NM", "CMTE_TP"]]
    #Creating a list of unique candidate ids. Some candidates can have multiple
    #committees
    candIDs = list(set(candidates["CAND_ID"]))
    #Empty dictionary to store candidates with the key being their candidate id
    candict = {}
    #For each of the unique ids
    for id in candIDs:
        #index on candidates the name, party, office, and district
        needCols = candidates.loc[candidates["CAND_ID"] == id, ["CAND_NAME", "CAND_PTY_AFFILIATION", "CAND_OFFICE_ST",
                                 "CAND_OFFICE_DISTRICT"]]
        #Create a dictionary specific for the candidate in the candict dictionary
        #outside of the loop
        candict[id] = {}
        #And save their name
        candict[id]["name"] = needCols.iloc[0,0]
        #party
        candict[id]["party"] = needCols.iloc[0,1]
        #and state inside the dictionary
        candict[id]["state"] = needCols.iloc[0,2]

    #Read the doantions pacs made
    pacDonations = pd.read_csv("data/cleaned/pac_donations.csv")
    #And for each candidate id
    for id in candIDs:
        #Find all the donations that the pacs made to a candidate and sum is
        pacTotal = pacDonations.loc[pacDonations["CAND_ID"] == id, "TRANSACTION_AMT"].sum()
        #Count the number of donations
        numDonations = pacDonations.loc[pacDonations["CAND_ID"] == id, "TRANSACTION_AMT"].count()
        #And count the number of different pacs
        numPacs = len(set(pacDonations.loc[pacDonations["CAND_ID"] == id, "CMTE_ID"]))
        #Save these in the candict dictionary
        candict[id]["pacDonations"] = pacTotal
        candict[id]["numPacDonations"] = numDonations
        candict[id]["numPacs"] = numDonations

    #Making a more narrow data frame for the candidates
    candTemp = candidates[["CMTE_ID", "CAND_ID", "CAND_PTY_AFFILIATION", "CAND_OFFICE_ST"]]

    #Creating a function that takes in a filename and a dictionary
    def individualSummations(filename, dictionary, candTemp):
        #Reading file of civillian donors
        individuals = pd.read_csv(filename)
        #Keeps the cmte, city, state, and transaction amount for each civillian
        #donation
        individuals = individuals[["CMTE_ID", "CITY", "STATE", "TRANSACTION_AMT"]]
        #Merging the individuals with the candidates to make sure that these
        #are only donations that went directly to a candidate committee
        individualsNew = pd.merge(candTemp, individuals, how = "left", on = "CMTE_ID")
        #Getting rid of any rows that do not have a transaction amount
        individualsNew = individualsNew.dropna(subset = ["TRANSACTION_AMT"])
        #Getting a list of the candidates in the file
        candDonations = list(set(individualsNew["CAND_ID"]))
        #For each of the candidates that received a donation
        for cand in candDonations:
            #find all the donations to that candidate
            candAll = individualsNew.loc[individualsNew["CAND_ID"] == cand, ]
            #save in the dictionary the sum of all itemized donations
            dictionary[cand]["totalDonations"] = candict[cand].get("totalDonations", 0)  + candAll["TRANSACTION_AMT"].sum()
            #Save in the dictionary the sum of all itemized donations within their
            #state
            dictionary[cand]["localDonations"] = candict[cand].get("localDonations", 0) + \
                candAll.loc[candAll["CAND_OFFICE_ST"] == candAll["STATE"], "TRANSACTION_AMT"].sum()
            #Count the number of different donations from inside the state
            dictionary[cand]["localCount"] = candict[cand].get("localCount", 0) + \
                candAll.loc[candAll["CAND_OFFICE_ST"] == candAll["STATE"], "TRANSACTION_AMT"].count()
            #The the amount of donations from individuals outside of the state
            dictionary[cand]["oosDonations"] = candict[cand].get("oosDonations", 0) + \
                candAll.loc[candAll["CAND_OFFICE_ST"] != candAll["STATE"], "TRANSACTION_AMT"].sum()
            #Count the number of donations from outside the state
            dictionary[cand]["oosCount"] = candict[cand].get("oosCount", 0) + \
                candAll.loc[candAll["CAND_OFFICE_ST"] != candAll["STATE"], "TRANSACTION_AMT"].count()

    #Listing all the files in the individuals folder because too big to store in
    #one file
    files = os.listdir("data/cleaned/individuals")
    #For each of the five files
    for file in files:
        #Create the file name with the proper file path
        file = "data/cleaned/individuals/" + file
        #Run the individuals donations function on that file so all the
        #Individual donations to candidates are aggregated
        individualSummations(file, candict, candTemp)

    #For each of the unique candidates
    for id in candIDs:
        #Try
        try:
            #and see if the candidate had all the fields full
            if len(candict[id]) < 11:
                #Then they did not have any individual donations, so make it 0
                candict[id]["totalDonations"] = 0
                candict[id]["localDonations"] = 0
                candict[id]["localCount"] = 0
                candict[id]["oosDonations"] = 0
                candict[id]["oosCount"] = 0
            #if the candidate does not have a state (presidential candidate),
            #or did not have any individual donations and they had not received
            #any money from PACs
            if candict[id]["state"] == '00' or (candict[id]["totalDonations"] == 0 and candict[id]["pacDonations"] == 0):
                #get rid of that candidate
                candict.pop(id)
        except:
            #If there are issues, skip
            continue
    #creating a list to save as a file
    candidatesOut = []
    #Starting a header list with id because id not in dictionary
    candidate = ["id"]
    #Extend the header list to include the keys in a candidate
    candidate.extend(list(candict["H0AL05163"].keys()))
    #append the header list to the list to be saved
    candidatesOut.append(candidate)
    #For each of the candidates in the unique list
    for id in candIDs:
        #Try to
        try:
            #make a list starting with just the candidate id
            candidate = [id]
            #And extend this list with the values saved in the dictionary for this
            candidate.extend(candict[id].values())
            #Append the candidate information to the list to be saved
            candidatesOut.append(candidate)
        #If the candidate is not in the dictionary, then skip
        except:
            continue
    #open a file tsv file to write out
    with open("data/transformed/candidateSummary2.tsv", "w") as candfile:
        #Create an object to write csvs
        csvwriter = csv.writer(candfile, delimiter = "\t")
        #Write each item in the list into the file
        for line in candidatesOut:
            csvwriter.writerow(line)
        #close the file
        candfile.close()
