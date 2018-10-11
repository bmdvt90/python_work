#Sample code to call API

#import urllib.request
#with urllib.request.urlopen('https://etrade.com/market/rest/quote/MSFT?detailFlag=ALL') as response:
#   html = response.read()
# Make a get request to get the latest position of the international space station from the opennotify api.
def stockcall():
	import json
	import requests
	import csv
s = "acn"
a = "https://api.iextrading.com/1.0/stock/"
b = "/stats"
apicall = a+s+b
response = requests.get(apicall)	
json_data = response.json()
#json_data = json.loads(response[0])
# Print the status code of the response.
# print(json_data)
#print("\n===================")
with open('test2.csv', 'w') as f:
#    f.write('Application Name, Application ID\n')
    	w = csv.DictWriter(f, json_data.keys())
    	w.writeheader()
    	w.writerow(json_data)
