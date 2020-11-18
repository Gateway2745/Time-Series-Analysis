import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA as arima
from math import sqrt
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as mse

filepath = '2010.csv'
df = pd.read_csv(filepath)
df = df['Wind Speed']
print(df.head())
x = df.to_numpy().tolist()

train_size = int(len(x)*0.8)
train, test = x[:train_size], x[train_size:]
print(len(train), len(test))
history = train
preds = list()

for i in range(len(test)):
    model = arima(history, order=(0, 0, 1))
    model_fit = model.fit(disp=False)
    yhat = model_fit.forecast()[0]
    preds.append(yhat)
    history.append(test[i])
    # print(f'Predicted = {yhat}; Expected = {test[i]}')

print(model_fit.summary())
rmse = sqrt(mse(test, preds))

plt.plot(test, color='blue', label='actual')
plt.plot(preds, color='red', label='prediction')
plt.legend(loc="upper left")
plt.show()
