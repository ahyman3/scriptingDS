# File name: nbaClass.py
# Created by: Alex Hyman
# Created on: 13 Jul 2018
# Purpose: To read the data, store in list and strip the white space
#
#
#
#Opening the file
fhand = open('nba-attendance-1989.txt', 'r')
# Creating the empty list
nba = []
for line in fhand:
    # Getting rid of the whitespace to the left and right on every line
    line = line.strip()
    # Creating a list that separates each word at the whitespace
    items = line.split()
    # Appending the list for one line to the nba lis
    nba.append(items)
for item in nba:
    # Printing all the information at each line
    print(item)
