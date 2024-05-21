# Introduction to Data Drift Detection

Data drift refers to the phenomenon where the statistical properties of the target variable in a machine learning model change over time. Detecting data drift is crucial in ensuring that machine learning models remain accurate and reliable in production environments. This README provides an overview of data drift detection methods and best practices.

## Methods to Detect Data Drift

To show the differnet ways to detect drifts, I have included a python code to comapre different drift check methods. 
IQR: basic stats
EWMA: no machine learnng but some data analysis
LSTM: the most intuitive neural network method. Other include isolation trees, and nearest neighbours (I might add this later)
Prophet: FB's timeseries library (not complete)

From the sample data I have (shown in main.py), only LSTM catches these as anomalies compared to IQR, and EWMA. This shows that LSTM is more sensitive and if we care about not missing out (false positives > false negatives) LSTM is the better choice.

<img width="611" alt="Screenshot 2024-05-07 at 23 01 38" src="https://github.com/haely/DataParenting/assets/32823897/010fae20-5493-4bb2-ad5f-d29e1805abfa">



### 1. Interquartile Range (IQR) Method (Statistical)
- **Description**: Compares the difference between the 75th and 25th percentiles of the target variable.
- **Implementation**: Calculate the IQR of the target variable. Flag data points as anomalies if they fall outside a specified range based on the IQR.

### 2. Exponential Weighted Moving Average (EWMA)
- **Description**: Uses a weighted average of past observations to detect changes in the target variable.
- **Implementation**: Calculate the EWMA of the target variable. Flag data points as anomalies if they deviate significantly from the EWMA.

### 3. Long Short-Term Memory (LSTM)
- **Description**: A type of recurrent neural network (RNN) that can learn long-term dependencies in sequential data.
- **Implementation**: Train an LSTM model on the target variable. Flag data points as anomalies if the prediction error exceeds a specified threshold.

### 4. Prophet
- **Description**: A forecasting tool developed by Facebook that can capture trends and seasonality in time series data.
- **Implementation**: Use Prophet to forecast the target variable. Flag data points as anomalies if the forecasted value deviates significantly from the actual value.

## General Best Practices
- **Regular Monitoring**: Continuously monitor the target variable for drift to ensure model performance.
- **Automated Alerts**: Set up automated alerts to notify when significant drift is detected.
- **Retraining Models**: Consider retraining machine learning models when data drift is detected to maintain model accuracy.

## When to Run Data Drift Detection in Machine Learning
- **Scheduled Intervals**: Run data drift detection at regular intervals (e.g., daily, weekly) to monitor for changes in the target variable.
- **Before Model Deployment**: Run data drift detection before deploying a model to ensure that the model performs well on current data.



