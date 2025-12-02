import streamlit as st
import pandas as pd

st.set_page_config(page_title="Employee Retention & Satisfaction Dashboard", layout="wide")

st.title("Employee Retention & Satisfaction Analysis")

uploaded_file = st.file_uploader("Upload HR Dataset", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset Loaded Successfully!")
    
    st.subheader("Preview of Data")
    st.dataframe(df.head())

    st.subheader("Basic Statistics")
    st.write(df.describe())

    st.subheader("Attrition Count")
    st.bar_chart(df["Attrition"].value_counts())

    if "JobSatisfaction" in df.columns:
        st.subheader("Job Satisfaction Distribution")
        st.bar_chart(df["JobSatisfaction"].value_counts())

    if "MonthlyIncome" in df.columns:
        st.subheader("Monthly Income Distribution")
        st.line_chart(df["MonthlyIncome"])

st.info("Upload your preprocessed HR dataset to begin analysis.")
