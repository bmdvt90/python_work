#Control program for stock assessment project
#Read Stock symbols into a list
import csv, json, requests
#Establish the dictionary in order to print the header once in the loop

# open input file and read stock symbols into a list
with open('stockprospectlist.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    stocks = []
    for row in readCSV:
        stock = row[0]
        stocks.append(stock)
# read the list and call stock API for each stock
# Open the outputfile for and write the header row
for stock in stocks:
	response = ''
	json_data = ''
	print(stock)
# Call Stock API for requested metrics
	response = requests.get("https://api.iextrading.com/1.0/stock/" + stock + "/stats")
	if response.status_code == 200:
		json_data = response.json()
	else:
		print(stock + "error code")