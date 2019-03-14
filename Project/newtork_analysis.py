'''
Filename: network_analysis.py
Created on: 3 September 2018
Created by: Alex Hyman
Purpose: To utilize the itemized donations to get a summary of which states
donated to which party and in which state. This will give an idea of the
overall political leanings of the state, as opposed to how much a money from
out of state has a candidate raises.
'''

import pandas as pd

if __name__ == "__main__":
    #Naming all states
    states = ["AL", "AK" "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI",
                    "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA",
                    "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM",
                    "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD",
                    "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    #Reading in all donations
    donations = pd.read_csv("data/cleaned/individual_donations.csv")
    #indexing onlt the id they donated to, the state the donar lives in, and
    #the amount donated
    donations = donations[["CMTE_ID", "STATE", "TRANSACTION_AMT"]]
    #Getting only states that are in the united states (not territories)
    donations = donations.loc[donations["STATE"].isin(states),]
    #Reading the candidate committees matcher
    candidateCmtes = pd.read_csv("data/cleaned/cand_committee.csv")
    #Reading in all the candidates
    candidates = pd.read_csv("data/cleaned/candidates_full.csv")
    #Getting only candidates that are currently seeking election and are
    #in the united states (not territories) and indexing in, state and party
    candidates = candidates.loc[(candidates["CAND_ELECTION_YR"] == 2018) & (candidates["CAND_OFFICE_ST"].isin(states)),
        ["CAND_ID", "CAND_OFFICE_ST", "CAND_PTY_AFFILIATION"]]
    #merging candidates with their committees and keeping only matching entries
    candidates = pd.merge(candidates, candidateCmtes, on = "CAND_ID", how = "inner")
    #Merging donations with the candidate/committee
    donations = pd.merge(donations, candidates, on = "CMTE_ID", how = "inner")
    #Shrinking down candidate data frame
    donations = donations[["CAND_OFFICE_ST", "CAND_PTY_AFFILIATION", "STATE", "TRANSACTION_AMT"]]
    #Creating new column that is a combination of candidate state and party
    donations["ST-PARTY"] = donations.CAND_OFFICE_ST.map(str) + "-" + donations.CAND_PTY_AFFILIATION
    #Creating grouping for donations and candidate state and party
    donationsGrouped = donations.groupby(["STATE", "CAND_OFFICE_ST", "CAND_PTY_AFFILIATION", "ST-PARTY"], as_index=False)["TRANSACTION_AMT"].sum()
    #Changing name of TRANSACTION_AMT
    donationsGrouped["Total_Donations"] = donationsGrouped["TRANSACTION_AMT"]
    donationsGrouped = donationsGrouped.drop("TRANSACTION_AMT", axis = 1)
    #Reordering structure of data frame
    donationsGrouped = donationsGrouped[["STATE", "CAND_PTY_AFFILIATION", "CAND_OFFICE_ST", "ST-PARTY", "Total_Donations"]]
    #Getting only democrats, republicans and independents
    parties = ["DEM", "REP", "IND"]
    donationsGrouped = donationsGrouped.loc[donationsGrouped["CAND_PTY_AFFILIATION"].isin(parties), ]
    #Saving donationsGrouped to to_csv
    donationsGrouped.to_csv("data/final summary/StateItemizedMoney.csv", index = False)
