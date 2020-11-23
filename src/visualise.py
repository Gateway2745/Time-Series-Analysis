"""
    Script to compute and plot various descriptive statistics for the wind energy 
    time series data located in the 'data' folder in this repository.

    Plots saved in the 'plot' folder.
"""
# Tamil Nadu -> Yearly Plots
# Other States -> Plots for August-September-October

import pandas as pd 
from matplotlib import pyplot as plt

df = pd.read_csv("../data/Tamil Nadu/2014_hourly.csv", header=0, index_col=0)
df = df.groupby(['Hour']).mean()
plt.style.use("seaborn")

# df = df.loc[(df['Year'] == 2014) & (df['Month'] >=8) & (df["Month"] <= 10)]

df.plot()
# df.iloc[:50, :].plot.bar(x='Hour', y='Wind Speed')

# plt.plot(df["Hour"], df["Wind Speed"], linestyle='solid')
# print(df.head)
# df.boxplot(column="Wind Speed",by='Hour')
# plt.plot(df["Hour"], df["Wind Speed"])
# plt.xlabel("Hour")
# plt.ylabel("Windspeed value")

plt.title("Tamil Nadu (2014) for August, September, October")
plt.show()