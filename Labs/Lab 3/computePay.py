'''
File Name: computePay.py
Created on: 31 Jul 2018
Created By: Alex Hyman
Purpose: To calculate the pay given the hours and a rate. This will be defined
in a function called computePay and will include overtime
'''

#Defining the function
def computePay(hours, rate):
    #if statement to see if we need to implement overtime
    if hours > 40:
        #If there is overtime, looking at how many ot hours
        ot = hours - 40
        #total pay is 40 hrs * normal rate + ot hours * 1.5 * normal rate
        pay = 40 * rate + ot * 1.5 * rate
        #Printing the formatted pay
        print("Pay: ${:.2f}".format(pay))
    else:
        #Normal calculation of rate * hours
        print("Pay: ${:.2f}".format(hours * rate))

#If this is our main file
if __name__ == '__main__':
    #We will run this script until tryAgain is false
    tryAgain = True
    #Starting while loop
    while tryAgain:
        #Enter the hours
        hours = input("Enter hours: ")
        #Enter the rate
        rate = input("Enter rate: ")
        #Make sure we can convert the rate and hours
        try:
            hours = float(hours)
            rate = float(rate)
            #If we can convert, use the function
            computePay(hours, rate)
            #No longer have to keep trying to get the rate and hours
            tryAgain = False
        except:
            #We could not convert and we will start the loop over
            print("Enter a correct number\n")
