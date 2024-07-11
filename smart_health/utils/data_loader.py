import pandas as pd

def load_health_data():
    return pd.read_csv('health_data.csv')

def load_patient_data():
    return pd.read_json('patient_data.json')
