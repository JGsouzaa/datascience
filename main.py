import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = pd.read_csv("ds_salaries.csv")
newdf = df[["salary_in_usd","work_year", "company_location","company_size","experience_level"]]

corr = df.corr()

corr_plot = sb.heatmap(corr, annot=True, fmt=".1f", linewidths=.6)

#data analysis
filters = ["company_location", "company_size", "experience_level"]
dic_filters = {}
for i in range(len(filters)):
    list_type = [] 
    k = newdf.drop_duplicates(subset=filters[i])
    for element in k[filters[i]]:
        list_type.append(element)
    dic_filters[filters[i]] = list_type



newdf.loc[newdf["experience_level"]=="MI"]




df.plot(x="salary", y="company_location", kind="scatter")

#x = workyear
#y = salary in usd
# filtrar y por company_location, company_size e experience_level