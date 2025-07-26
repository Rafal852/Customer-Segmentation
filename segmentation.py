import streamlit as st
import pandas as pd
import numpy as np
import joblib


kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Customer Segmentation App")
st.write("Enter customer details to predict the segment.")

age = st.number_input("Age", min_value=18, max_value=100, value=18)
income = st.number_input("Income", min_value=0, max_value=2000000, value=0)
total_spending = st.number_input("Total Spending(sum of purchases)", min_value=0, max_value=5000, value=0)
num_web_purchases = st.number_input("Number of Web Purchases", min_value=0, max_value=100, value=0)
num_store_purchases = st.number_input("Number of Store Purchases", min_value=0, max_value=100, value=0)
recency = st.number_input("Recency(days since last purchase)", min_value=0, max_value=365, value=0)


input_data = pd.DataFrame({
    "Age" : [age],
    "Income" : [income],
    "Total_Spending" : [total_spending],
    "NumWebPurchases" : [num_web_purchases],
    "NumStorePurchases" : [num_store_purchases],
    "Recency" : [recency]
})

input_scaled = scaler.transform(input_data)

cluster_profiles = {
    0: "Inactive/Low-value customers: Older, low income, low spending, low purchase activity, high recency.",
    1: "Premium loyal customers: Older, high income, high spending, high purchase activity, high recency.",
    2: "Active senior buyers: Oldest, high income, moderate spending, moderate purchase activity, very recent.",
    3: "Dormant/Low-value customers: Younger, low income, very low spending, low purchase activity, very recent.",
    4: "Affluent, engaged customers: Older, highest income, highest spending, highest purchase activity, high recency.",
    5: "Affluent, active young customers: Youngest, highest income, highest spending, high store purchases, moderate recency."
}

if st.button("Predict Segment"):
    cluster = kmeans.predict(input_scaled)[0]

    st.success(f"Predicted Segment: Cluster {cluster}")

    st.info(cluster_profiles.get(cluster, "No profile available for this segment."))