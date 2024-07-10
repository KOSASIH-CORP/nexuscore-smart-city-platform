import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.inspection import permutation_importance

def model_explainability(model, X, y):
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model.fit(X_train, y_train)
    
    # Get feature importance using permutation importance
    feature_importance = permutation_importance(model, X_test, y_test, n_repeats=10, random_state=42)
    
    # Create dataframe to store feature importance
    feature_importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importance.importances_mean})
    
    return feature_importance_df
