'''
Filename: scraping.py
Created by: Alex hyman
Created on: 23 August 2018
Purpose: Only donations over a certain amount can be itemized, therefore it is
necessary to scrape the FEC website for aggregated data of itemized and unitemized
donations. The candidateIDs were extracted from the cleaned data.
'''
import pandas as pd

#Creating a function  to take a candidate id, and create a url with the pattern
#For the fec website and reading some information on them
def get_candidate_info(id):
    #C reating url string
    url = "http://www.fec.gov/data/candidate/" + id
    #Using pandas to read the table
    tables = pd.read_html(url)
    #Getting the first table
    table =  tables[0]
    #Getting the total amount of money raised by the candidate
    moneyRaised = table.at[0,1]
    #Getting the total raised from individuals
    totalIndividuals = table.at[2,1]
    #Getting the total amount of money raised by pacs
    partyDonations = table.at[5,1]
    #Returning the ID, all money raised, money raised by individual, and money
    #Raised by pacs
    pacDonations = table.at[6,1]
    return (id, moneyRaised, totalIndividuals, partyDonations, pacDonations)


if __name__ == "__main__":
    #Reading the file for house members
    house = pd.read_csv("data/transformed/houseSummary.tsv", delimiter= "\t")
    #Reading the file for senators
    senate = pd.read_csv("data/transformed/senatorsData.tsv", delimiter="\t")
    #Getting the ids for house candidates
    houseIDs = list(house["id"])
    #Getting the ids for senate candidates
    senateIDs = list(senate["id"])
    #creating an empty list for the house ids
    ids = []
    #Creatinf an empty list for the amount raised overall
    totalReceipts = []
    #Creating a list of total individual donations
    individualDonations = []
    #List of pac donations
    pacDonations = []
    #creating an empty list for saving
    dflist = []
    #For each of the unique house ids

    for id in houseIDs:
        #Print the so we can check status
        print(id)
        #try to
        try:
            #Append the candidate info to the list
            dflist.append(get_candidate_info(id))
        #Except error
        except:
            #Go to next candidate
            continue
    #Convert the list of scraped candidate info into a data frame
    houseDF = pd.DataFrame(dflist, columns=["id", "allRaised","allIndividuals", "PartyDonations", "PACDonations"])
    #And merge the scraped data with the existing data
    house_all = pd.merge(house, houseDF, on="id", how = "left")
    #conver the merged data frame into a new tsv file
    house_all.to_csv("data/transformed/houseScraping.tsv", sep= "\t")

    #Repeat above for senators
    dflist = []
    for id in senateIDs:
        try:
            item = get_candidate_info(id)
            print(item)
            dflist.append(item)
        except:
            continue
    senateDF = pd.DataFrame(dflist, columns=["id", "allRaised",
"allIndividuals", "PartyDonations", "PACDonations"])
    senate_all = pd.merge(senate, senateDF, on="id", how = "left")
    senate_all.to_csv("data/transformed/senateScraping.tsv", sep= "\t")
