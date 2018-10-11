#Control program for stock assessment project
#Read Stock symbols into a list
import csv, json, requests, time
import pandas as pd
#Establish the dictionary in order to print the header once in the loop
localtime = time.asctime( time.localtime(time.time()) )
print("Start Time" + localtime)
stocksdict = {}
stocksdict["Symbol"] = ""
stocksdict["Company_Name"] = ""
stocksdict["LastSale"] = 0
stocksdict["Sector"] = ""
stocksdict["Industry"] = ""
stocksdict["Market_Cap"] = 0
stocksdict["Week52_High"] = 0
stocksdict["Week52_Low"] = 0
stocksdict["Dividend_Rate"] = 0
stocksdict["Dividend_Yield"] = 0
stocksdict["EPS"] = 0
stocksdict["EPS_TTM"] = 0
stocksdict["ROE"] = 0
stocksdict["ROA"] = 0
stocksdict["EBITDA"] = 0
stocksdict["Revenue"] = 0
stocksdict["Revenue_PS"] = 0
stocksdict["Revenue_PE"] = 0
stocksdict["Gross_Profit"] = 0
stocksdict["profitMargin"] = 0
stocksdict["Cash"] = 0
stocksdict["Debt"] = 0
stocksdict["Price_to_Sales"] = 0
stocksdict["Price_To_Book"] = 0
#import input to pandas dataframe
df = pd.read_csv('datafiles\\input\\nyse.csv',index_col="Symbol")
inputlist = df.index.get_values()
# open input file and read stock symbols into a list
#with open('datafiles\input\stockprospectlist.csv') as csvfile:
#    readCSV = csv.reader(csvfile, delimiter=',')
#    stocks = []
# read the list and call stock API for each stock
# Open the outputfile for and write the header row
with open('datafiles\output\stockoutputdata.csv', 'w') as f:
	w = csv.DictWriter(f, stocksdict.keys())
	w.writeheader()
	for row in inputlist:
		response = ''
		json_data = ''
		lastsale = df.loc[row,"LastSale"]
		sector = df.loc[row,"Sector"]
		industry = df.loc[row,"Industry"]
		stock = row
# Call Stock API for requested metrics
		response = requests.get("https://api.iextrading.com/1.0/stock/" + stock + "/stats")
		if response.status_code == 200:
			json_data = response.json()
# Copy the called data into a dictionary
			stocksdict["Symbol"] = json_data["symbol"]
			stocksdict["Company_Name"] = json_data["companyName"]
			stocksdict["Sector"] = sector
			stocksdict["Industry"] = industry
			stocksdict["Market_Cap"] = json_data["marketcap"]
			stocksdict["LastSale"] = lastsale
			stocksdict["Week52_High"] = json_data["week52high"]
			stocksdict["Week52_Low"] = json_data["week52low"]
			stocksdict["Dividend_Rate"] = json_data["dividendRate"]
			stocksdict["Dividend_Yield"] = json_data["dividendYield"]
			stocksdict["EPS"] = json_data["latestEPS"]
			stocksdict["EPS_TTM"] = json_data["ttmEPS"]
			stocksdict["ROE"] = json_data["returnOnEquity"]
			stocksdict["ROA"] = json_data["returnOnAssets"]
			stocksdict["EBITDA"] = json_data["EBITDA"]
			stocksdict["Revenue"] = json_data["revenue"]
			stocksdict["Revenue_PS"] = json_data["revenuePerShare"]
			stocksdict["Revenue_PE"] = json_data["revenuePerEmployee"]
			stocksdict["Gross_Profit"] = json_data["grossProfit"]
			stocksdict["profitMargin"] = json_data["profitMargin"]
			stocksdict["Cash"] = json_data["cash"]
			stocksdict["Debt"] = json_data["debt"]
			stocksdict["Price_to_Sales"] = json_data["priceToSales"]
			stocksdict["Price_To_Book"] = json_data["priceToBook"]
# Verify the stocks qualify based on the following criteria
			if stocksdict["Dividend_Yield"] > 3:
				if stocksdict["Market_Cap"] > 300000000:
					if stocksdict["ROA"] > 0:
						if stocksdict["EPS"] > 0:
# Write the dictionary results to the output file
								w.writerow(stocksdict)
			else :
				print(stocksdict["Company_Name"] + " does not qualify for further analysis")
		else :
			print(stocksdict["Company_Name"] + " does not qualify for further analysis for error " + str(response.status_code))
# End of loop
print("All Stocks Complete")
localtime = time.asctime( time.localtime(time.time()) )
print("End Time" + localtime)
# End of Program