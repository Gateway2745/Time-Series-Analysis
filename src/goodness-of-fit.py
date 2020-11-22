from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/Tamil Nadu/TN.csv")
speed = df['Wind Speed'].to_numpy()
list_of_dists = ["norm", "weibull_min", "weibull_max"]

results = []
for i in list_of_dists:
    dist = getattr(stats, i)
    param = dist.fit(speed)
    a = stats.kstest(speed, i, args=param)
    print(a)