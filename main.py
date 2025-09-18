import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
dates = pd.date_range(start='2022-01-01', periods=365)
daily_users = 1000 + 200 * np.sin(2 * np.pi * np.arange(365) / 365) + 50 * np.random.randn(365) #Seasonal trend + noise
daily_sessions = 2 * daily_users + 100 * np.random.randn(365) # Correlated with users
daily_pageviews = 5 * daily_sessions + 200 * np.random.randn(365) # Correlated with sessions
data = {'Date': dates, 'DailyUsers': daily_users, 'DailySessions': daily_sessions, 'DailyPageviews': daily_pageviews}
df = pd.DataFrame(data)
df = df.set_index('Date')
# --- 2. Time Series Decomposition ---
# Decompose Daily Users
decomposition = seasonal_decompose(df['DailyUsers'], model='additive', period=30) # Assuming roughly monthly seasonality
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid
# --- 3. Visualization ---
plt.figure(figsize=(12, 8))
plt.subplot(411)
plt.plot(df['DailyUsers'], label='Original')
plt.legend(loc='upper left')
plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='upper left')
plt.subplot(413)
plt.plot(seasonal, label='Seasonality')
plt.legend(loc='upper left')
plt.subplot(414)
plt.plot(residual, label='Residuals')
plt.legend(loc='upper left')
plt.tight_layout()
output_filename = 'time_series_decomposition.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
# --- 4. Forecasting (Illustrative -  More sophisticated models could be used)---
# Simple forecasting using the trend component (for demonstration)
future_dates = pd.date_range(start='2023-01-01', periods=30)
future_trend = trend[-30:].mean() + np.arange(30) * (trend[-1] - trend[-30]) / 30 #linear extrapolation
#This is a very basic forecast,  more advanced methods should be applied for real-world scenarios.
# --- 5. Churn Prediction (Illustrative) ---
# A simple example: flag potential churn if the forecasted trend drops below a threshold
churn_threshold = 900
potential_churn = future_trend < churn_threshold
print("\nPotential Churn Prediction (Illustrative):")
print(f"Future Trend: {future_trend}")
print(f"Potential Churn: {potential_churn}")
#Note: This churn prediction is highly simplified.  A robust solution would involve more complex modeling and feature engineering.