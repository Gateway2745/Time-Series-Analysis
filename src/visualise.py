"""
    Script to compute and plot various descriptive statistics for the wind energy 
    time series data located in the 'data' folder in this repository.

    Plots saved in the 'plot' folder.
"""
# Tamil Nadu -> Yearly Plots
# Other States -> Plots for August-September-October

import pandas as pd 
from matplotlib import pyplot as plt

df = pd.read_csv("../data/Tamil Nadu/TN.csv")
plt.style.use("seaborn")

# df = df.loc[(df['Year'] == 2014) & (df['Month'] >=8) & (df["Month"] <= 10)]
df = df.loc[df['Year'] == 2014]
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# hours = [i for i in range(24)]
# speeds = [df['Wind Speed'][i] for i in range(len(df))]
# ax.bar(hours,speeds)

# plt.plot(df["Hour"], df["Wind Speed"], linestyle='solid')
print(df.head)
df.hist(df['Hour'], df['Wind Speed'])
# df.boxplot(column="Wind Speed",by='Hour')
# plt.plot(df["Hour"], df["Wind Speed"])
plt.xlabel("Hour")
plt.ylabel("Windspeed value")

# plt.title("(Madhya Pradesh)")
plt.show()