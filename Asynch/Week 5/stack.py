import pandas as pd

if __name__ == "__main__":
    persondict = {'person':['Bob','Alice','Steve'],
        'age':[32, 24, 64], 'weight':[128, 86, 95]}
    df = pd.DataFrame(persondict, columns = ["person", "age", "weight"])
    df = df.set_index("person")
    print(df)
    result = df.stack()
    dfStacked = result.reset_index()
    dfStacked.columns = ["person", "attribute", "value"]
    print(dfStacked)
    dfUnstacked = result.unstack()
    dfUnstacked = dfUnstacked.reset_index()
    print(dfUnstacked)
    print(dfUnstacked.pivot("person"))
