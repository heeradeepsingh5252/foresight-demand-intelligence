# 📊 Foresight Demand Intelligence

An end-to-end demand forecasting and inventory intelligence project
built using Python, Pandas, Scikit-learn, Matplotlib, and Streamlit.

## 🎯 Project Objective

Foresight analyzes historical sales data and predicts future product
demand to help businesses make better inventory and planning decisions.

## 🚀 Key Features

- Data inspection and cleaning
- Exploratory Data Analysis (EDA)
- Daily demand analysis
- SKU-level revenue analysis
- Units-sold analysis
- Demand forecasting
- Random Forest regression model
- Model evaluation using MAE, RMSE, and R²
- Feature importance analysis
- 30-day future demand forecast
- Interactive Streamlit dashboard

## 🤖 Machine Learning

### Model
Random Forest Regressor

### Features

- Lag 1
- Lag 7
- Lag 30
- Rolling 7-day average
- Rolling 30-day average

### Model Performance

- MAE: ~29.36 units
- RMSE: ~44.79 units
- R²: ~0.725

## 📈 Dashboard

The Streamlit dashboard provides:

- Total Revenue
- Total Units Sold
- Average Daily Demand
- 30-Day Forecast Average
- Historical Demand
- Actual vs Predicted Demand
- Future Demand Forecast

## 🛠️ Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Jupyter Notebook

## 📁 Project Structure

```text
Foresight/
├── app/
├── data/
├── models/
├── notebooks/
├── reports/
├── service/
├── src/
├── README.md
├── requirements.txt
└── .gitignore