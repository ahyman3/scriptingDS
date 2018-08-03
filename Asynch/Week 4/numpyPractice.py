import numpy as np

if __name__ == "__main__":
    #creating the array
    arr = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
    print(arr,"\n")

    #index slicing for last 2 rows and 3 and 4 column
    print(arr[-2:,2:4],"\n")

    #summing the columns
    print("Column sum: ", np.sum(arr, axis = 0))
