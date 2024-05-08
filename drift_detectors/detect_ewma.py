import pandas as pd

def detect_anomalies_ewma(data, alpha=0.2, threshold_multiplier=2):
    """
    Detect anomalies in time series data using exponential weighted moving average (EWMA).

    Args:
    - data (DataFrame): DataFrame containing the time series data with a 'date' column and a numeric column to analyze.
    - alpha (float): Smoothing factor for EWMA. Default is 0.2.
    - threshold_multiplier (float): Multiplier for the anomaly threshold (e.g., 2 times the IQR). Default is 2.

    Returns:
    - DataFrame: Input DataFrame with an additional 'is_anomaly_iqr' column indicating whether each data point is an anomaly.
    """
    # Calculate EWMA
    data['ewma'] = data['spending'].ewm(alpha=alpha, adjust=False).mean()

    # Calculate the difference between actual spending and EWMA
    data['diff'] = data['spending'] - data['ewma']

    # Define anomaly threshold based on IQR
    Q1 = data['diff'].quantile(0.25)
    Q3 = data['diff'].quantile(0.75)
    IQR = Q3 - Q1
    threshold_iqr = threshold_multiplier * IQR

    # Flag anomalies based on IQR
    data['is_anomaly_ewma'] = (data['diff'] < (Q1 - threshold_iqr)) | (data['diff'] > (Q3 + threshold_iqr))

    return data

# Example usage
data = pd.DataFrame({
    'date': pd.to_datetime(['2024-04-01', '2024-04-02', '2024-04-03', '2024-04-04', '2024-04-05', '2024-04-06', '2024-04-07']),
    'spending': [100, 120, 80, 95, 150, 110, 70]
})

data_with_anomalies = detect_anomalies_ewma(data)
print(data_with_anomalies[['date', 'spending', 'is_anomaly_ewma']])

