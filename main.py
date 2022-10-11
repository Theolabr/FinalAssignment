import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Total=0
data = pd.read_csv('FLS.csv')
df = pd.DataFrame(data)
newdf = df.fillna(0)
newdf=newdf.astype({"zip_code":'int', "bottles_sold":'int'})
print(newdf)
# select columns in index positions
df_new = newdf.iloc[:, [6, 14, 20]]
print(df_new.head())

# Grouping and perform sum over each group
Byzip = df_new.groupby(['zip_code', 'item_number'], as_index=False)['bottles_sold'].sum()
print(Byzip)


dd = pd.DataFrame(Byzip)



plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")
x=dd['zip_code']
y= dd['bottles_sold']
#colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.plot(x, y , 'ro')
plt.show()

#Sales per store
newdf['TotalSales'] = newdf['sale_dollars'].groupby(newdf['store_number']).transform('sum')

print(newdf['TotalSales'])
Total = newdf['TotalSales'].sum()
print(Total)
n= newdf['TotalSales']
percentages = []



for i in range(72):
    percentages.append((n[i]/Total)*100)


print(percentages)

