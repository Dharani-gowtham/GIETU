import streamlit as st
st.title("PCEP-30-02 1.2 – Understand Python’s logic and structure")
st.subheader("Keywords")
st.markdown("""
            As of Python 3.12, there are 35 keywords in the language. Here's the complete list:

False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

These keywords have special meanings within Python and cannot be used as variable names, function names, or other identifiers. It's important to familiarize yourself with this list to avoid conflicts and write valid Python code.

Additional notes:

    Some keywords were introduced in later versions of Python, so the exact list may differ depending on the version you're using.
    The keyword module provides functions to check if a string is a keyword or soft keyword.

I hope this helps! Let me know if you have any other questions.
            """)

st.subheader("Instructions")
st.markdown("""
            Instructions in Python, essentially lines of code, can be understood through three key aspects:

1. Lexis:

    Building blocks: Individual elements like characters, keywords (e.g., def, for), identifiers (e.g., variable names), operators (e.g., +, =, ==), numbers, strings.
    Analogy: Words and punctuation in a sentence.
    Example: x = 5 + 2 * 3 contains characters, keywords (x, =, +, *), identifier (x), numbers (5, 2, 3).

2. Syntax:

    Rules: Governs how lexicals are arranged to form valid code structures.
    Analogy: Sentence structure and grammar.
    Example: def my_function(x): follows the function definition syntax (keyword def, function name, parameter in parentheses, colon).

3. Semantics:

    Meaning: What the code does when executed, given valid syntax.
    Analogy: Meaning conveyed by the sentence.
    Example: The previous example defines a function called my_function that takes one argument named x.

To summarize, instructions in Python are like sentences:

    Lexis are the individual words and punctuation.
    Syntax is the grammar that dictates how these words are put together.
    Semantics is the overall meaning conveyed by the sentence (what the code does).

Here are some additional points about instructions in Python:

    Line-based language: Each line typically represents a single instruction.
    Indentation matters: Python uses indentation (spaces) to define code blocks, not curly braces.
    Whitespace ignored: Spaces and tabs are generally ignored unless they affect indentation.
    Multiple ways to achieve the same outcome: Different syntactic forms can sometimes achieve the same functionality.

Understanding these aspects will help you write readable, correct, and effective Python code.
            
            """)