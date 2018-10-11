#sample code to read csv file into 

import csv

with open('stockinput.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    stocks = []
    colors = []
    for row in readCSV:
        stock = row[0]

        stocks.append(stock)

    print(stocks)

    # now, remember our lists?

    whatstock = input('What color do you wish to know the date of?:')
    stockex = stocks.index(whatstock)
    print('The stock is ',whatstock,' .')