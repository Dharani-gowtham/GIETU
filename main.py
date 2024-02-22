import streamlit as st
import subprocess
st.set_page_config(layout="wide")

value ="""
def function():
    # write your code here
"""

st.title("Python Basics, OOPS & Data Structures")
st.code("Github URL: https://github.com/Dharani-gowtham/GIETU")

# col1, col2 = st.columns([1,1])

# with col1:
#     st.subheader("Col 1")
    
# with col2:
#     st.subheader("Reference Links")
    
#     st.markdown("""<iframe width="100%" height="300" src="https://www.youtube.com/embed/nr8biZfSZ3Y" title="I coded one project EVERY WEEK for a YEAR" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
#         """,unsafe_allow_html=True)
    
#     st.divider()
#     st.subheader("YouTube Channels")
#     st.link_button("ByteByte GO",url="https://www.youtube.com/@ByteByteGo")
    
# editor, result = st.columns([4,2])

# text_code = st.text_area(label="Code Editor", height=500,label_visibility="collapsed", value=value)

# if st.button("Run", use_container_width=True):
#     file_name = "student_code.py"
#     with open(file_name,'w') as file:
#         file.write(text_code)
    
#     command = f"python {file_name}"
#     result = subprocess.run(command, shell=True, capture_output=True, text=True)
#     st.text(result.stdout)
#     if result.returncode != 0:
#         st.code(f"Error: {result.stderr}")
#     else:
#         st.code(result)
#         st.code(result.stdout)
    
#     if result.returncode == 0:
#         st.success(f"Executed Successfully")


st.title("Python Questions for Practice")

st.subheader("Week 1: Python Basics")
with st.expander("Input/Output"):
    st.write("""
             1. Basic Input: Write a program that asks the user for their name and age, then prints a greeting message including their name.\n
2. Number Input: Create a program that reads two numbers from the user and calculates their sum and average, displaying the results.
3. Formatted Output: Write a program that calculates the area of a circle and displays the result with two decimal places using string formatting.
4. User Choice: Implement a menu with options like "print hello" and "calculate area". Let the user choose the option and execute the corresponding function.
5. File Input/Output: Write a program that reads numbers from a text file and calculates their statistics (mean, median, etc.). Write the results to another file.
Variations: Explore advanced input/output methods like using command-line arguments, reading binary data, and using custom error handling.
             """)
with st.expander("Questions using Data Types in Python:"):
    st.write("1. **Data Type Detective:** Write a function identify_type(data) that takes any data as input and returns its data type (e.g., int, float, str, list, etc.) using the type() function. Can you expand it to handle more complex data types like dictionaries or sets?")
    
    st.write("2. **Number Crunching:** Create a program that reads a list of numbers (integers and floats) from the user and calculates the sum, average, minimum, and maximum values. Use appropriate data types for storing and manipulating the numbers.")
    
    st.write("3. **String Manipulation:** Write a function reverse_words(sentence) that takes a string as input and returns a new string with the words reversed while preserving the original order of words. Remember to account for punctuation and spaces.")
    
    st.write("4. **List Comprehensions:** Create a list containing the squares of all even numbers from 1 to 20 using list comprehensions. Explore different ways to achieve the same result with loops and conditional statements.")
    
    st.write("5. **Dictionary Deep Dive:** Write a program that reads a dictionary containing student names and their grades. Calculate the average grade for each subject and display the top 3 students with the highest overall average. Leverage dictionary methods effectively.")
    
    st.write("6. **Tuple Challenge:** Define a tuple containing different data types (int, float, string). Write functions to access specific elements by index, iterate through the entire tuple, and check if a specific value exists within it.")
    
    st.write("7. **Set Operations:** Create two sets containing unique words from two different text files. Perform set operations like union, intersection, and difference to identify common and distinct words between the files.")
    
    st.write("8. **Boolean Logic:** Write a program that simulates a simple quiz with multiple choice questions. Store questions and answers in appropriate data structures and use boolean expressions to evaluate user responses and calculate the score.")
    
    st.write("9. **Data Type Conversions:** Create a program that prompts the user for a string representing a number. Convert the string to an appropriate numeric data type (int or float) and perform basic arithmetic operations based on user input (+, -, *, /). Handle potential errors gracefully.")
    
    st.write("10. **Data Type Mystery:** Write a program that defines a variable with a value but doesn't reveal its data type. Challenge the user to guess the data type by performing various operations and observations (e.g., printing, checking length, using methods).")
with st.expander("Questions using arithmetic operators"):
    st.write("")

st.subheader("Week 2: Functions and Control Flow")
with st.expander("1. Inroduction to Python, Installation"):
    st.write("kjb")
    
st.subheader("Week 3: Lists and Tuples")
with st.expander("1. Inroduction to Python, Installation"):
    st.write("kjb")
    
st.subheader("Week 4: Dictionaries and Sets")
with st.expander("1. Inroduction to Python, Installation"):
    st.write("kjb")

st.subheader("Week 5: File Handling and Exception Handling")
with st.expander("1. Inroduction to Python, Installation"):
    st.write("kjb")

st.subheader("Week 6: Object-Oriented Programming and Advanced Data Structures")
with st.expander("1. Inroduction to Python, Installation"):
    st.write("kjb")
    
st.subheader("Week 7: Practice Questions and Projects")
with st.expander("1. Inroduction to Python, Installation"):
    st.write("kjb")
st.write("""
         Week 1: Python Basics
- Day 1: Introduction to Python, Installation
- Day 2: Basic Syntax and Data Types
- Day 3: Variables and Operators
- Day 4: Input and Output
- Day 5: Review and Practice
- Day 6: Control Flow Statements (Part 1)
- Day 7: Control Flow Statements (Part 2)

Week 2: Functions and Control Flow
- Day 8: Functions (Part 1)
- Day 9: Functions (Part 2)
- Day 10: Function Arguments and Return Values
- Day 11: Scope and Global Variables
- Day 12: Review and Practice
- Day 13: Lists (Part 1)
- Day 14: Lists (Part 2)

Week 3: Lists and Tuples
- Day 15: List Methods and Operations
- Day 16: List Slicing and Manipulation
- Day 17: Tuples (Part 1)
- Day 18: Tuples (Part 2)
- Day 19: Review and Practice
- Day 20: Dictionaries (Part 1)
- Day 21: Dictionaries (Part 2)

Week 4: Dictionaries and Sets
- Day 22: Dictionary Methods and Operations
- Day 23: Dictionary Comprehension
- Day 24: Sets (Part 1)
- Day 25: Sets (Part 2)
- Day 26: Review and Practice
- Day 27: File Handling (Part 1)
- Day 28: File Handling (Part 2)

Week 5: File Handling and Exception Handling
- Day 29: Reading and Writing Text Files
- Day 30: Handling CSV and JSON Files
- Day 31: Exception Handling (Part 1)
- Day 32: Exception Handling (Part 2)
- Day 33: Review and Practice
- Day 34: Object-Oriented Programming (OOP) Basics (Part 1)
- Day 35: OOP Basics (Part 2)

Week 6: Object-Oriented Programming and Advanced Data Structures
- Day 36: Classes and Objects
- Day 37: Attributes and Methods
- Day 38: Inheritance and Polymorphism
- Day 39: Review and Practice
- Day 40: Stacks and Queues
- Day 41: Linked Lists
- Day 42: Trees (Part 1)
- Day 43: Trees (Part 2)
- Day 44: Review and Practice

Week 7: Practice Questions and Projects
- Day 45: Practice Questions on Advanced Data Structures
- Day 46-52: Work on Mini-Projects and Coding Exercises
         
         """)