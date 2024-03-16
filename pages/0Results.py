import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

batch1 = pd.read_csv("batch1.csv")

st.title("Project Result")
st.table(batch1)
# st.data_editor(batch1, hide_index=True, use_container_width=True, disabled=("BATCH", "NAME", "ROLL NUMBER", "P-Desc", "S-Desc", "C-Desc", "CODE", "WORKING" , "TOTAL MARKS"))