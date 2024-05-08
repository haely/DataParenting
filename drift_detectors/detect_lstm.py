import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def detect_anomalies_lstm(data, window_size=3, threshold_multiplier=2):
    """
    Detect anomalies in time series data using LSTM.

    Args:
    - data (DataFrame): DataFrame containing the time series data with a 'date' column and a numeric column to analyze.
    - window_size (int): Number of previous time steps to use as input features for LSTM. Default is 3.
    - threshold_multiplier (float): Multiplier for the anomaly threshold (e.g., 2 times the standard deviation). Default is 2.

    Returns:
    - DataFrame: Input DataFrame with an additional 'is_anomaly_lstm' column indicating whether each data point is an anomaly.
    """
    # Normalize the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data['spending'].values.reshape(-1, 1))

    # Create sequences of data for LSTM
    X, y = [], []
    for i in range(window_size, len(scaled_data)):
        X.append(scaled_data[i - window_size:i, 0])
        y.append(scaled_data[i, 0])
    X, y = np.array(X), np.array(y)

    # Reshape data for LSTM
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    # Build LSTM model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], 1)))
    model.add(LSTM(units=50))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X, y, epochs=100, batch_size=32)

    # Predictions using the trained LSTM model
    predictions = model.predict(X)
    residuals = np.abs(scaled_data[window_size:] - predictions)

    # Calculate threshold for anomalies
    threshold = threshold_multiplier * residuals.std()

    # Flag anomalies based on threshold
    data['is_anomaly_lstm'] = False
    data.iloc[window_size:, data.columns.get_loc('is_anomaly_lstm')] = residuals > threshold

    return data

# Example usage
data = pd.DataFrame({
    'date': pd.to_datetime(['2024-04-01', '2024-04-02', '2024-04-03', '2024-04-04', '2024-04-05', '2024-04-06', '2024-04-07']),
    'spending': [100, 120, 80, 95, 150, 110, 70]
})

data_with_anomalies_lstm = detect_anomalies_lstm(data)
print(data_with_anomalies_lstm[['date', 'spending', 'is_anomaly_lstm']])

