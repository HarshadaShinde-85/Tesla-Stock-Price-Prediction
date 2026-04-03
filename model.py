# Tesla Stock Price Prediction Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


# ---------------------------
# 1. DATA COLLECTION
# ---------------------------

# Load dataset
data = pd.read_excel("../data/Tesla.xls")

print("Dataset Shape:", data.shape)
print(data.head())


# ---------------------------
# 2. DATA CLEANING
# ---------------------------

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Sort values
data = data.sort_values(by='Date')

# Check missing values
print("Missing Values:\n", data.isnull().sum())

# Drop missing values if present
data = data.dropna()


# ---------------------------
# 3. FEATURE SELECTION
# ---------------------------

# Selecting important features
features = ['Open', 'High', 'Low', 'Volume']
target = 'Close'

X = data[features]
y = data[target]


# ---------------------------
# 4. DATA PREPROCESSING
# ---------------------------

# Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ---------------------------
# 5. MODEL BUILDING
# ---------------------------

# Linear Regression Model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)


# Random Forest Model
rf_model = RandomForestRegressor(n_estimators=100)
rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)


# ---------------------------
# 6. MODEL EVALUATION
# ---------------------------

def evaluate_model(name, y_test, predictions):
    print(f"\n{name} Performance:")
    print("R2 Score:", r2_score(y_test, predictions))
    print("RMSE:", np.sqrt(mean_squared_error(y_test, predictions)))


evaluate_model("Linear Regression", y_test, lr_predictions)
evaluate_model("Random Forest", y_test, rf_predictions)


# ---------------------------
# 7. VISUALIZATION
# ---------------------------

plt.figure(figsize=(10,5))
plt.plot(y_test.values, label="Actual Price")
plt.plot(rf_predictions, label="Predicted Price")
plt.legend()
plt.title("Actual vs Predicted Tesla Stock Price")
plt.savefig("../outputs/prediction_plot.png")
plt.show()


# ---------------------------
# 8. SAMPLE PREDICTION
# ---------------------------

sample = np.array([[700, 720, 690, 30000000]])
prediction = rf_model.predict(sample)

print("\nPredicted Closing Price:", prediction[0])