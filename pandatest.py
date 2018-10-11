# Import pandas library
import pandas as pd 
#import numpy as np
# Import the data
df = pd.read_csv('NYSE.csv',index_col='Symbol')
#stocks = nasdaq(Index).tolist()
# open input file and read stock symbols into a list
inputlist = df.index.get_values()
for row in inputlist:
    lastsale = df.loc[row,"LastSale"]
    print(row + " last price is " + str(lastsale))

# Display first 10 rows
#print(nasdaq.head)

# Inspect nasdaq
#print(nasdaq.info())