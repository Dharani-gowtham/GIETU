import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_extras.card import card

def example(key):
    if st.checkbox("Use url", value=True, key=key):
        add_logo("http://placekitten.com/120/120")
    else:
        add_logo("gallery/kitty.jpeg", height=300)
    st.write("👈 Check out the cat in the nav-bar!")

def examplea():
    with st.container():
        card(
            title="",
            text="",
            image="https://yt3.googleusercontent.com/efrVnDJbJOQ5XcXrrFhA9V2wTXh6gP_i0KycoYjqhN3nEh6VbCgqMQakAcFqEsguw7wxhHEjnA=s176-c-k-c0x00ffffff-no-rj",
            url="https://www.google.com",
        )
        st.button("Byte Byte Go")


st.title("Questions for Practice")
example(1)
examplea()

