import streamlit as st
import yfinance as yf
from datetime import date

st.set_page_config(
    page_title="Ahmed's StockHub",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    body {
        background-color: #f8f9fa;
        font-family: 'Arial', sans-serif;
    }
    h1 {
        font-size: 42px;
        text-align: center;
        color: #2C3E50;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .sub-header {
        font-size: 22px;
        text-align: center;
        color: #5D6D7E;
        margin-bottom: 30px;
    }
    .box {
        background: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.1);
        text-align: center;
        font-size: 20px;
    }
    .sidebar .sidebar-content {
        padding-top: 30px;
    }
    .stButton button {
        background-color: #007BFF;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
    }
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown(
        "<h1 style='color: #007BFF; text-align: center;'>Ahmed's StockHub 📈</h1>",
        unsafe_allow_html=True,
    )
    st.info(
        "Welcome to **Ahmed's StockHub**, a platform to easily fetch and analyze stock market data!"
    )
    st.markdown("---")
    section = st.selectbox("Navigate", ["Stock Data", "About Ahmed"])

st.markdown("<h1>Welcome to Ahmed's StockHub 📊</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Analyze and Download Stock Market Data with Ease</p>", unsafe_allow_html=True)

if section == "Stock Data":
    st.markdown("## 🔎 Fetch Historical Stock Data")

    stock_list = [
        "AAPL", "MSFT", "AMZN", "GOOGL", "META", "TSLA", "NVDA", "JPM", "V", "WMT"
    ]
    selected_ticker = st.selectbox("Select a Stock Ticker", stock_list)

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date:", value=date(2015, 1, 1))
    with col2:
        end_date = st.date_input("End Date:", value=date.today())

    if st.button("📥 Fetch Data"):
        with st.spinner("Fetching data..."):
            data = yf.download(selected_ticker, start=start_date, end=end_date)
        if not data.empty:
            st.success("✅ Data retrieved successfully!")
            st.dataframe(data.reset_index(), use_container_width=True)
            csv_data = data.to_csv(index=True)
            st.download_button(
                label="💾 Download CSV",
                data=csv_data,
                file_name=f"{selected_ticker}_data.csv",
                mime="text/csv",
            )
        else:
            st.warning("⚠ No data available for the selected period.")

elif section == "About Ahmed":
    st.markdown("<h1 style='text-align: center; color: #2C3E50;'>About Ahmed Hasnain</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='box'>
        <p style='font-size: 18px; color: #5D6D7E;'>
        Hi, I'm <strong>Ahmed Hasnain</strong>, a passionate Data Scientist specializing in AI, ML, and Data Analytics.
        My goal is to transform data into actionable insights that drive real-world impact.
        Connect with me on <a href='https://github.com/Ahmedmoria' target='_blank'>GitHub</a> and <a href='https://linkedin.com/in/ahmedhasnain' target='_blank'>LinkedIn</a>!
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <hr>
    <p style="text-align: center; color: #95A5A6;">
    Built with ❤️ by <a href="https://linkedin.com/in/ahmedhasnain" target="_blank">Ahmed Hasnain</a>
    </p>
    """,
    unsafe_allow_html=True,
)
