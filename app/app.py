import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Foresight Demand Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown('''
<style>

/* ================================
   MAIN BACKGROUND
   ================================ */

.stApp {
    background-color: #080d1a;
}


/* ================================
   SIDEBAR
   ================================ */

section[data-testid="stSidebar"] {
    background-color: #080d1a;
    border-right: 1px solid #1f2937;
}

section[data-testid="stSidebar"] > div {
    padding-top: 2rem;
}

section[data-testid="stSidebar"] * {
    color: #d1d5db !important;
}


/* ================================
   MAIN CONTAINER
   ================================ */

.block-container {
    padding-top: 4rem;
}
/* Keep dashboard content below Streamlit top toolbar */
[data-testid="stAppViewContainer"] {
    padding-top: 0 !important;
}

.block-container {
    padding-top: 4rem !important;
}

/* ================================
   DASHBOARD HEADINGS
   ================================ */

.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4 {
    color: #f8fafc !important;
}


/* ================================
   KPI CARDS
   ================================ */

.metric-card {
    color: #f8fafc !important;
    opacity: 1 !important;
}

.metric-card * {
    opacity: 1 !important;
}

.metric-title {
    color: #94a3b8 !important;
    font-size: 14px;
    opacity: 1 !important;
}

.metric-value {
    color: #f8fafc !important;
    font-size: 30px;
    font-weight: 700;
    opacity: 1 !important;
}

.metric-subtitle {
    color: #94a3b8 !important;
    opacity: 1 !important;
}


/* ================================
   BUSINESS INSIGHTS
   ================================ */

.section-card {
    color: #f8fafc !important;
    opacity: 1 !important;
}

.section-card * {
    opacity: 1 !important;
}

.section-card .muted,
.muted {
    color: #94a3b8 !important;
    opacity: 1 !important;
}


/* ================================
   GENERAL CUSTOM TEXT
   ================================ */

.stApp p {
    opacity: 1 !important;
}


/* ================================
   SELECTBOX
   ================================ */

div[data-baseweb="select"] * {
    color: #1f2937 !important;
}


/* ================================
   CAPTIONS
   ================================ */

[data-testid="stCaptionContainer"] {
    color: #94a3b8 !important;
    opacity: 1 !important;
}


/* ================================
   HIDE STREAMLIT MENU / FOOTER
   ================================ */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
''', unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    sales = pd.read_csv(
        "data/processed/sales_clean.csv"
    )

    predictions = pd.read_csv(
        "data/processed/demand_predictions.csv"
    )

    sales["Date"] = pd.to_datetime(sales["Date"])
    predictions["Date"] = pd.to_datetime(predictions["Date"])

    return sales, predictions


sales, predictions = load_data()


# =========================================================
# CALCULATE KPIs
# =========================================================

total_revenue = sales["Revenue"].sum()

total_units = sales["Units_Sold"].sum()

average_daily_demand = (
    sales.groupby("Date")["Units_Sold"]
    .sum()
    .mean()
)

forecast_average = predictions["Predicted"].mean()

forecast_max = predictions["Predicted"].max()

forecast_min = predictions["Predicted"].min()

historical_average = (
    sales.groupby("Date")["Units_Sold"]
    .sum()
    .mean()
)

forecast_change = (
    (forecast_average - historical_average)
    / historical_average
) * 100


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            font-size:25px;
            font-weight:700;
            color:#f8fafc;
            margin-bottom:5px;
        ">
        📊 FORESIGHT
        </div>

        <div style="
            color:#64748b;
            font-size:13px;
            margin-bottom:30px;
        ">
        Demand Intelligence Platform
        </div>
        """,
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        [
            "Executive Dashboard",
            "Demand Forecast",
            "Model Performance",
            "Sales Analytics"
        ]
    )

    st.markdown("---")

    st.markdown(
        """
        <div class="muted">
        AI-powered demand forecasting<br>
        & inventory intelligence
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            margin-top:30px;
            color:#475569;
            font-size:12px;
        ">
        FORESIGHT v1.0
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# EXECUTIVE DASHBOARD
# =========================================================

if page == "Executive Dashboard":

    st.title("Executive Dashboard")

    st.markdown(
        """
        <div class="muted">
        Demand forecasting and inventory intelligence
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")


    # =====================================================
    # KPI CARDS
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">TOTAL REVENUE</div>
                <div class="metric-value">₹{total_revenue / 1e9:.2f}B</div>
                <div class="metric-subtitle">
                    Overall sales revenue
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">UNITS SOLD</div>
                <div class="metric-value">{total_units:,.0f}</div>
                <div class="metric-subtitle">
                    Total units sold
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">AVG DAILY DEMAND</div>
                <div class="metric-value">{average_daily_demand:,.0f}</div>
                <div class="metric-subtitle">
                    Units per day
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">30-DAY FORECAST</div>
                <div class="metric-value">{forecast_average:,.0f}</div>
                <div class="metric-subtitle">
                    Average predicted demand
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown("<br>", unsafe_allow_html=True)


    # =====================================================
    # FORECAST SIGNALS
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        trend_symbol = "↓" if forecast_change < 0 else "↑"

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">FORECAST SIGNAL</div>
                <div class="metric-value">
                    {trend_symbol} {abs(forecast_change):.1f}%
                </div>
                <div class="metric-subtitle">
                    Forecast vs historical average
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">PEAK FORECAST</div>
                <div class="metric-value">
                    {forecast_max:,.0f}
                </div>
                <div class="metric-subtitle">
                    Highest predicted demand
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">FORECAST RANGE</div>
                <div class="metric-value">
                    {forecast_min:,.0f} – {forecast_max:,.0f}
                </div>
                <div class="metric-subtitle">
                    Minimum to maximum prediction
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown("<br>", unsafe_allow_html=True)


    # =====================================================
    # HISTORICAL + FORECAST
    # =====================================================

    daily_demand = (
        sales.groupby("Date")["Units_Sold"]
        .sum()
        .reset_index()
    )


col1, col2 = st.columns(2)

# =====================================
# HISTORICAL DEMAND
# =====================================

with col1:

    st.subheader("📈 Historical Demand")

    # Demand Analysis Period

    daily_demand = (
        sales.groupby("Date")["Units_Sold"]
        .sum()
        .reset_index()
    )

    period = st.selectbox(
        "📅 Demand Analysis Period",
        ["Last 30 Days", "Last 90 Days", "Last 180 Days", "All Data"]
    )

    daily_demand["Date"] = pd.to_datetime(daily_demand["Date"])

    # Filter data based on selected period
    if period == "Last 30 Days":
        start_date = daily_demand["Date"].max() - pd.Timedelta(days=30)
        filtered_demand = daily_demand[
            daily_demand["Date"] >= start_date
        ]

    elif period == "Last 90 Days":
        start_date = daily_demand["Date"].max() - pd.Timedelta(days=90)
        filtered_demand = daily_demand[
            daily_demand["Date"] >= start_date
        ]

    elif period == "Last 180 Days":
        start_date = daily_demand["Date"].max() - pd.Timedelta(days=180)
        filtered_demand = daily_demand[
            daily_demand["Date"] >= start_date
        ]

    else:
        filtered_demand = daily_demand.copy()

    historical_chart = px.line(
        filtered_demand,
        x="Date",
        y="Units_Sold"
    )

    historical_chart.update_traces(
        mode="lines",
        line_width=2
    )

    historical_chart.update_layout(
        template="plotly_dark",
        height=390,
        margin=dict(
            l=10,
            r=10,
            t=20,
            b=10
        ),
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        xaxis_title="",
        yaxis_title="Units",
        hovermode="x unified"
    )

    st.plotly_chart(
        historical_chart,
        width="stretch"
    )
    with col2:
        st.subheader("🔮 Demand Forecast")

        forecast_chart = px.line(
            predictions,
            x="Date",
            y="Predicted"
        )

        forecast_chart.update_traces(
            mode="lines+markers",
            line_width=2
        )

        forecast_chart.update_layout(
            template="plotly_dark",
            height=390,
            margin=dict(
                l=10,
                r=10,
                t=20,
                b=10
            ),
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            xaxis_title="",
            yaxis_title="Units",
            hovermode="x unified"
        )

        st.plotly_chart(
            forecast_chart,
            width="stretch"
        )
    # =====================================================
    # BUSINESS INSIGHTS
    # =====================================================

    st.subheader("🧠 Business Insights")

    insight1, insight2, insight3 = st.columns(3)


    with insight1:

        st.markdown(
            f"""
            <div class="section-card">

            <div style="
                color:#94a3b8;
                font-size:13px;
                margin-bottom:8px;
            ">
            DEMAND SIGNAL
            </div>

            <div style="
                font-size:18px;
                font-weight:600;
                color:#f8fafc;
            ">
            {"Forecast demand is below historical levels"
            if forecast_change < 0
            else
            "Forecast demand is above historical levels"}
            </div>

            <div class="muted" style="margin-top:10px;">
            The forecast average is
            {abs(forecast_change):.1f}%
            {"lower" if forecast_change < 0 else "higher"}
            than historical average demand.
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with insight2:

        st.markdown(
            f"""
            <div class="section-card">

            <div style="
                color:#94a3b8;
                font-size:13px;
                margin-bottom:8px;
            ">
            PEAK DEMAND
            </div>

            <div style="
                font-size:18px;
                font-weight:600;
                color:#f8fafc;
            ">
            {forecast_max:,.0f} units
            </div>

            <div class="muted" style="margin-top:10px;">
            This represents the highest predicted
            daily demand in the forecast period.
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with insight3:

        st.markdown(
            f"""
            <div class="section-card">

            <div style="
                color:#94a3b8;
                font-size:13px;
                margin-bottom:8px;
            ">
            FORECAST RANGE
            </div>

            <div style="
                font-size:18px;
                font-weight:600;
                color:#f8fafc;
            ">
            {forecast_min:,.0f} – {forecast_max:,.0f}
            </div>

            <div class="muted" style="margin-top:10px;">
            Expected daily demand range
            across the forecast horizon.
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # ACTUAL VS PREDICTED
    # =====================================================

    st.subheader("🎯 Model Performance")

    performance = predictions.copy()

    performance_chart = go.Figure()

    performance_chart.add_trace(
        go.Scatter(
            x=performance["Date"],
            y=performance["Actual"],
            mode="lines",
            name="Actual",
            line=dict(width=2)
        )
    )

    performance_chart.add_trace(
        go.Scatter(
            x=performance["Date"],
            y=performance["Predicted"],
            mode="lines",
            name="Predicted",
            line=dict(width=2)
        )
    )

    performance_chart.update_layout(
        template="plotly_dark",
        height=400,
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        margin=dict(
            l=10,
            r=10,
            t=20,
            b=10
        ),
        xaxis_title="",
        yaxis_title="Units Sold",
        hovermode="x unified"
    )

    st.plotly_chart(
        performance_chart,
        use_container_width=True
    )
# =========================================================
# DEMAND FORECAST
# =========================================================

if page == "Demand Forecast":

    st.title("Demand Forecast")

    st.markdown(
        """
        <div class="muted">
        Forward-looking demand predictions generated by the forecasting model.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")


    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">AVERAGE FORECAST</div>
                <div class="metric-value">{forecast_average:,.0f}</div>
                <div class="metric-subtitle">Units per day</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">PEAK DEMAND</div>
                <div class="metric-value">{forecast_max:,.0f}</div>
                <div class="metric-subtitle">Highest prediction</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">LOW DEMAND</div>
                <div class="metric-value">{forecast_min:,.0f}</div>
                <div class="metric-subtitle">Lowest prediction</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown("")

    st.subheader("30-Day Forecast")

    fig = px.line(
        predictions,
        x="Date",
        y="Predicted"
    )

    fig.update_traces(
        mode="lines+markers",
        line_width=2
    )

    fig.update_layout(
        template="plotly_dark",
        height=500,
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        xaxis_title="Date",
        yaxis_title="Predicted Units",
        hovermode="x unified"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.subheader("Forecast Data")

    forecast_table = predictions[
        ["Date", "Predicted"]
    ].copy()

    forecast_table["Date"] = forecast_table["Date"].dt.date

    forecast_table["Predicted"] = (
        forecast_table["Predicted"]
        .round(0)
        .astype(int)
    )

    st.dataframe(
        forecast_table,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# MODEL PERFORMANCE
# =========================================================

elif page == "Model Performance":

    st.title("Model Performance")

    st.markdown(
        """
        <div class="muted">
        Comparison between actual demand and model predictions.
        </div>
        """,
        unsafe_allow_html=True
    )

    performance = predictions.copy()

    performance["Error"] = (
        performance["Actual"]
        - performance["Predicted"]
    )

    performance["Absolute Error"] = (
        performance["Error"].abs()
    )


    mae = performance["Absolute Error"].mean()

    rmse = (
        (performance["Error"] ** 2)
        .mean()
        ** 0.5
    )

    mape = (
        performance["Absolute Error"]
        / performance["Actual"].replace(0, pd.NA)
    ).mean() * 100


    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">MAE</div>
                <div class="metric-value">{mae:,.1f}</div>
                <div class="metric-subtitle">
                    Mean Absolute Error
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">RMSE</div>
                <div class="metric-value">{rmse:,.1f}</div>
                <div class="metric-subtitle">
                    Root Mean Squared Error
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">MAPE</div>
                <div class="metric-value">{mape:.1f}%</div>
                <div class="metric-subtitle">
                    Mean Absolute Percentage Error
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown("")

    st.subheader("Actual vs Predicted Demand")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=performance["Date"],
            y=performance["Actual"],
            mode="lines",
            name="Actual"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=performance["Date"],
            y=performance["Predicted"],
            mode="lines",
            name="Predicted"
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=500,
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        xaxis_title="Date",
        yaxis_title="Units Sold",
        hovermode="x unified"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.subheader("Prediction Error")

    error_chart = px.bar(
        performance,
        x="Date",
        y="Error"
    )

    error_chart.update_layout(
        template="plotly_dark",
        height=350,
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        xaxis_title="",
        yaxis_title="Prediction Error"
    )

    st.plotly_chart(
        error_chart,
        use_container_width=True
    )


# =========================================================
# SALES ANALYTICS
# =========================================================

elif page == "Sales Analytics":

    st.title("Sales Analytics")

    st.markdown(
        """
        <div class="muted">
        Historical sales and demand analysis.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")


    # Monthly revenue

    monthly_sales = (
        sales.set_index("Date")
        .resample("ME")
        .agg({
            "Revenue": "sum",
            "Units_Sold": "sum"
        })
        .reset_index()
    )


    col1, col2 = st.columns(2)


    with col1:

        st.subheader("💰 Monthly Revenue")

        revenue_chart = px.bar(
            monthly_sales,
            x="Date",
            y="Revenue"
        )

        revenue_chart.update_layout(
            template="plotly_dark",
            height=400,
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            xaxis_title="",
            yaxis_title="Revenue"
        )

        st.plotly_chart(
            revenue_chart,
            use_container_width=True
        )


    with col2:

        st.subheader("📦 Monthly Units Sold")

        units_chart = px.bar(
            monthly_sales,
            x="Date",
            y="Units_Sold"
        )

        units_chart.update_layout(
            template="plotly_dark",
            height=400,
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            xaxis_title="",
            yaxis_title="Units"
        )

        st.plotly_chart(
            units_chart,
            use_container_width=True
        )


    st.subheader("Demand Distribution")

    distribution = px.histogram(
        sales,
        x="Units_Sold",
        nbins=30
    )

    distribution.update_layout(
        template="plotly_dark",
        height=400,
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        xaxis_title="Units Sold",
        yaxis_title="Frequency"
    )

    st.plotly_chart(
        distribution,
        use_container_width=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div style="
        text-align:center;
        color:#475569;
        padding-top:40px;
        font-size:12px;
    ">
        Foresight Demand Intelligence · AI-Powered Analytics
    </div>
    """,
    unsafe_allow_html=True
)