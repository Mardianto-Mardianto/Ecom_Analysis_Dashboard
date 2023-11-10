import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime

customer_df = pd.read_csv("E-Commerce Public Dataset/customers_dataset.csv")
seller_df = pd.read_csv("E-Commerce Public Dataset/sellers_dataset.csv")
rfm_df = pd.read_csv("E-Commerce Public Dataset/rfm_df.csv")
rfm_rank_df = pd.read_csv("E-Commerce Public Dataset/rfm_rank.csv")
order_items_product_df = pd.read_csv("E-Commerce Public Dataset/order_items_product_df.csv")

with st.sidebar:
    # Menambahkan logo perusahaan
    st.sidebar.success("Select Any Page from here") 
    

st.title('Customer and Seller Demography')

tab1, tab2 = st.tabs(["Customer", "Seller"])

with tab1 :
    st.subheader("Customer Demographics")

    col1, col2, col3 = st.columns(3)

    top_cities = customer_df['customer_city'].value_counts(ascending=False)
    top_city = top_cities.index.tolist()[0]

    top_states = customer_df['customer_state'].value_counts(ascending=False)
    top_state = top_states.index.tolist()[0]

    with col1:
        st.metric(label="#Customer", value= customer_df.shape[0])
    
    with col2:
        st.metric(label="Top City", value= top_city)
    
    with col3 :
        st.metric(label="Top State", value= top_state)
    
    fig, ax = plt.subplots(figsize=(20, 10))
            
    sns.countplot(customer_df,
                y="customer_state",
                order=customer_df['customer_state'].value_counts(ascending=False).index,
                palette="rainbow",
                )
    ax.set_title("Number of Customer by State", loc="center", fontsize=30)
    st.pyplot(fig)

    st.table(customer_df['customer_state'].value_counts(ascending=False))

with tab2 :
    st.subheader("Seller Demographics")

    col1, col2, col3 = st.columns(3)

    top_cities_s = seller_df['seller_city'].value_counts(ascending=False)
    top_city_s = top_cities_s.index.tolist()[0]

    top_states_s = seller_df['seller_state'].value_counts(ascending=False)
    top_state_s = top_states_s.index.tolist()[0]

    with col1:
        st.metric(label="#Seller", value= seller_df.shape[0])
    
    with col2:
        st.metric(label="Top City", value= top_city_s)
    
    with col3 :
        st.metric(label="Top State", value= top_state_s)

    fig, ax = plt.subplots(figsize=(20, 10))
            
    sns.countplot(seller_df,
                y="seller_state",
                order=seller_df['seller_state'].value_counts(ascending=False).index,
                palette="rainbow",
                )
    ax.set_title("Number of Seller by State", loc="center", fontsize=30)
    st.pyplot(fig)

    st.table(seller_df['seller_state'].value_counts(ascending=False))



