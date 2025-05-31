import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

df = pd.read_csv("transactions.csv")

st.title("Fraud Detection Dashboard")

st.metric("Total Transactions", len(df))
st.metric("Rule-Based Fraud", df["rule_fraud"].sum())
st.metric("ML-Predicted Fraud", df["ml_fraud"].sum())

with st.sidebar:
    st.header("Filters")
    min_amt, max_amt = st.slider("Transaction Amount", 0, int(df["amount"].max()), (0, 1000))
    fraud_type = st.selectbox("Fraud Type", ["All", "Rule-Based", "ML Predicted"])
    
filtered_df = df[(df["amount"] >= min_amt) & (df["amount"] <= max_amt)]
if fraud_type == "Rule-Based":
    filtered_df = filtered_df[filtered_df["rule_fraud"] == 1]
elif fraud_type == "ML Predicted":
    filtered_df = filtered_df[filtered_df["ml_fraud"] ==1]
    
st.subheader("Filtered Transactions")
st.dataframe(filtered_df)

st.subheader("Fraud by Hour")
chart_data = filtered_df.groupby("hour")[["rule_fraud", "ml_fraud"]].sum().reset_index()
st.bar_chart(chart_data.set_index("hour"))