"""
    Script to compute and plot various descriptive statistics for the wind energy 
    time series data located in the 'data' folder in this repository.

    Plots saved in the 'plot' folder.
"""
# Tamil Nadu -> Yearly Plots
# Other States -> Plots for August-September-October

import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns
from pandas.plotting import autocorrelation_plot

# df = pd.read_csv("../data/Tamil Nadu/2014_hourly.csv", header=0, index_col=0)
# df = df.groupby(['Hour']).mean()
# plt.style.use("seaborn")

# df = df.loc[(df['Year'] == 2014) & (df['Month'] >=8) & (df["Month"] <= 10)]

#df.plot()
# df.iloc[:50, :].plot.bar(x='Hour', y='Wind Speed')

# plt.plot(df["Hour"], df["Wind Speed"], linestyle='solid')
# print(df.head)
# df.boxplot(column="Wind Speed",by='Hour')
# plt.plot(df["Hour"], df["Wind Speed"])
# plt.xlabel("Hour")
# plt.ylabel("Windspeed value")

# plt.title("Tamil Nadu (2014) for August, September, October")
# plt.show()
#plt.show()

def show_violinplot(path_to_csv):
    series = pd.read_csv(path_to_csv, header=0, index_col=0, parse_dates={'Date': ['Month', 'Day','Year']}, squeeze=True)
    series = series['Wind Speed']
    groups = series.groupby(pd.Grouper(freq='A'))
    years = pd.DataFrame()
    for name, group in groups:
	    years[name.year] = group.values
    fig, ax = plt.subplots(figsize =(9, 7)) 
    figure = sns.violinplot(data=years, ax=ax)
    figure.plot()
    plt.title('Violin plot grouped by Year')
    plt.xlabel('Year')
    plt.ylabel('Wind Speed')
    plt.savefig('../plots/yearly/violinplot.png')
    plt.show()

def get_autocorrelation(path_to_csv):
    series = pd.read_csv(path_to_csv, header=0, index_col=0, parse_dates={'Date': ['Month', 'Day','Year']}, squeeze=True)
    series = series['Wind Speed']
    autocorrelation_plot(series)
    plt.show()

def get_heatmap(path_to_csv):
    series = pd.read_csv(path_to_csv, header=0, index_col=0, parse_dates={'Date': ['Month', 'Day','Year']}, squeeze=True)
    series = series['Wind Speed']
    groups = series.groupby(pd.Grouper(freq='A'))
    years = pd.DataFrame()
    for name, group in groups:
	    years[name.year] = group.values
    years = years.T
    plt.matshow(years, interpolation=None, aspect='auto')
    plt.show()

show_violinplot("../data/Tamil Nadu/TN.csv")
#get_autocorrelation("../data/Tamil Nadu/2014.csv")
#get_heatmap("../data/Tamil Nadu/2014.csv")