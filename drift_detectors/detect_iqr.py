#from fbprophet import Prophet
import pandas as pd
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
    return q1, q3

  def detect_anomalies_iqr(self, num_std=1.5):
    """
    Identifies anomalies in the daily spending data based on IQR thresholds.

    Args:
        num_std (float, optional): The number of standard deviations used for thresholds. Defaults to 1.5.

    Returns:
        pandas.DataFrame: A copy of the original data with a new column 'is_anomaly' (boolean) indicating anomalies.
    """
    q1, q3 = self._get_iqr()  # Unpack the returned tuple to access q1 and q3
    iqr = q3 - q1  # Calculate IQR using the unpacked values
    lower_bound = q1 - (num_std * iqr)
    upper_bound = q3 + (num_std * iqr)
      
    #iqr = self._get_iqr()
    #lower_bound = q1 - (num_std * iqr)
    #upper_bound = q3 + (num_std * iqr)
    self.data['is_anomaly_iqr'] = ~self.data['spending'].between(lower_bound, upper_bound)
    return self.data.copy()

