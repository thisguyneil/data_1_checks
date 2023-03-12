import pandas as pd
import matplotlib.pyplot as plt

df =  pd.read_excel('assets/2022 Sales Results.xlsx', sheet_name='SalesResults')
BID = df['Winning Bid']
DAT = df['Sale Date']

plt.scatter(BID, DAT)
plt.show()
#print(df.head)