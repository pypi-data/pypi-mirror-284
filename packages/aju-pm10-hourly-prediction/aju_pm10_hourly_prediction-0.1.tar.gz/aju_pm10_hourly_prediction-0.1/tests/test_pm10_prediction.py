import unittest
import os
import pandas as pd
from aju_pm10_hourly_prediction import run_full_pipeline

class TestPM10Prediction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Paths for test data and models
        cls.input_csv = 'data/raw_data.csv'
        cls.xgb_model_path = 'models/best_xgb_model2.pkl'
        cls.rf_model_path = 'models/best_rf_model.pkl'
        cls.svm_model_path = 'models/best_svm_model.pkl'
        cls.gru_model_path = 'models/gru_model.h5'
        cls.lstm_model_path = 'models/lstm_model.keras'
        
        # Generate a small test dataset if it doesn't exist
        if not os.path.exists(cls.input_csv):
            data = {
                'Date': ['01/01/2020'] * 48,
                'Time': ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'] * 2,
                'AC Penrose PM10 1h average [µg/m³]': [10.0 + i for i in range(48)],
                'Feature1': [1.0] * 48,
                'Feature2': [2.0] * 48
            }
            df = pd.DataFrame(data)
            df.to_csv(cls.input_csv, index=False)

    def test_run_full_pipeline(self):
        pred_df = run_full_pipeline(
            input_csv=self.input_csv,
            xgb_model_path=self.xgb_model_path,
            rf_model_path=self.rf_model_path,
            svm_model_path=self.svm_model_path,
            gru_model_path=self.gru_model_path,
            lstm_model_path=self.lstm_model_path
        )
        
        # Check if the output is a DataFrame
        self.assertIsInstance(pred_df, pd.DataFrame)
        
        # Check if the DataFrame is not empty
        self.assertFalse(pred_df.empty)

        # Check if the DataFrame has the expected columns
        expected_columns = ['xgb', 'rf', 'svm', 'gru', 'lstm']
        self.assertTrue(all(column in pred_df.columns for column in expected_columns))

if __name__ == '__main__':
    unittest.main()
