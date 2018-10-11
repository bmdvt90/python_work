import csv

data = {}

# open file of stocks and create reader
with open('stockinput.csv', 'rb') as f:
	reader = csv.reader(f, delimiter=',', quotechar='"', skipinitialspace=True)
# read header
header = reader.next()
# create list for each column
for name in header:
    data[name] = []
# read rows, append values to lists
for row in reader:
    for i, value in enumerate(row):
        data[header[i]].append(value)

# print result
for key, values in data.items():
   print ("\n\n%s\n-----" % key)
   for value in values:
      print(value)