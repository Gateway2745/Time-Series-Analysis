from math import sqrt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as mse
from statsmodels.tsa.arima_model import ARIMA as arima
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

#ARIMA
##############################
# load dataframe
df = pd.read_csv('TN.csv')

train_data = df.loc[(df['Year'] == 2013) & (df['Month']==12)]['Wind Speed'].to_numpy().tolist()
val_data = df.loc[(df['Year'] == 2014) & (df['Month']==1)]['Wind Speed'].to_numpy().tolist()
train_size = len(train_data)
val_size = len(val_data)
print(train_size,val_size)
history = train_data
preds = list()

for i in range(len(val_data)):
    model = arima(history, order=(3,1,0))
    model_fit = model.fit(disp=False)
    yhat = model_fit.forecast()[0]
    preds.append(yhat)
    history.append(val_data[i])
    print('predicted=%f, expected=%f' % (yhat, val_data[i]))


from sklearn.metrics import mean_squared_error
error = mean_squared_error(val_data, preds)
print('Test MSE: %.3f' % error)
# plot
plt.plot(val_data)
plt.plot(preds, color='red')
fig1 = plt.gcf()
fig1.savefig("two_days_arima.png",dpi=500)
plt.show()


#######################################
#SARIMA 


