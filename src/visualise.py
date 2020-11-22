"""
    Script to compute and plot various descriptive statistics for the wind energy 
    time series data located in the 'data' folder in this repository.
"""
import pandas as pd 
from matplotlib import pyplot as plt

df = pd.read_csv("../data/Tamil Nadu/TN.csv")
plt.style.use("seaborn")

print(df.head)
df = df.loc[(df['Year'] == 2000)]
# print(df.head)
df.boxplot(column="Wind Speed",by='Hour')

# plt.plot(days, speeds,linestyle='solid')
# plt.xlabel("Day of the month")
# plt.ylabel("Avg Windspeed value")

plt.show()