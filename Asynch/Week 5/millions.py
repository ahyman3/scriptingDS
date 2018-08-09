import pandas as pd
import csv

if __name__ == "__main__":
    #initializing the infile name
    infile = "albb.salaries.2003.tsv"
    #empty team list to append team of players salary under 310000
    teamsList = []
    #empty player list to append player names under 310000
    playerList = []
    #empty salary list to append salaries for the players under 310000
    salaryList = []
    #empty position list to append team of position salary under 310000
    positionList = []
    #opening the file
    with open(infile, "r") as csvfile:
        #using the scv library to go through each line to filter nonapplicable players
        csvreader = csv.reader(csvfile, delimiter = "\t")
        #looping through each line in the csv file
        for player in csvreader:
            #Trying to see if able to convert to int
            try:
                #replacing the commas
                salary = player[2].replace(",", "")
                #converting to integer
                salary = int(salary)
                #If the salary less than 310000
                if salary < 310000:
                    #then append the team name from the csv file to the
                    #playerList
                    teamsList.append(player[0])
                    #then append the player name from the csv file to the
                    #playerList
                    playerList.append(player[1])
                    #then append the salary from the csv file to the
                    #salaryList
                    salaryList.append(player[2])
                    #then append the position  from the csv file to the
                    #positionList
                    positionList.append(player[3])
                #otherwise go to the next line
                else:
                    continue
            #If cannot convert to the integer, go to next line
            except:
                continue
        #Closing the csvfile
        csvfile.close()
    #opening the file to write
    with open("under-million.csv", "w") as fout:
        #Creating the the csv file for the output
        csvwriter = csv.writer(fout, delimiter = ",", quoting = csv.QUOTE_MINIMAL)
        #Writing the title fo the scv file
        csvwriter.writerow(["Players under $310,000"])
        #Creating a blank row x2
        csvwriter.writerow([])
        csvwriter.writerow([])
        #Creating the table header
        csvwriter.writerow(["Team", "Player", "Salary", "Position"])
        #going through eachbline in the player/salary list
        for team, player, salary, position in zip(teamsList, playerList, \
            salaryList, positionList):
            #writing the entry for the salary and name
            csvwriter.writerow([team, player, salary, position])
        #Closing the file
        fout.close()
    #Starting empty pitcher list
    pitcherList = []
    #opeining the million csv that was created
    with open("under-million.csv", "r") as fout2:
        #initializing the csv reader
        csvreader2 = csv.reader(fout2, delimiter = ",")
        #going through each of the lines in the csv reader
        for items in csvreader2:
            #If able to index
            try:
                #If they are a pitcher append to the pitcher list
                if items[3] == "Pitcher":
                    #appending the entire line to the pitcher list
                    pitcherList.append(items)
                    #otherwise next in loop
                else:
                    continue
            except IndexError:
                continue
    #Initialize the output file
    with open("Pitchers.csv", "w") as csvout2:
        #Creating the csvwriter
        csvwriter2 = csv.writer(csvout2, delimiter = ",", quoting = csv.QUOTE_MINIMAL)
        #Header for the csv file
        csvwriter2.writerow(["Pitchers under $310,000"])
        #Skipping 2 rows
        csvwriter2.writerow([""])
        csvwriter2.writerow([""])
        #Writing the header for the table
        csvwriter2.writerow(["Team", "Player", "Salary"])
        #For all teh pitchers in the pitcherList
        for line in pitcherList:
            #write the team name, player name, and salary
            csvwriter2.writerow(line[0:3])
        #Closing out the file
        csvout2.close()
