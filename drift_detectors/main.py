# Example usage
data = pd.DataFrame({
    'date': pd.to_datetime(['2024-04-01', '2024-04-02', '2024-04-03', '2024-04-04', '2024-04-05', '2024-04-06', '2024-04-07']),
    'spending': [100, 120, 80, 95, 150, 110, 70]
})

data_with_anomalies_lstm = detect_anomalies_lstm(data)
print(data_with_anomalies_lstm[['date', 'spending', 'is_anomaly_lstm']])

