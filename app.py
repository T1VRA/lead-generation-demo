import streamlit as st
import pandas as pd
import os

st.title("Lead Generation Dashboard")

df = pd.read_csv("leads.csv")

st.success("CSV loaded successfully")

st.markdown(df.to_html(index=False), unsafe_allow_html=True)
