import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy import stats
import numpy as np


df = pd.read_csv("data/data.csv")
df.shape

df.head()
df.dtypes

string_col = df.select_dtypes(include="object").columns
df[string_col]=df[string_col].astype("string")
df.dtypes

df.city.value_counts()

df_seattle = df[df.city == "Seattle"]
df_seattle.shape

df_seattle = df_seattle.drop(columns=["city", "country","statezip", "yr_renovated"])
df_seattle.head()

plt.figure(figsize=(12,8))
sb.scatterplot(x = df_seattle.sqft_living, y = df_seattle.price)
plt.show()

z_price = np.abs(stats.zscore(df_seattle["price"]))
z_sqftliving = np.abs(stats.zscore(df_seattle["sqft_living"]))

a_out_price = np.where(z_price > 3)
a_out_sqftliving = np.where(z_sqftliving > 3)

print(a_out_price)
print(a_out_sqftliving)
print(a_out_price[0])

for element in a_out_price[0]:
    df_seattle_clean = df_seattle.drop(df.index[element+1])