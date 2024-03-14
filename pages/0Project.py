import streamlit as st

st.title("Project")
data = {
    "Problem Statement Description": "2",
    "Problem Solution Description": "2",
    "Steps to Achieve that Solution": "6",
    "Code": "3",
    "Working": "7"
        }

st.data_editor(data, use_container_width=True)