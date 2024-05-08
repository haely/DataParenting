#from fbprophet import Prophet

class DailySpendingAnomalyDetector:
  """
  This class detects anomalies in daily spending data using IQR and Prophet.
  """

  def __init__(self, data):
    """
    Initializes the class with daily spending data.

    Args:
        data (pandas.DataFrame): A DataFrame with a 'date' column (datetime) and a 'spending' column (numeric).
    """
    self.data = data.copy()  # Avoid modifying original data

  def _get_iqr(self):
    """
    Calculates the Interquartile Range (IQR) of the spending data.

    Returns:
        float: The IQR value.
    """
    q1 = self.data['spending'].quantile(0.25)
    q3 = self.data['spending'].quantile(0.75)
    return q3 - q1

  def detect_anomalies_iqr(self, num_std=1.5):
    """
    Identifies anomalies in the daily spending data based on IQR thresholds.

    Args:
        num_std (float, optional): The number of standard deviations used for thresholds. Defaults to 1.5.

    Returns:
        pandas.DataFrame: A copy of the original data with a new column 'is_anomaly' (boolean) indicating anomalies.
    """
    iqr = self._get_iqr()
    lower_bound = q1 - (num_std * iqr)
    upper_bound = q3 + (num_std * iqr)
    self.data['is_anomaly_iqr'] = ~self.data['spending'].between(lower_bound, upper_bound)
    return self.data.copy()
  """
  def detect_anomalies_prophet(self):
    """
    Identifies potential anomalies using Facebook Prophet for forecasting.

    Returns:
        pandas.DataFrame: A copy of the original data with 'prophet_forecast' and 'prophet_is_anomaly' columns.
    """
    data_copy = self.data.copy()
    data_copy.rename(columns={'date': 'ds', 'spending': 'y'}, inplace=True)  # Prophet format
    model = Prophet()
    model.fit(data_copy)
    future = model.make_future_dataframe(periods=len(data_copy))
    forecast = model.predict(future)
    data_copy['prophet_forecast'] = forecast['yhat']
    data_copy['prophet_is_anomaly'] = abs(data_copy['spending'] - data_copy['prophet_forecast']) > (1.5 * forecast['yhat'].std())
    return data_copy
   """
# Example usage
data = pd.DataFrame({
  'date': pd.to_datetime(['2024-04-01', '2024-04-02', '2024-04-03', '2024-04-04', '2024-04-05', '2024-04-06', '2024-04-07']),
  'spending': [100, 120, 80, 95, 150, 110, 70]
})

anomaly_detector = DailySpendingAnomalyDetector(data)
data_with_iqr_anomalies = anomaly_detector.detect_anomalies_iqr()
#data_with_prophet_anomalies = anomaly_detector.detect_anomalies_prophet()

print(data_with_iqr_anomalies)
#print(data_with_prophet_anomalies)

