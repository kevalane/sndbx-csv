import pandas as pd

data = pd.read_csv('Book1.csv')

for i, j in data.iterrows():
    print(str(i) + ": " + j.productName + ", $" + str(j.transactionAmountUSD))
    print()

