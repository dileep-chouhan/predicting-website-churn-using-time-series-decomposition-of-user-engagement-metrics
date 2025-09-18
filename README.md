# Predicting Website Churn Using Time Series Decomposition of User Engagement Metrics

## Overview

This project aims to predict potential website user churn by analyzing time series data of key user engagement metrics.  We employ time series decomposition techniques to identify trends, seasonality, and residuals in the data, allowing for more accurate forecasting of traffic decline and proactive mitigation strategies.  The analysis focuses on identifying patterns indicative of churn and providing insights into the factors contributing to user attrition.


## Technologies Used

This project utilizes the following Python libraries:

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Statsmodels (for time series decomposition)


## How to Run

1. **Install Dependencies:**  Navigate to the project directory in your terminal and install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Script:** Execute the main script using:

   ```bash
   python main.py
   ```


## Example Output

The script will print key analysis results to the console, including summary statistics of the time series data and the identified trend, seasonal, and residual components.  Additionally, the script generates several plot files visualizing the decomposed time series and forecasts, including:

* `engagement_decomposition.png`:  A plot showing the original time series data along with its decomposed components (trend, seasonality, residual).
* `churn_forecast.png`: A plot visualizing the forecasted user engagement levels, highlighting potential churn periods.

These plot files will be saved in the project directory.  The specific output may vary depending on the input data used.