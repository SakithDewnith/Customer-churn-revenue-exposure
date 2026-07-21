import os
import pandas as pd
import plotly.express as px
import streamlit as st

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError



# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Customer Retention Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>

    /* Main page background */
[data-testid="stAppViewContainer"] {
    background-color: #F8FAFC;
}

    /* Hide Streamlit top bar */
    header[data-testid="stHeader"] {
        display: none;
    }

    /* Remove top empty space */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 1rem !important;
    }

    /* 
       --- FIXED HEADER & STOP OVERLAP --- 
    */
    div[data-testid="stVerticalBlock"] > div:has(h2) {
        position: sticky !important;
        top: 0 !important;
        z-index: 999999 !important; 
        
        background-color: #EFF6FF !important;
        border-bottom: 1px solid #2563EB !important;
        
        /* Creates a solid edge below the header to block elements from peeking through */
        box-shadow: 0px 1px 0px 0px #FFFFFF !important; 
    }

    /* Makes Streamlit's native bordered containers look like white UI cards */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF !important;
        border-radius: 12px !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.02) !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# HEADER ROW
# =====================================================

with st.container():

    title_col = st.container()

    st.markdown(
        """
        <h2 style="
            margin:0;
            padding:0;
            font-size:30px;
            font-weight:700;
            color:#1E293B;
        ">
        Customer Retention & Churn Risk Analytics Dashboard
        </h2>

        <p style="
            margin-top:5px;
            color:#64748B;
            font-size:14px;
        ">
        Analyze future revenue exposure using historical churn patterns.
        </p>
        """,
        unsafe_allow_html=True
    )


# =====================================================
# DATABASE CONNECTION
# =====================================================

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    st.error(
        "DATABASE_URL not found. Check your .env file."
    )
    st.stop()


@st.cache_resource
def get_engine():

    return create_engine(
        DATABASE_URL,
        pool_pre_ping=True
    )


engine = get_engine()



# =====================================================
# LOAD DATABASE TABLES
# =====================================================

@st.cache_data(ttl=3600)
def load_tables():

    try:

        customers = pd.read_sql(
            "SELECT * FROM churn_cleaned",
            engine
        )


        contract = pd.read_sql(
            "SELECT * FROM contract_analysis",
            engine
        )


        drivers = pd.read_sql(
            "SELECT * FROM driver_analysis",
            engine
        )


        future = pd.read_sql(
            "SELECT * FROM future_revenue_exposure",
            engine
        )


    except SQLAlchemyError as e:

        st.error(
            f"Database loading error: {e}"
        )

        st.stop()


    return customers, contract, drivers, future



df, contract_df, driver_df, future_df = load_tables()



df["monthly_charges"] = pd.to_numeric(
    df["monthly_charges"],
    errors="coerce"
)





# =====================================================
# SIDEBAR FILTERS
# =====================================================

st.sidebar.header(
    "Customer Filters"
)



def create_filter(title, column):

    if column in df.columns:

        return st.sidebar.multiselect(
            title,
            sorted(
                df[column]
                .dropna()
                .unique()
            )
        )

    return []



contract_filter = create_filter(
    "Contract Type",
    "contract"
)


tech_filter = create_filter(
    "Tech Support",
    "tech_support"
)


security_filter = create_filter(
    "Online Security",
    "online_security"
)


payment_filter = create_filter(
    "Payment Method",
    "payment_method"
)



filtered_df = df.copy()



filters = [

    ("contract", contract_filter),

    ("tech_support", tech_filter),

    ("online_security", security_filter),

    ("payment_method", payment_filter)

]



for column, selected in filters:

    if selected:

        filtered_df = filtered_df[
            filtered_df[column]
            .isin(selected)
        ]



st.sidebar.caption(
    f"Showing {len(filtered_df):,} customers"
)



if filtered_df.empty:

    st.warning(
        "No data matches the selected filters."
    )

    st.stop()


# =====================================================
# KPI CARDS
# =====================================================

# 1. Total projected revenue exposure
revenue_exposure = contract_df[
    "future_revenue_exposure"
].sum()

# 2. Estimated at-risk customers
contract_df["estimated_at_risk_customers"] = (
    contract_df["active_customers"]
    *
    contract_df["churn_rate"]
    /
    100
)

