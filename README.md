# 🚗 Tesla Stock Price Prediction using Machine Learning

This project predicts **Tesla (TSLA) stock closing prices** using Machine Learning regression models trained on historical stock market data. It demonstrates a complete **end-to-end Machine Learning pipeline**, including data collection, cleaning, preprocessing, feature selection, model training, evaluation, comparison, and visualization.

The objective of this project is to analyze stock trends and forecast Tesla’s future closing price using structured financial indicators such as Open, High, Low, and Volume.

---

# 📌 Project Objectives

The main goals of this project are:

* Perform exploratory data analysis on Tesla stock dataset
* Clean and preprocess real-world financial data
* Select important predictive features
* Train regression models for price prediction
* Compare multiple machine learning models
* Evaluate performance using statistical metrics
* Visualize prediction accuracy

---

# 📂 Project Structure

```
Tesla-Stock-Price-Prediction
│
├── data/
│   └── Tesla.xls
│
├── src/
│   └── model.py
│
├── notebooks/
│   └── tesla_price_prediction.ipynb
│
├── outputs/
│   └── prediction_plot.png
│
├── requirements.txt
└── README.md
```

---

# 📊 Dataset Information

Dataset contains Tesla historical stock price data including:

* Date
* Open price
* High price
* Low price
* Close price
* Volume traded

Target Variable:

Close Price

Independent Variables:

Open, High, Low, Volume

Dataset format:

Excel (.xls)

# ⚙️ Technologies Used

Programming Language:

Python

Libraries:

Pandas
NumPy
Matplotlib
Scikit-learn

Development Tools:

VS Code
Jupyter Notebook
GitHub


# 🔄 Machine Learning Pipeline

The project follows a structured ML workflow:

Data Collection
→ Data Cleaning
→ Data Preprocessing
→ Feature Selection
→ Model Training
→ Model Evaluation
→ Model Comparison
→ Prediction
→ Visualization

# 📥 Step 1: Data Collection

Dataset loaded using Pandas:

import pandas as pd
data = pd.read_excel("Tesla.xls")

The dataset contains historical Tesla stock market values.

# 🧹 Step 2: Data Cleaning

Cleaning steps performed:

* Converted Date column into datetime format
* Sorted dataset chronologically
* Checked missing values
* Removed null values
* Verified dataset consistency

# ⚙️ Step 3: Data Preprocessing

Selected relevant columns affecting stock price prediction:

Open
High
Low
Volume

Target column: Close

Dataset split into:

80% Training Data
20% Testing Data

Example:

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 🎯 Step 4: Feature Selection

Selected features based on stock market influence:

Independent Variables:

Open
High
Low
Volume

Dependent Variable:

Close Price

These indicators strongly influence daily closing price behavior.

# 🤖 Step 5: Model Training

Two regression models were implemented:

### 1️⃣ Linear Regression

Used as baseline prediction model.

Example:

```python
from sklearn.linear_model import LinearRegression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
```

---

### 2️⃣ Random Forest Regressor

Used to improve prediction accuracy through ensemble learning.

Example:

```python
from sklearn.ensemble import RandomForestRegressor
rf_model = RandomForestRegressor(n_estimators=100)
rf_model.fit(X_train, y_train)
```

---

# 📈 Step 6: Model Evaluation

Models evaluated using:

```
R² Score
RMSE (Root Mean Squared Error)
```

Example:

```python
from sklearn.metrics import r2_score, mean_squared_error
```

Evaluation helps compare prediction performance.

---

# 📊 Step 7: Model Comparison

Comparison results:

| Model             | Accuracy |
| ----------------- | -------- |
| Linear Regression | Moderate |
| Random Forest     | Higher   |

Random Forest provided better prediction performance.

---

# 📉 Step 8: Visualization

Generated comparison graph:

```
Actual Closing Price vs Predicted Closing Price
```

Saved at:

```
outputs/prediction_plot.png
```

Example:

```python
plt.plot(y_test.values)
plt.plot(predictions)
```

---

# 🔮 Step 9: Sample Prediction

Example input:

```
Open = 700
High = 720
Low = 690
Volume = 30000000
```

Predicted output:

```
Estimated Tesla Closing Price
```

---

# 🚀 How to Run This Project

### Step 1: Clone Repository

```
git clone https://github.com/yourusername/Tesla-Stock-Price-Prediction.git
```

---

### Step 2: Navigate to Project Folder

```
cd Tesla-Stock-Price-Prediction
```

---

### Step 3: Create Virtual Environment

```
python -m venv venv
```

---

### Step 4: Activate Environment

Windows:

```
venv\Scripts\activate
```

---

### Step 5: Install Dependencies

```
pip install -r requirements.txt
```

---

### Step 6: Run Model

```
python src/model.py
```

---

# 📊 Output Generated

After execution:

✔ Dataset summary
✔ Missing value report
✔ Model accuracy score
✔ RMSE value
✔ Predicted Tesla price
✔ Prediction visualization graph

---

# 📌 Future Improvements

Possible enhancements:

* Add LSTM deep learning model
* Use real-time stock API integration
* Hyperparameter tuning
* Feature scaling optimization
* Deploy using Streamlit
* Build dashboard visualization

---

# 🎓 Learning Outcomes

This project demonstrates:

✔ End-to-end ML workflow
✔ Regression modeling techniques
✔ Financial dataset preprocessing
✔ Feature engineering basics
✔ Model comparison strategies
✔ Visualization skills

