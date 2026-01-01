import streamlit as st

def show_cleaning(numeric_data, data):
    na_strategy = st.selectbox(
        "Missing value strategy",
        ["Do nothing", "Drop rows", "Fill numeric with mean", "Fill numeric with median"]
    )

    if na_strategy == "Drop rows":
        data = data.dropna()

    elif na_strategy == "Fill numeric with mean":
        for col in numeric_data:
            data[col] = data[col].fillna(data[col].mean())

    elif na_strategy == "Fill numeric with median":
        for col in numeric_data:
            data[col] = data[col].fillna(data[col].median())


