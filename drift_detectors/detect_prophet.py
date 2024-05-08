from fbprophet import Prophet
import pandas as pd
import numpy as np

def detect_anomalies_prophet(data, threshold_multiplier=2):
    """
    Detect anomalies in time series data using Prophet.

    Args:
    - data (DataFrame): DataFrame containing the time series data with a 'date' column and a numeric column to analyze.
    - threshold_multiplier (float): Multiplier for the anomaly threshold (e.g., 2 times the standard deviation). Default is 2.

    Returns:
    - DataFrame: Input DataFrame with an additional 'is_anomaly_prophet' column indicating whether each data point is an anomaly.
    """
    # Prepare data for Prophet
    prophet_data = data.rename(columns={'date': 'ds', 'spending': 'y'})

    # Fit Prophet model
    model = Prophet()
    model.fit(prophet_data)

    # Make predictions
    future = model.make_future_dataframe(periods=0)
    forecast = model.predict(future)

    # Calculate residuals
    residuals = np.abs(prophet_data['y'] - forecast['yhat'])

    # Calculate threshold for anomalies
    threshold = threshold_multiplier * residuals.std()

    # Flag anomalies based on threshold
    data['is_anomaly_prophet'] = False
    data.loc[residuals > threshold, 'is_anomaly_prophet'] = True

    return data

# Example usage
data = pd.DataFrame({
    'date': pd.to_datetime(['2024-04-01', '2024-04-02', '2024-04-03', '2024-04-04', '2024-04-05', '2024-04-06', '2024-04-07']),
    'spending': [100, 120, 80, 95, 150, 110, 70]
})

data_with_anomalies_prophet = detect_anomalies_prophet(data)
print(data_with_anomalies_prophet[['date', 'spending', 'is_anomaly_prophet']])

