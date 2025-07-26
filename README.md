# Customer Segmentation Clustering

This project applies unsupervised machine learning to retail customer data to discover actionable customer segments. By analyzing demographic and behavioral data, it enables businesses to understand their customer base, identify high-value groups, and personalize marketing efforts.

---

## Project Overview

The core objective is to segment customers into distinct groups based on their characteristics and purchasing patterns. This segmentation helps businesses answer questions such as:
- Who are my most valuable customers?
- Which customers are at risk of churning?
- What are the typical profiles of my loyal, dormant, or high-spending customers?

---

## Main Features

- **Data Preparation & Feature Engineering:** Cleans data, creates derived attributes (age, total spending, tenure), and applies feature scaling.
- **Exploratory Data Analysis (EDA):** Visualizations (histograms, boxplots, heatmaps) and statistical summaries help uncover patterns.
- **Customer Segmentation:** Clusters customers using KMeans on key variables such as age, income, spending, web/store purchases, and recency. The optimal cluster number is selected with the elbow method.
- **Cluster Profiling:** Segments are characterized by typical age, income, engagement, and spending, assisting business interpretation.
- **Interactive Segment Prediction:** A Streamlit app allows anyone to enter customer details and get instant segment predictions and descriptions.

---

## Example Cluster Profiles

- **Inactive/Low-value customers:** Older, low income, low spending, low activity, rarely purchase.
- **Premium loyal customers:** Older, high income, high spending, frequent, loyal.
- **Active senior buyers:** Oldest with good income, moderate spending/activity, recent purchases.
- **Dormant/Low-value customers:** Younger, low income/spending, low activity, recent purchases.
- **Affluent, engaged customers:** Older, highest income and spending, most active.
- **Affluent, active young customers:** Young, highest income/spending, especially active in store purchases.

---

## Business Value

- **Targeted Marketing:** Run more effective, segment-specific campaigns.
- **Customer Retention:** Identify and re-engage segments at risk of churning.
- **Resource Allocation:** Focus attention and offers on strategically important groups.
- **Personalization:** Deliver tailored experiences and recommendations.

---

## Data Source

Data used in this project comes from the public Kaggle dataset:  
[Customer Segmentation Clustering – Kaggle](https://www.kaggle.com/datasets/vishakhdapat/customer-segmentation-clustering)

It contains anonymized customer demographics, purchasing history, and campaign response information, making it suitable for unsupervised customer segmentation analysis.

---

## Technologies Used

- Python (pandas, numpy, scikit-learn, joblib)
- Jupyter Notebook for analysis and modeling
- Streamlit for deployment and real-time predictions
