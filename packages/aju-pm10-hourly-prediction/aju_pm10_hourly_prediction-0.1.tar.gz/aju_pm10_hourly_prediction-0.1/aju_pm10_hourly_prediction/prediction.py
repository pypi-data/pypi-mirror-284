# aju_pm10_hourly_prediction/prediction.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from keras.models import load_model
import pickle
from datetime import timedelta
import warnings
from .visualization import visualize_predictions

warnings.filterwarnings('ignore')

def predict_and_visualize(df, xgb_model_path, rf_model_path, svm_model_path, gru_model_path, lstm_model_path):
    last_day_pm10 = df["AC Penrose PM10 1h average [µg/m³]"].tail(24)
    last_day_dates = last_day_pm10.index
    df.drop(["AC Penrose PM10 1h average [µg/m³]"], axis=1, inplace=True)
    feature_columns = df.columns  # Save feature columns to check shape
    
    best_xgb_model = pickle.load(open(xgb_model_path, "rb"))
    best_rf_model = pickle.load(open(rf_model_path, "rb"))
    best_svm_model = pickle.load(open(svm_model_path, "rb"))
    custom_objects = {'mse': mean_squared_error}
    gru_model = load_model(gru_model_path, custom_objects=custom_objects)
    lstm_model = load_model(lstm_model_path, custom_objects=custom_objects)
    
    # Ensure the feature shape matches for models
    def create_input_data(df, last_n_hours=24):
        last_data = df[-last_n_hours:]
        X = last_data.values
        return X

    def predict_next_day(models, df):
        predictions = {}
        last_n_hours = 24
        X = create_input_data(df, last_n_hours)
        
        # Check shape and use only relevant features
        if X.shape[1] != len(feature_columns):
            raise ValueError(f"Feature shape mismatch, expected: {len(feature_columns)}, got {X.shape[1]}")
        
        predictions['xgb'] = models[0].predict(X)
        predictions['rf'] = models[1].predict(X)
        predictions['svm'] = models[2].predict(X)
        X_reshaped = X.reshape((1, X.shape[0], X.shape[1]))
        predictions['gru'] = models[3].predict(X_reshaped).flatten()
        predictions['lstm'] = models[4].predict(X_reshaped).flatten()
        return predictions

    predictions = predict_next_day([best_xgb_model, best_rf_model, best_svm_model, gru_model, lstm_model], df)
    
    # Ensure the index is datetime
    df.index = pd.to_datetime(df.index)
    
    next_day_dates = pd.date_range(start=df.index[-1] + timedelta(hours=1), periods=24, freq='H')
    pred_df = pd.DataFrame(predictions, index=next_day_dates)
    visualize_predictions(last_day_pm10, pred_df)
    return pred_df
