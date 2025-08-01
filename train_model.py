import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
import json
import os

# Load penguin dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
df = pd.read_csv(url)

# Drop rows with missing values
df.dropna(inplace=True)

# Map target labels to integers
species_map = {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}
df['species'] = df['species'].map(species_map)

# Select features and label
X = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
y = df['species']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
model.fit(X_train, y_train)

# Save model as JSON
model_path = "model/model.json"
os.makedirs("model", exist_ok=True)
model.save_model(model_path)

print(f"✅ Model saved to {model_path}")
