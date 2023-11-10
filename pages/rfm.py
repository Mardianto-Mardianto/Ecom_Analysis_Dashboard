import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime
from babel.numbers import format_currency

customer_df = pd.read_csv("E-Commerce Public Dataset/customers_dataset.csv")
seller_df = pd.read_csv("E-Commerce Public Dataset/sellers_dataset.csv")
rfm_df = pd.read_csv("E-Commerce Public Dataset/rfm_df.csv")
rfm_rank_df = pd.read_csv("E-Commerce Public Dataset/rfm_rank.csv")
order_items_product_df = pd.read_csv("E-Commerce Public Dataset/order_items_product_df.csv")

with st.sidebar:
    # Menambahkan logo perusahaan
    st.sidebar.success("Select Any Page from here") 
    
st.title('RFM Analysis')

col1, col2, col3 = st.columns(3)

with col1:
    avg_recency = round(rfm_df.Recency.mean(), 1)
    st.metric("Average Recency (days)", value=avg_recency)
 
with col2:
    avg_frequency = round(rfm_df.Frequency.mean(), 2)
    st.metric("Average Frequency", value=avg_frequency)
 
with col3:
    avg_frequency = format_currency(rfm_df.Monetary.mean(), "BR", locale="pt_BR") 
    st.metric("Average Monetary", value=avg_frequency)

tab1, tab2, tab3 = st.tabs(["Recency", "Frequency", "Monetary"])

with tab1 :
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(y="Recency", x="CustomerId", data=rfm_df.sort_values(by="Recency", ascending=True).head(5), palette="rainbow")
    ax.set_ylabel(None)
    ax.set_xlabel("CustomerId", fontsize=30)
    ax.set_title("By Recency (days)", loc="center", fontsize=50)
    ax.tick_params(axis='y', labelsize=30)
    ax.tick_params(axis='x', labelsize=25, rotation=45)

    st.pyplot(fig)

with tab2 :
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(y="Frequency", x="CustomerId", data=rfm_df.sort_values(by="Frequency", ascending=False).head(5), palette="rainbow")
    ax.set_ylabel(None)
    ax.set_xlabel("CustomerId", fontsize=30)
    ax.set_title("By Frequency", loc="center", fontsize=50)
    ax.tick_params(axis='y', labelsize=30)
    ax.tick_params(axis='x', labelsize=25, rotation=45)

    st.pyplot(fig)

with tab3 :
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(y="Monetary", x="CustomerId", data=rfm_df.sort_values(by="Monetary", ascending=False).head(5), palette="rainbow")
    ax.set_ylabel(None)
    ax.set_xlabel("CustomerId", fontsize=30)
    ax.set_title("By Monetary", loc="center", fontsize=50)
    ax.tick_params(axis='y', labelsize=30)
    ax.tick_params(axis='x', labelsize=25, rotation=45)
    
    st.pyplot(fig)

st.subheader("RFM Score")

col4, col5 = st.columns(2)

with col4:
    avg_rfm = round(rfm_df.RFM_Score.mean(), 2)
    st.metric("Average RFM Score", value=avg_rfm)
 
with col5:
    top_cust_segment = rfm_df.Customer_segment.mode()[0]
    st.metric("Top Customer Segment", value=top_cust_segment)

fig, ax = plt.subplots(figsize=(20, 10))

plt.pie(rfm_df.Customer_segment.value_counts(),
        labels=rfm_df.Customer_segment.value_counts().index,
        wedgeprops = {'width': 0.4},
        autopct='%.0f%%')

st.pyplot(fig)