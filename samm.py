import streamlit as st


class component:
    def highlight(self):
        st.success(f"Button Pressed from{self.text}")
        
    def __init__(self, text):
        self.text = text
        st.button(f"{self.text} button", on_click=self.highlight)
        
    

for i in range(10):        
    component(i)