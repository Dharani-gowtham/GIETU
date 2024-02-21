import streamlit as st


def wid(data):
    with st.expander(f"Question {data}"):
        col1, col2 = st.columns([1,1])
        with col1:
            st.subheader("Hello")
        
        with col2:
            st.subheader("Col2")
        
for i in range(1, 11):
    wid(i)
    