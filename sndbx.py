import pandas as pd

data = pd.read_csv('Book1.csv')

products = []
transactions = []
touched = []
for i, j in data.iterrows():
    products.append(j.productName)
    transactions.append(j.transactionAmountUSD)

for i in range(0, len(products)):
    for j in range(i+1, len(products)):
        if (products[i] == products[j]):
            transactions[i] = transactions[i] + transactions[j]
            touched.append(j)

for i in range(0, len(touched)):
    products.pop(touched[i])
    transactions.pop(touched[i])


for i in range(0, len(products)):
    print(str(products[i]) + ": " + str(transactions[i]))

input("Press any key to continue...")
