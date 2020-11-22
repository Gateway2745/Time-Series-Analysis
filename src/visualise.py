"""
    Script to compute and plot various descriptive statistics for the wind energy 
    time series data located in the 'data' folder in this repository.
"""
import pandas as pd 
from matplotlib import pyplot as plt

pd.read_csv("data/TN.csv")
plt.style.use("seaborn")



plt.tight_layout()
plt.show()