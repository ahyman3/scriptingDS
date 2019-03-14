'''
Filename: grouping.py
Created on: 3 September 2018
Created by: Alex Hyman
Purpose: To group the candidates by state, party and race and find out how much
money has been raised in that race
'''
import pandas as pd

if __name__ == "__main__":
    #Read the senate and house summaries
    house = pd.read_csv("data/final summary/HouseSummary.csv")
    senate = pd.read_csv("data/final summary/SenateSummary.csv")
    #group the house by the party, state, and district
    houseSummary = house.drop("Unnamed: 0", axis = 1).groupby(["party", "state",
        "CAND_OFFICE_DISTRICT"], as_index=False).sum()
    #Making the district an integer
    houseSummary["CAND_OFFICE_DISTRICT"] = houseSummary["CAND_OFFICE_DISTRICT"].astype("int")
    #group senate by party and state
    senateSummary = senate.drop("Unnamed: 0", axis = 1).groupby(["party", "state"],
     as_index=False).sum()
    #Saving the grouped data to a csv
    houseSummary.to_csv("data/final summary/HouseGrouped.csv", index = False)
    senateSummary.to_csv("data/final summary/SenateGrouped.csv", index = False)
    
