'''
filename:election_cleaning.py
created on: 26 Aug 2018
created by: Alex Hyman
purpose: To separate the candidates to which chamber of congress they are running
for, either house pr senate
'''

import pandas as pd

if __name__ == "__main__":
    #Read the summarized candidates information
    candidateSummary = pd.read_csv("data/transformed/candidateSummary.tsv", delimiter = "\t")
    #Readin the cleaned candidates information
    candidatesAll = pd.read_csv("data/cleaned/candidates.csv")
    #Indexing all the campaigns for candidates that's id begins with S (senate)
    senate = donationSummary.loc[donationSummary.id.str[0] == "S", ]
    #Indexing all the campaigns for candidates that's id begins with H (house)
    house = donationSummary.loc[donationSummary.id.str[0] == "H", ]
    #States that have active senate races
    states = ["AZ", "CA", "CT", "DE", "FL", "HI", "IN", "ME", "MD", "MA", "MI", "MN",
                "MS", "MO", "MT", "NE", "NV", "NJ", "NM", "NY", "ND", "OH", "PA", "RI",
                "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    #indexing active senate campaigns that are in the states list
    activeSenate = senate.loc[senate["state"].isin(states), ]
    #Saving these to a senate file
    activeSenate.to_csv("data/transformed/senatorsData.tsv", sep = "\t")
    #Making a data frame with only the candidates that have a district and an id
    houseCandidates = candidatesAll[["CAND_ID", "CAND_OFFICE_DISTRICT"]]
    #Merging the house data frame with the districts data frame, essentially adding the
    #district the candidate is running in
    houseDistrict = pd.merge(house, houseCandidates, "left", left_on="id", right_on="CAND_ID")
    #dropping the redundant cand_id column
    houseDistrict = houseDistrict.drop("CAND_ID", axis = 1)
    #Saving the house data frame to a tsv file
    houseDistrict.to_csv("data/transformed/houseSummary.tsv", sep = "\t")
