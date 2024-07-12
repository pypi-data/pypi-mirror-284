# aju_pm10_hourly_prediction/pipeline.py
from .data_cleaning import process_air_quality_data
from .feature_engineering import create_features, select_top_features
from .prediction import predict_and_visualize
from .visualization import visualize_correlation_matrix, visualize_pm10_over_time

def run_full_pipeline(input_csv, xgb_model_path, rf_model_path, svm_model_path, gru_model_path, lstm_model_path):
    # Process and clean the data
    cleaned_df = process_air_quality_data(input_csv)

    # Visualize correlation matrix after imputation
    visualize_correlation_matrix(cleaned_df)

    # Create features
    feature_df = create_features(cleaned_df)

    # Visualize PM10 hourly average over time
    visualize_pm10_over_time(cleaned_df)

    # Select top 5 features
    selected_df, top_features = select_top_features(feature_df, 'AC Penrose PM10 1h average [µg/m³]')
    selected_df.to_csv('data/PM10_1hr_TopFeatures.csv')

    # Predict and visualize
    pred_df = predict_and_visualize(
        selected_df, 
        xgb_model_path, 
        rf_model_path, 
        svm_model_path, 
        gru_model_path, 
        lstm_model_path
    )
    return pred_df
