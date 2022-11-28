import pandas as pd

df_station1 = pd.read_csv("data/data.csv", error_bad_lines=False)
df_station1.head


print("end")