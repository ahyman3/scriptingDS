# File Name: NBAfile.py
# Created By: Alex Hyman
# Created on: 13 Jul 2018
# Purpose: To read the nba attendance file and print out a string for
# each city that says the average attendance and the average ticket price
#
#
#
# Opening the nba attendance file
fhand = open('nba-attendance-1989.txt', 'r')
# parsing through each line in the nba attendance file
for line in fhand:
    # saving each of the entries in their own variable
    city, attend, price  = line.strip().split()
    # Printing out the statement replacing all underscores with a space,
    # converting the attendance into an integer, and the price into a float
    # with two decimal places
    print("The attendance in {:s} was {:d} and the ticket price \
was {:.2f}".format(city.replace("_", " "), int(attend), float(price)))
