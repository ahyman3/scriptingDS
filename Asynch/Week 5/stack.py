import pandas as pd

#If the file is the main file
if __name__ == "__main__":
    #creating the person dictionary
    persondict = {'person':['Bob','Alice','Steve'],
        'age':[32, 24, 64], 'weight':[128, 86, 95]}
    #Converting teh dictionary into the DataFrame
    df = pd.DataFrame(persondict, columns = ["person", "age", "weight"])
    #Setting the index for the data frame to person
    df = df.set_index("person")
    #Printing the data frame
    print("Data frame:")
    print(df,"\n")
    #Stacking the data frame
    result = df.stack()
    #Getting rid of the indexes
    dfStacked = result.reset_index()
    #Naming the columns
    dfStacked.columns = ["person", "attribute", "value"]
    #Printing the stacked columns with the named columns
    print("Stacked data frame:")
    print(dfStacked,"\n")
    #Unstacking the stacked data frame
    dfUnstacked = result.unstack()
    #Resetting the index
    dfUnstacked = dfUnstacked.reset_index()
    #Printing the unstacked data frame
    print("Unstacked data frame")
    print(dfUnstacked,"\n")
    #Pivoting the stacked data frame
    dfPivot = dfStacked.pivot("person", "attribute", "value")
    #Printing the pivot table
    print("Pivot data frame: ")
    print(dfPivot, "\n")
