def categorize(vec):
    unique = set(vec)
    print("The total is {:d}".format(sum(vec)))
    print("The average is {:.2f}".format(sum(vec)/len(vec)))
    countVec = {}
    for num in vec:
        countVec[num] = countVec.get(num, 0) + 1
    for num in unique:
        print("There are {:d} {:d}'s'".format(countVec[num], num))




if __name__ == "__main__":
    vec = []
    num = input("Enter Number: ")
    while num != 'done':
        try:
            num = int(num)
            vec.append(num)
            num = input("Enter Number: ")
        except:
            print("Enter a number\n")
    categorize(vec)
