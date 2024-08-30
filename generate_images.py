import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Load dataset
df = sns.load_dataset('flights')
df['yearMonth'] = pd.to_datetime("01-"+df['month'].astype(str)+"-"+df['year'].astype(str))
df.set_index('yearMonth', inplace=True)

# Generate the rolling mean and std graph
df['rollMean'] = df.passengers.rolling(window=12).mean()
df['rollStd'] = df.passengers.rolling(window=12).std()

# Save rolling mean and std graph
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x=df.index, y=df.passengers, label='Passengers')
sns.lineplot(data=df, x=df.index, y=df.rollMean, label='Rolling Mean')
sns.lineplot(data=df, x=df.index, y=df.rollStd, label='Rolling Std')
plt.legend()
plt.title('Rolling Mean and Standard Deviation')
plt.savefig('static/rolling_mean_std.png')
plt.close()

# Placeholder for the future prediction graph (as it's typically complex and requires model fitting)
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x=df.index, y=df.passengers, label='SARIMAX Predicted')
sns.lineplot(data=df, x=df.index, y=df.passengers.shift(12), label='ARIMA Predicted')
plt.plot(df.index, df.passengers, 'k--', label='Future Predictions')
plt.legend()
plt.title('Future Prediction')
plt.savefig('static/future_prediction.png')
plt.close()

# Generate and save SARIMAX PACF and ACF graphs
plt.figure(figsize=(5, 5))
plot_pacf(df['passengers'].diff().dropna(), lags=20)
plt.title('SARIMAX Partial Autocorrelation')
plt.savefig('static/sarimax_pacf.png')
plt.close()

plt.figure(figsize=(5, 5))
plot_acf(df['passengers'].diff().dropna(), lags=20)
plt.title('SARIMAX Autocorrelation')
plt.savefig('static/sarimax_acf.png')
plt.close()

# Generate and save ARIMA PACF and ACF graphs (using same data for simplicity)
plt.figure(figsize=(5, 5))
plot_pacf(df['passengers'].diff().dropna(), lags=20)
plt.title('ARIMA Partial Autocorrelation')
plt.savefig('static/arima_pacf.png')
plt.close()

plt.figure(figsize=(5, 5))
plot_acf(df['passengers'].diff().dropna(), lags=20)
plt.title('ARIMA Autocorrelation')
plt.savefig('static/arima_acf.png')
plt.close()
