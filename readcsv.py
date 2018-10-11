# Read the stock symbols from the file into a list
def readcsv():
	pass
import csv
with open('stockinput.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    stocks = []
    for row in readCSV:
        stock = row[0]
        stocks.append(stock)
#for each stock in the list call API to gather data
#    for row in stocks:
#        print(row)
