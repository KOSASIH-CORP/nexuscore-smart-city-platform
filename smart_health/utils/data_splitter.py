import pandas as pd
from sklearn.model_selection import train_test_split

def split_health_data(data):
    X = data.drop(['id', 'patient_id', 'timestamp'], axis=1)
    y = data['heart_rate']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def split_patient_data(data):
    X = data.drop(['id', 'name', 'age', 'gender', 'medical_history'], axis=1)
    y = data['medical_history']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
