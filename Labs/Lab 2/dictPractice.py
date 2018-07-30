#File name: dict.py
#Created By: Alex Hyman
#Created on 30 Jul 2018
#Purpose: Lab #2, show proficiencies with dictionaries

if __name__ == "__main__":
    #Initializing the dictionaries
    stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
    prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

    #a. Show the expression that gets the value of the stock dictionary at the
    #key ‘orange’. Show a statement that adds an item to the stock dictionary
    #called ‘cherry’ with some integer value and that adds ‘cherry’ to the prices
    #dictionary with a numeric value. (Or pick your own fruit name.)

    #indexing orange on stock
    print("There are {:d} oranges in stock".format(stock["orange"]))

    #adding cheries to prices
    prices["cherries"] = 7
    print("Cherries are now ${:.2f}".format(prices["cherries"]))

    #b. Write the code for a loop that iterates over the stock dictionary and
    #prints each key and value.

    #starting loop
    for key, value in stock.items():
        #printing each key and value using from the items method
        print("key: {:s}\tprice: {:d}".format(key, value))

    #c. Suppose that we have a list:
    groceries = ["apple", "banana", "pear"]
    #Write the code that will sum the total number in stock of the items in the
    #groceries list.

    #Starting the summation at 0
    totStock = 0
    #Looping through the groceries list
    for item in groceries:
        #getting the item from the stock, if not there make it zero
        totStock += stock.get(item, 0)
    print("There are {:d} items from the grocery list in stock".format(totStock))

    #d. Write the code that can print out the total value in stock of all the
    #items. This program can iterate over the stock dictionary and for each item
    #multiply the number in stock times the price of that item in the prices
    #dictionary. (This can include the items for ‘cherry’ or not, as you choose.)

    #Initializing the price
    totPrice = 0
    #Looping through all they keys in stock
    for item in stock.keys():
        #multiplying the price
        totPrice += stock.get(item, 0) * prices.get(item, 0)
    #printing total price of the stock
    print("The total price of the stock is ${:.2f}".format(totPrice))
