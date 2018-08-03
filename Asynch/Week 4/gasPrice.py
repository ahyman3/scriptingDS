import numpy as np
import csv
import matplotlib.pyplot as plt

if __name__ == "__main__":
    filename = 'price_of_gasoline.xl.csv'
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
        "Oct", "Nov", "Dec"]
    years = []
    prices = []
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter = ',')
        for item in lines:
            if item[0] is "" or item[0] == "Year" or item[0].startswith("Price"):
                continue
            elif int(item[0]) > 2000:
                continue
            else:
                try:
                    years.append(int(item[0]))
                    prices.append(item[1:])
                except IndexError:
                    print("Error", item)
    csvfile.close()
    data = np.array(prices)
    data[data == ""] = 0
    data = data.astype(np.float)
    avgPrice = []
    for i, year in enumerate(years):
        print("The average gas price in {:d} was ${:.2f}".format(year, np.sum(data[i,:]) / data.shape[1]))
        avgPrice.append(np.sum(data[i,:]) / data.shape[1])
    plt.plot(years, avgPrice)
    plt.show()
