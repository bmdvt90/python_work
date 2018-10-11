#Create Dictionary
stocksdict = {}
newstocksdict ={}
temp = ""
#companyName,marketcap,week52high,week52low,dividendRate,dividendYield,latestEPS,returnOnEquity,symbol,EBITDA,revenue,grossProfit,cash,debt,ttmEPS,revenuePerShare,revenuePerEmployee,returnOnAssets,profitMargin,priceToSales,priceToBook
# Add keyvalue pairs to dictionary
stocksdict["companyName"] = "Accenture"
stocksdict["symbol"] = "ACN"
stocksdict["marketcap"] = 300000000
stocksdict["week52high"] = 163.75
print(stocksdict.get("companyName"))
#? How do I assign the value of a dictionary to a variable/temp value?
temp = stocksdict["companyName"]
newstocksdict["Company_Name"] = stocksdict["companyName"]
newstocksdict["Symbol"] = stocksdict["symbol"]
print(newstocksdict)