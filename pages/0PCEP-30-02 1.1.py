import streamlit as st
st.set_page_config(layout="wide")
st.title("PCEP-30-02 1.1 – Understand fundamental terms and definitions")
st.write('The terms "interpreting" and "compiler" both deal with translating code from one form to another, but they work differently and have different advantages and disadvantages. Here\'s a breakdown:')

st.subheader("Interpreting vs. interpreter:")
st.markdown("""
**Interpreting:** The act of understanding and translating the meaning of something, usually from one language to another. In programming, it refers to translating human-readable code into a form the computer can directly understand and execute.

**Interpreter:** A software program that performs interpreting. It reads and executes code line by line, translating each line into machine code on the fly. Examples: Python interpreter, JavaScript interpreter.
    
            """
)
st.subheader("Compiling vs. compiler:")
st.markdown("""

**Compiling:** The act of translating code from a high-level programming language into a lower-level language, typically machine code specific to the target computer architecture. This translation happens all at once before the program runs.

**Compiler:** A software program that performs compiling. It analyzes the entire source code and generates a standalone executable file in machine code. Examples: C++ compiler, Java compiler.

            """
)