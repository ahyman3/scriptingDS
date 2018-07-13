# File name: pay.py
# Create on: 13 Jul 2018
# Created By: Alex Hyman
# Purpose: Take user inputs for rate and hours and calculate the amount
# of money they had made for the week
#
#
#
hrs = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
print("Pay: {:.2f}".format(hrs * rate))