at_risk_customers = (
    contract_df["estimated_at_risk_customers"]
    .sum()
    .round()
)

# 3. Revenue exposure rate
revenue_exposure_rate = (
    revenue_exposure
    /
    contract_df["active_revenue"].sum()
) * 100

# 4. Average customer value at risk
avg_customer_value = (
    revenue_exposure
    /
    at_risk_customers
)


# CSS
st.markdown(
    """
    <style>
    .kpi-card {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 18px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 8px rgba(15,23,42,0.05);
        height: 105px;
    }
    .kpi-title {
        font-size: 12px;
        color: #64748B;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: .4px;
    }
    .kpi-value {
        font-size: 26px;
        font-weight: 700;
        color: #1E293B;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def show_kpi(title, value, border_color):
    st.markdown(
        f"""
        <div class="kpi-card" style="border-top: 4px solid {border_color};">
            <div class="kpi-title">{title}</div>
            <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


col1, col2, col3, col4 = st.columns(4)

with col1:
    show_kpi("Revenue Exposure", f"${revenue_exposure:,.0f}/mo", "#EF4444") # Red for risk

with col2:
    show_kpi("At-Risk Customers", f"{at_risk_customers:.0f}", "#F59E0B") # Amber for warning

with col3:
    show_kpi("Revenue Exposure Rate", f"{revenue_exposure_rate:.2f}%", "#6366F1") # Indigo

with col4:
    show_kpi("Avg. Customer Value", f"${avg_customer_value:,.0f}/mo", "#10B981") # Green for value

st.markdown("<br>", unsafe_allow_html=True)


# =====================================================
# Future Revenue Exposure Analysis
# =====================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    """
    <h3 style="
        margin-top:10px;
        margin-bottom:10px;
        font-size:24px;
        font-weight:700;
    ">
    📈 Future Revenue Exposure Analysis
    </h3>
    """,
    unsafe_allow_html=True
)
# -----------------------------------------
# Contract Analysis
# -----------------------------------------

col1, col2 = st.columns(2)


with col1:
    # WRAP IN A NATIVE CONTAINER TO CREATE THE CARD
    with st.container(border=True):

        st.markdown(
            """
            <h4 style="
                margin-bottom:2px;
                font-size:18px;
                font-weight:600;
            ">
            Contract Segment Analysis (Priority Segment)
            </h4>
            """,
            unsafe_allow_html=True
        )
        
        revenue_contract = contract_df[
            [
              "contract",
            "future_revenue_exposure"
            ]
        ].copy()

        revenue_contract.columns = [
            "contract",
            "revenue_exposure"
        ]
        
        # 1. Calculate a dynamic max value to add headroom
        max_y = revenue_contract["revenue_exposure"].max()
        
        fig = px.bar(
            revenue_contract,
            x="contract",
            y="revenue_exposure",
            text="revenue_exposure",
            color="contract",
            color_discrete_map={
                "Month-to-month": "#EF4444",
                "One year": "#FBBF24",
                "Two year": "#10B981"
            }
        )

        fig.update_traces(
            texttemplate="$%{text:,.0f}",
            textposition="outside",
            cliponaxis=False # 2. Prevents text from being cropped by the boundary
        )

        fig.update_layout(
            height=240,
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            margin=dict(l=40, r=40, t=0, b=0), # Increased top margin slightly for breathing room
            xaxis=dict(
                showgrid=False,
                title=""
            ),
            yaxis=dict(
                gridcolor="#F1F5F9",
                title="",
                range=[0, max_y * 1.2] # 3. Extends the y-axis 20% higher than the tallest bar
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

with col2:
    # WRAP IN A NATIVE CONTAINER TO CREATE THE CARD
     with st.container(border=True):

        st.markdown(
            """
            <h4 style="
                margin-bottom:5px;
                font-size:18px;
                font-weight:600;
            ">
            Month-to-month Contract Drivers
            </h4>
            """,
            unsafe_allow_html=True
        )

        # Get top 5 drivers by revenue exposed to fit perfectly in the card height
        driver_chart = future_df.sort_values("revenue_exposed", ascending=True).tail(5)

        # 1. Calculate a dynamic max value to add headroom to the X-AXIS
        max_x = driver_chart["revenue_exposed"].max()

        fig = px.bar(
            driver_chart,
            x="revenue_exposed",
            y="driver",
            orientation="h",
            text="revenue_exposed",
            color_discrete_sequence=["#334155"] # Slate gray to complement the red and blue
        )

        fig.update_traces(
            texttemplate="$%{text:,.0f}",
            textposition="outside",
            cliponaxis=False # 2. Prevents text from being cropped by the chart boundary
        )

        fig.update_layout(
            height=240,
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            # Increased 'l' to fit long driver names, and 'r' to fit the outside numbers
            margin=dict(l=100, r=40, t=40, b=0), 
            xaxis=dict(
                showgrid=False,
                showticklabels=False, # Hides bottom numbers to keep it clean
                title="",
                range=[0, max_x * 1.25] # 3. Extends the X-axis 25% further to the right
            ),
            yaxis=dict(
                gridcolor="#F1F5F9",
                title=""
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
st.markdown("<br>", unsafe_allow_html=True)


st.markdown(
    """
    <div style="
        background-color: #F8FAFC; /* Light gray-blue background */
        border-left: 5px solid #0EA5E9; /* Your Streamlit blue color */
        padding: 15px;
        border-radius: 4px;
        margin-top: 15px;
    ">
        <p style="
            margin: 0; 
            font-size: 14px; 
            color: #334155; /* Slate text color */
            line-height: 1.5;
        ">
            <strong>💡 Key Finding:</strong>  Month-to-month customers have the highest projected revenue exposure, with missing Tech Support and Online Security identified as the main risk drivers.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


st.divider()



# =====================================================
# RETENTION OPPORTUNITIES
# =====================================================

st.markdown(
"""
<h3 style="
    margin-top:20px;
    margin-bottom:10px;
    font-size:24px;
    font-weight:700;
">
🎯 Retention Opportunities
</h3>

<p style="
    margin-top:0px;
    margin-bottom:15px;
    color:#64748B;
    font-size:14px;
">
Potential actions identified from high-risk customer segments.
</p>
""",
unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)

card_height = "170px"

with col1:
    with st.container():
        st.markdown(
        f"""
        <div style="height:{card_height}; background-color:#DBEAFE; padding:15px; border-radius:10px;">

        <h4 style="
            margin-top:0;
            margin-bottom:10px;
            font-size:17px;
            font-weight:600;
            color:#1E3A8A;
        ">
        🔄 Contract Upgrade
        </h4>

        <p style="
            margin:0;
            font-size:14px;
            color:#334155;
        ">
        <b>Target:</b> Month-to-month customers
        </p>

        <p style="
            margin-top:10px;
            font-size:14px;
            color:#334155;
        ">
        Evaluate contract upgrade campaigns to encourage longer-term customer commitment.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )


with col2:
    with st.container():
        st.markdown(
        f"""
        <div style="height:{card_height}; background-color:#FEF9C3; padding:15px; border-radius:10px;">

        <h4 style="
            margin-top:0;
            margin-bottom:10px;
            font-size:17px;
            font-weight:600;
            color:#92400E;
        ">
        🛠 Tech Support Adoption
        </h4>

        <p style="
            margin:0;
            font-size:14px;
            color:#334155;
        ">
        <b>Target:</b> Month-to-month customers without Tech Support.
        </p>

        <p style="
            margin-top:10px;
            font-size:14px;
            color:#334155;
        ">
        Evaluate Tech Support adoption campaigns to improve customer retention.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )


with col3:
    with st.container():
        st.markdown(
        f"""
        <div style="height:{card_height}; background-color:#DCFCE7; padding:15px; border-radius:10px;">

        <h4 style="
            margin-top:0;
            margin-bottom:10px;
            font-size:17px;
            font-weight:600;
            color:#166534;
        ">
        🔒 Online Security Adoption
        </h4>

        <p style="
            margin:0;
            font-size:14px;
            color:#334155;
        ">
        <b>Target:</b> Month-to-month customers without Online Security
        </p>

        <p style="
            margin-top:10px;
            font-size:14px;
            color:#334155;
        ">
        Evaluate Online Security adoption campaigns to reduce customer churn.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )