import pickle
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, IsolationForest
import numpy as np

def load_model(model_path="models/model.pkl"):
    with open(model_path, 'rb') as f:
        return pickle.load(f)

def predict_revenue(model, country, target_date):
    # Dummy features for demo - replace with your real features
    # Model expects [month, country_encoded, prev_month_revenue]
    country_map = {"United Kingdom":0, "EIRE":1, "Germany":2, "France":3, "all":99}
    month = pd.to_datetime(target_date).month
    features = np.array([[month, country_map.get(country,0), 10000]])
    pred = model.predict(features)[0]
    if country.lower() == 'all':
        pred = pred * 5 # sum of all countries logic
    return float(pred)

def monitor_performance(new_data):
    """Novelty detection for monitoring - Q5"""
    iso = IsolationForest(contamination=0.05)
    preds = iso.fit_predict(new_data.reshape(-1,1))
    return preds
