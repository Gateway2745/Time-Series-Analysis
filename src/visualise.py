"""
    Script to compute and plot various descriptive statistics for the wind energy 
    time series data located in the 'data' folder in this repository.
"""
import pandas as pd 
from matplotlib import pyplot as plt

df = pd.read_csv("../data/Tamil Nadu/TN.csv", header=0, index_col=0, squeeze=True)
plt.style.use("seaborn")

df.boxplot(column="Wind Speed",by='Hour')

# plt.plot(days, speeds,linestyle='solid')
# plt.xlabel("Day of the month")
# plt.ylabel("Avg Windspeed value")

plt.show()