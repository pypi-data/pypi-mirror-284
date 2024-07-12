# aju_pm10_hourly_prediction/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def visualize_predictions(last_day_pm10, pred_df):
    plt.figure(figsize=(14, 7))
    plt.plot(last_day_pm10.index, last_day_pm10, label="Actual PM10 Last Day", color='black')
    plt.plot(pred_df.index, pred_df['xgb'], label="XGBoost Predictions", linestyle='--')
    plt.plot(pred_df.index, pred_df['rf'], label="Random Forest Predictions", linestyle='--')
    plt.xlabel("Datetime")
    plt.ylabel("PM10 Values [µg/m³]")
    plt.title("Predictions vs Previous Day PM10 Values")
    plt.legend()
    plt.show()

def visualize_correlation_matrix(df):
    plt.figure(figsize=(12, 10))
    correlation_matrix = df.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

    sns.heatmap(correlation_matrix, mask=mask, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix After Imputation')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.yticks(rotation=0)  # Rotate y-axis labels for better readability
    plt.show()

def visualize_pm10_over_time(df, pm10_column='AC Penrose PM10 1h average [µg/m³]'):
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df[pm10_column], label='PM10 Hourly Average', color='blue')
    plt.xlabel("Datetime")
    plt.ylabel("PM10 Values [µg/m³]")
    plt.title("PM10 Hourly Average Over Time")
    plt.legend()
    plt.show()
