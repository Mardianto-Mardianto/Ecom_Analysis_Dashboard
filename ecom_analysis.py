import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime

customer_df = pd.read_csv("E-Commerce Public Dataset/customers_dataset.csv")
#geolocation_df = pd.read_csv("E-Commerce Public Dataset/geolocation_dataset.csv")
#order_items_df = pd.read_csv("E-Commerce Public Dataset/order_items_dataset.csv")
#order_payment_df = pd.read_csv("E-Commerce Public Dataset/order_payments_dataset.csv")
#order_reviews_df = pd.read_csv("E-Commerce Public Dataset/order_reviews_dataset.csv")
#orders_df = pd.read_csv("E-Commerce Public Dataset/orders_dataset.csv")
#product_category_df = pd.read_csv("E-Commerce Public Dataset/product_category_name_translation.csv")
#product_df = pd.read_csv("E-Commerce Public Dataset/products_dataset.csv")
seller_df = pd.read_csv("E-Commerce Public Dataset/sellers_dataset.csv")
rfm_df = pd.read_csv("E-Commerce Public Dataset/rfm_df.csv")
order_items_product_df = pd.read_csv("E-Commerce Public Dataset/order_items_product_df.csv")

st.set_page_config(page_title = "Ecommerce Analysis") 
st.title('Top Category Products')

with st.sidebar:
    # Menambahkan logo perusahaan
    st.sidebar.success("Select Any Page from here") 

top = order_items_product_df['product_category_name'].value_counts(ascending=False)
top3 = top.index.tolist()[:3]

# with st.container():
#     st.image("https://static.vecteezy.com/system/resources/previews/011/188/868/non_2x/1st-2nd-3rd-medal-first-place-second-third-award-winner-badge-guarantee-winning-prize-ribbon-symbol-sign-icon-logo-template-clip-art-illustration-vector.jpg")
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.header(top3[0])
#     with col2:
#         st.header(top3[1])
#     with col3:
#         st.header(top3[2])

col1, col2 = st.columns([1,5])

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3377/3377937.png", width=80)
with col2:
    st.subheader(top3[0])

col3, col4 = st.columns([1, 5])

with col3:
    st.image("https://cdn-icons-png.flaticon.com/512/3379/3379061.png", width=80)
with col4:
    st.subheader(top3[1])

col5, col6 = st.columns([1, 5])

with col5:
    st.image("https://cdn-icons-png.flaticon.com/512/3379/3379178.png", width=80)
with col6:
    st.subheader(top3[2])

col7, col8 = st.columns([1,9])

with col7:
    number = st.number_input("Top", value=5, min_value=1)

with col8:
    title = "Top {} Category Product"
    #st.subheader(title.format(number))

    fig, ax = plt.subplots(figsize=(20, 10))
        
    sns.countplot(order_items_product_df,
                y="product_category_name",
                order=order_items_product_df['product_category_name'].value_counts(ascending=False).iloc[:number].index,
                palette="spring",
                )
    ax.set_title(title.format(number), loc="center", fontsize=30)
    st.pyplot(fig)

st.table(top.iloc[:number])
