import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

batch1 = pd.read_csv("batch1.csv")

st.title("Project Result")
st.data_editor(batch1, hide_index=True, use_container_width=True)