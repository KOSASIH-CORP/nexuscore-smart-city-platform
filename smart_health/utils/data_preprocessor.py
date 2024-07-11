import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_health_data(data):
    scaler = StandardScaler()
    data[['heart_rate', 'blood_pressure', 'body_temperature']] = scaler.fit_transform(data[['heart_rate', 'blood_pressure', 'body_temperature']])
    return data

def preprocess_patient_data(data):
    return data
