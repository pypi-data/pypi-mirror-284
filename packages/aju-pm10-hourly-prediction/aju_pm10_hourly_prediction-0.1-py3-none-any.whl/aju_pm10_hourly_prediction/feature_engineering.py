# aju_pm10_hourly_prediction/feature_engineering.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

def create_features(df):
    df['PM10_Lag1'] = df['AC Penrose PM10 1h average [µg/m³]'].shift(1)
    df['PM10_Lag2'] = df['AC Penrose PM10 1h average [µg/m³]'].shift(2)
    df['PM10_Lag3'] = df['AC Penrose PM10 1h average [µg/m³]'].shift(3)
    df['PM10_RollingMean3'] = df['AC Penrose PM10 1h average [µg/m³]'].rolling(window=3).mean()
    df['PM10_RollingStd3'] = df['AC Penrose PM10 1h average [µg/m³]'].rolling(window=3).std()
    df = df.dropna()
    return df

def select_top_features(df, target_column, top_n=5):
    # Ensure only numerical features are used for model fitting
    X = df.drop(columns=[target_column]).select_dtypes(include=[np.number])
    y = df[target_column]

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    feature_importances = pd.DataFrame({
        'Feature': X.columns,
        'Importance': model.feature_importances_
    }).sort_values(by='Importance', ascending=False)

    top_features = feature_importances.head(top_n)['Feature'].tolist()
    selected_df = df[top_features + [target_column]]
    
    return selected_df, top_features
