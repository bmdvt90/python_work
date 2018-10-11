#Sample code to call API

#import urllib.request
#with urllib.request.urlopen('https://etrade.com/market/rest/quote/MSFT?detailFlag=ALL') as response:
#   html = response.read()
# Make a get request to get the latest position of the international space station from the opennotify api.
import json
import requests
import csv
response = requests.get('https://api.iextrading.com/1.0/stock/acn/stats')
json_data = response.json()
# Print the status code of the response.
#print(json_data)
#print("\n===================")
with open('test.csv', 'w') as f:
#    f.write('Application Name, Application ID\n')
    for key in json_data.keys():
        f.write("%s,%s\n"%(key,json_data.values))
"""
f = open('output.csv','wb')
w = csv.DictWriter(f,json_data.keys())
w.writerow(json_data)
f.close()
#
#for k, v in json_data.items():
#for v in json_data.values():
#	print("\nKey: " + k)
#	print("Value: " + str(v))
#	print(v)
#use this example to load keys to a list for printing headers
# do something similar for values to load to a list and write to CSV
"""