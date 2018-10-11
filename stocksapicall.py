#module to call stock input api
def call_stock_api(stock_symbol):
	import json
	import requests
	import csv
	s = stock_symbol
	a = "https://api.iextrading.com/1.0/stock/"
	b = "/stats"
	apicall = a+s+b
	response = requests.get(apicall)
	json_data = response.json()
	with open('test2.csv', 'w') as f:
		w = csv.DictWriter(f, json_data.keys())
	w.writeheader()
	w.writerow(json_data)
