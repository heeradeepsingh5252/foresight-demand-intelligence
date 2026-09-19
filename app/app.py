import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
sales = pd.read_csv("data/processed/sales_clean.csv")
predictions = pd.read_csv("data/processed/demand_predictions.csv")
# Convert dates
sales["Date"] = pd.to_datetime(sales["Date"])
predictions["Date"] = pd.to_datetime(predictions["Date"])

print("Data loaded successfully.")

# Dashboard title
st.set_page_config(
    page_title="Foresight Demand Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Foresight Demand Intelligence")
st.write("Demand forecasting and inventory intelligence dashboard")

# Key Performance Indicators

total_revenue = sales["Revenue"].sum()
total_units = sales["Units_Sold"].sum()
average_daily_demand = sales.groupby("Date")["Units_Sold"].sum().mean()
forecast_average = predictions["Predicted"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Revenue",
    f"₹{total_revenue:,.0f}"
)

col2.metric(
    "Total Units Sold",
    f"{total_units:,.0f}"
)

col3.metric(
    "Avg Daily Demand",
    f"{average_daily_demand:,.0f}"
)

col4.metric(
    "30-Day Forecast Avg",
    f"{forecast_average:,.0f}"
)

# Historical demand

daily_demand = (
    sales.groupby("Date")["Units_Sold"]
    .sum()
    .reset_index()
)

st.subheader("📈 Historical Demand")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    daily_demand["Date"],
    daily_demand["Units_Sold"]
)

ax.set_xlabel("Date")
ax.set_ylabel("Units Sold")
ax.set_title("Daily Demand Trend")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# 30-Day Demand Forecast

st.subheader("🔮 30-Day Demand Forecast")

fig2, ax2 = plt.subplots(figsize=(12, 5))

ax2.plot(
    predictions["Date"],
   predictions["Predicted"],
    marker="o"
)

ax2.set_xlabel("Date")
ax2.set_ylabel("Predicted Units Sold")
ax2.set_title("Predicted Demand")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig2)

# Actual vs Predicted Demand

st.subheader("🎯 Actual vs Predicted Demand")

fig3, ax3 = plt.subplots(figsize=(12, 5))

ax3.plot(
    predictions["Date"],
    predictions["Actual"],
    label="Actual"
)

ax3.plot(
    predictions["Date"],
    predictions["Predicted"],
    label="Predicted"
)

ax3.set_xlabel("Date")
ax3.set_ylabel("Units Sold")
ax3.set_title("Model Performance")

ax3.legend()

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig3)