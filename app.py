import streamlit as st
import pandas as pd
from src.recommender import Recommender

# ----------------------------
# Load dataset
# ----------------------------
df = pd.read_csv("data/train.csv", nrows=10000)

st.set_page_config(page_title="Product Recommender", layout="wide")

st.title("🛒 E-Commerce Product Recommendation System")
st.write("Select a product and get similar recommendations")

# ----------------------------
# Build model
# ----------------------------
rec = Recommender(df)
rec.build_model()

# ----------------------------
# Product selection
# ----------------------------
product_list = df['TITLE'].dropna().unique()
selected_product = st.selectbox("Choose a product", product_list)

# ----------------------------
# Recommendation button
# ----------------------------
if st.button("Recommend"):

    st.subheader("Base Product")
    st.write(selected_product)

    st.subheader("Recommended Products")

    results = rec.recommend(selected_product)

    # ----------------------------
    # SAFE OUTPUT HANDLING
    # ----------------------------
    if results is None or results.empty:
        st.warning("No recommendations found 😢")
    else:
        st.dataframe(results)