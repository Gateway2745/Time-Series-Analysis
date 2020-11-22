import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from matplotlib import pyplot




########
# df = pd.read_csv("data/Tamil Nadu/weekly.csv")
# dates = pd.date_range(start='1/1/2018', end='31/12/2018',periods=53)
# df.drop(['week'],axis=1,inplace=True)

# df.set_index(dates,inplace=True)

# print(df.head)
# result = seasonal_decompose(df, model='additive')
# result.plot()
# pyplot.show()

################
# df = pd.read_csv("data/Tamil Nadu/TN.csv")
# dates = pd.date_range(start='1/1/2000',freq='H',periods=744)
# data = df.loc[(df['Year'] == 2000) & (df['Month']==1)]['Wind Speed']
# #print(data.head)
# print(dates)
# req = pd.DataFrame(list(data),index=dates,columns=['wind_speed'])
# print(req.shape)


# result = seasonal_decompose(req, model='additive')
# result.plot()
# pyplot.show()

###############################

df = pd.read_csv("data/Tamil Nadu/TN.csv")
dates = pd.date_range(start='1/1/2000',freq='H',periods=8760)
data = df.loc[df['Year'] == 2000]['Wind Speed']
#print(data.head)
print(dates)
req = pd.DataFrame(list(data),index=dates,columns=['wind_speed'])
print(req.shape)


result = seasonal_decompose(req, model='additive')
result.plot()
pyplot.show()

###############################