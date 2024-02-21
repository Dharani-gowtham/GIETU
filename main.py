import streamlit as st
import subprocess
st.set_page_config(layout="wide")

value ="""
def function():
    # write your code here
"""

st.title("Python Basics, OOPS & Data Structures")
st.code("Github URL: https://github.com/Dharani-gowtham/GIETU")

col1, col2 = st.columns([1,1])

with col1:
    st.subheader("Col 1")
    
with col2:
    st.subheader("Reference Links")
    with st.container(height=300):
        st.markdown("""<iframe width="100%" height="250" src="https://www.youtube.com/embed/nr8biZfSZ3Y" title="I coded one project EVERY WEEK for a YEAR" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        """,unsafe_allow_html=True)
    
    st.markdown("""<iframe width="100%" height="300" src="https://www.youtube.com/embed/nr8biZfSZ3Y" title="I coded one project EVERY WEEK for a YEAR" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        """,unsafe_allow_html=True)
    
    st.divider()
    st.subheader("YouTube Channels")
    st.link_button("ByteByte GO",url="https://www.youtube.com/@ByteByteGo")
    
editor, result = st.columns([4,2])

text_code = st.text_area(label="Code Editor", height=500,label_visibility="collapsed", value=value)

if st.button("Run", use_container_width=True):
    file_name = "student_code.py"
    with open(file_name,'w') as file:
        file.write(text_code)
    
    command = f"python {file_name}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    st.text(result.stdout)
    if result.returncode != 0:
        st.code(f"Error: {result.stderr}")
    
    if result.returncode == 0:
        st.success(f"Executed Successfully")
