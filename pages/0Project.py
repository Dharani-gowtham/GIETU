import streamlit as st

st.title("Project - DeadLine (19 Mar 2024)")
st.caption(" `Games` `Pre-build Program` `Github Repo` are not allowed")
st.subheader("Marks Allocated: Pass percentage: 60")
data = {
    "Problem Statement Description": "2",
    "Problem Solution Description": "2",
    "Steps to Achieve that Solution": "6",
    "Code": "3",
    "Working": "7",
    "Total": "20"
        }

st.data_editor(data, use_container_width=True)
st.subheader("Tech Stack that can be used")
col1, col2, col3 = st.columns([1,1,1])


with col1:
    st.subheader("Front-end Frameworks")
    st.checkbox("Streamlit", value=True, disabled=True)
    st.checkbox("React", value=True, disabled=True)
    st.checkbox("Tkinter", value=True, disabled=True)
    
with col2:
    st.subheader("Back-end Frameworks")
    st.checkbox("Flask", value=True, disabled=True)
    st.checkbox("Django", value=True, disabled=True)
    st.checkbox("Fast API", value=True, disabled=True)

with col3:
    st.subheader("Database Frameworks")
    st.checkbox("MongoDB", value=True, disabled=True)
    st.checkbox("MySQL", value=True, disabled=True)
    st.checkbox("SQlite", value=True, disabled=True)