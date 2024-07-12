# aju_pm10_hourly_prediction/data_cleaning.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import KNNImputer
import warnings

warnings.filterwarnings('ignore')

def process_air_quality_data(input_csv):
    data = pd.read_csv(input_csv, encoding='latin1')
    data["Datetime"] = pd.to_datetime(data["Date"] + " " + data["Time"], format='%d/%m/%Y %H:%M', errors='coerce')
    data = data.drop(columns=["Date", "Time"])
    data = data.drop_duplicates(subset=["Datetime"])
    full_datetime_range = pd.date_range(start=data["Datetime"].min(), end=data["Datetime"].max(), freq='H')
    data = data.set_index("Datetime").reindex(full_datetime_range)
    data.index.name = 'Datetime'
    data.interpolate(method='time', inplace=True)
    data[data < 0] = np.nan
    
    visualize_before_cleaning(data)
    
    data = remove_outliers_iqr(data)
    df_cleaned = data.sort_index().reset_index()
    datetime_series = df_cleaned['Datetime']
    df_cleaned = df_cleaned.drop(columns=['Datetime'])
    
    visualize_before_imputation(df_cleaned)
    
    imputer = KNNImputer(n_neighbors=2)
    df_imputed_values = imputer.fit_transform(df_cleaned)
    df_imputed = pd.DataFrame(df_imputed_values, columns=df_cleaned.columns)
    df_imputed['Datetime'] = datetime_series
    df_imputed = df_imputed.set_index('Datetime')
    
    return df_imputed

def remove_outliers_iqr(data, k=1.5):
    numeric_df = data.select_dtypes(include=np.number)
    Q1 = numeric_df.quantile(0.25)
    Q3 = numeric_df.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - k * IQR
    upper_bound = Q3 + k * IQR
    data_cleaned = data.copy()
    for col in numeric_df.columns:
        outlier_mask = (data_cleaned[col] < lower_bound[col]) | (data_cleaned[col] > upper_bound[col])
        data_cleaned.loc[outlier_mask, col] = np.nan
    return data_cleaned

def visualize_before_cleaning(data):
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=data)
    plt.title('Original Data Box Plot')
    plt.xticks(rotation=45, ha="right")
    plt.show()

def visualize_before_imputation(df_cleaned):
    plt.figure(figsize=(12, 6))
    sns.heatmap(df_cleaned.isnull(), cbar=False, cmap='viridis')
    plt.xticks(ticks=np.arange(len(df_cleaned.columns)) + 0.5, labels=df_cleaned.columns, rotation=45, ha='right')
    plt.title('Heatmap of Missing Data Before Imputation')
    plt.show()
