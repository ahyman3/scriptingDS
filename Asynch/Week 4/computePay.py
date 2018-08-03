'''
File Name: computePay.py
Created on: 31 Jul 2018
Created By: Alex Hyman
Purpose: To calculate the pay given the hours and a rate. This will be defined
in a function called computePay and will include overtime
'''

def computePay(hours, rate):
    if hours > 40:
        ot = hours - 40
        pay = 40 * rate + ot * 1.5 * rate
        print("Pay: ${:.2f}".format(pay))
    else:
        print("Pay: ${:.2f}".format(hours * rate))

if __name__ == '__main__':
    tryAgain = True
    while tryAgain:
        hours = input("Enter hours: ")
        rate = input("Enter rate: ")
        try:
            hours = float(hours)
            rate = float(rate)
            computePay(hours, rate)
            tryAgain = False
        except:
            print("Enter a correct number\n")
