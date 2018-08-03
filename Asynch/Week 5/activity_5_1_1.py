import pandas as pd

#Defining the function to replace the commas
def str_replace(string):
    return string.replace(",", "")


if __name__ == "__main__":
    #Creating the dictionary to convert into a data frame
    state_data = {'State':['Alabama','Alaska','Arizona','Arkansas'],
        'PostCode':['AL','AK','AZ','AR'],'Area':['52,423','656,424','*','53,182'],
        'Pop':['4,040,587','550,043','3,665,228','2,350,750']}
    #creating the data frame with pandas using the dictionary as the data source
    #and providing the columns names to match
    df = pd.DataFrame(state_data, ["State", "PostCode", "Area", "Pop"])
    #Setting the states as the indexes
    df = df.set_index("State")
    #Replacing the * with 0
    df["Area"] = df["Area"].replace('*','0')
    #applying the str replace to all the items in column Pop and converting it
    #To an integer
    df["Pop"] = pd.to_numeric(df["Pop"].map(str_replace))
    ##Replacing all the commas in the Area column and converting into integer
    df["Area"] = pd.to_numeric(df["Area"].map(str_replace))
    #Printing the data frame
    print(df)
