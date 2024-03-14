import streamlit as st

st.title("Project")
st.subheader("Marks Allocated")
data = {
    "Problem Statement Description": "2",
    "Problem Solution Description": "2",
    "Steps to Achieve that Solution": "6",
    "Code": "3",
    "Working": "7"
        }

st.data_editor(data, use_container_width=True)

st.subheader("Tech Stack that can be used")
st.checkbox("Flask", value=True, disabled=True)
st.checkbox("Django", value=True, disabled=True)
st.checkbox("Fast API", value=True, disabled=True)
st.checkbox("Streamlit", value=True, disabled=True)
st.checkbox("React", value=True, disabled=True)
st.checkbox("Tkinter", value=True, disabled=True)