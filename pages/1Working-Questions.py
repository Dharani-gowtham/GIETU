import streamlit as st

st.subheader("http://172.44.1.61:8501" )
st.subheader("https://gietuniversity.streamlit.app/Working-Questions")



st.markdown("""

FOR LOOP:


Certainly! Here are five situation-based Python programming questions along with two test cases for each:

**Question 1: Multiplication Table**

**Description:**
Write a Python program to generate the multiplication table for a given number. Implement a `for` loop to display the table up to a specified range.

**Instructions:**
1. Take an integer input, `number`, for which the multiplication table needs to be generated.
2. Take another integer input, `range_limit`, representing the range up to which the table should be displayed.
3. Implement a `for` loop to print the multiplication table.

**Test Cases:**

Test Case 1:
```python
Input:
number = 5
range_limit = 3

Output:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
```

Test Case 2:
```python
Input:
number = 8
range_limit = 4

Output:
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
```

**Question 2: Password Validation**

**Description:**
Create a Python program to validate passwords based on certain criteria. Implement a `for` loop to check each character of the password.

**Instructions:**
1. Take a string input, `password`, representing the password to be validated.
2. Check if the password contains at least one uppercase letter, one lowercase letter, and one digit.
3. Print whether the password is valid or not.

**Test Cases:**

Test Case 1:
```python
Input:
password = "SecureP@ss1"

Output:
Password is valid
```

Test Case 2:
```python
Input:
password = "WeakPassword"

Output:
Password is not valid
```

**Question 3: Fibonacci Series**

**Description:**
Write a Python program to generate the Fibonacci series up to a specified number of terms using a `for` loop.

**Instructions:**
1. Take an integer input, `terms`, representing the number of terms in the Fibonacci series.
2. Implement a `for` loop to calculate and print the Fibonacci series.

**Test Cases:**

Test Case 1:
```python
Input:
terms = 5

Output:
Fibonacci Series: 0, 1, 1, 2, 3
```

Test Case 2:
```python
Input:
terms = 8

Output:
Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13
```

**Question 4: Temperature Conversion**

**Description:**
Create a Python program to convert temperatures from Celsius to Fahrenheit using a `for` loop.

**Instructions:**
1. Take a list input, `celsius_temps`, containing temperatures in Celsius.
2. Implement a `for` loop to convert each temperature to Fahrenheit using the formula: `F = (C * 9/5) + 32`.
3. Print the converted temperatures.

**Test Cases:**

Test Case 1:
```python
Input:
celsius_temps = [0, 25, 100]

Output:
Converted Temperatures: [32.0, 77.0, 212.0]
```

Test Case 2:
```python
Input:
celsius_temps = [-10, 0, 20]

Output:
Converted Temperatures: [14.0, 32.0, 68.0]
```

**Question 5: Counting Vowels**

**Description:**
Write a Python program to count the number of vowels in a given string using a `for` loop.

**Instructions:**
1. Take a string input, `input_string`, containing alphabets.
2. Implement a `for` loop to iterate through each character and count the number of vowels (consider both uppercase and lowercase).
3. Print the total count of vowels.

**Test Cases:**

Test Case 1:
```python
Input:
input_string = "Hello World"

Output:
Total vowels: 3
```

Test Case 2:
```python
Input:
input_string = "Programming is Fun"

Output:
Total vowels: 6
```

Question 6:

**Title: Grocery Shopping List**

**Description:**

Imagine you are creating a program to help someone manage their grocery shopping list. Write a Python program that takes a list of grocery items and their corresponding prices. Implement a `for` loop to calculate and display the total cost of the items in the list.

**Instructions:**

1. Create a list of tuples, where each tuple contains the name of a grocery item and its price (e.g., `('apple', 2.50)`).
2. Implement a `for` loop to iterate through the list and calculate the total cost.
3. Print the total cost of all the items.

**Example:**

```python
grocery_list = [('apple', 2.50), ('banana', 1.50), ('bread', 3.00)]

Output:
The total cost of the groceries is $7.00
```

**Test Cases:**

Test Case 1:
```python
grocery_list = [('milk', 1.75), ('eggs', 2.00), ('cheese', 4.50)]

Output:
The total cost of the groceries is $8.25
```

Test Case 2:
```python
grocery_list = [('tomatoes', 1.20), ('onions', 0.75), ('potatoes', 2.50)]

Output:
The total cost of the groceries is $4.45
```





IF ELSE

Certainly! Here are five situation-based Python programming questions involving `if-else` statements, along with two test cases for each:

**Question 1: Grade Classification**

**Description:**
Write a Python program to classify student grades based on their marks. Implement `if-else` statements to determine the grade.

**Instructions:**
1. Take an integer input, `marks`, representing the student's score.
2. Classify the grade as 'A' for marks above 90, 'B' for marks between 80 and 90, 'C' for marks between 70 and 80, and 'D' for marks below 70.
3. Print the grade.

**Test Cases:**

Test Case 1:
```python
Input:
marks = 95

Output:
Grade: A
```

Test Case 2:
```python
Input:
marks = 78

Output:
Grade: C
```

**Question 2: Leap Year Check**

**Description:**
Create a Python program to check if a given year is a leap year or not. Use `if-else` statements to make the determination.

**Instructions:**
1. Take an integer input, `year`, representing the year to be checked.
2. Check if the year is a leap year. A leap year is divisible by 4, except for years that are divisible by 100 but not by 400.
3. Print whether the year is a leap year or not.

**Test Cases:**

Test Case 1:
```python
Input:
year = 2020

Output:
2020 is a leap year
```

Test Case 2:
```python
Input:
year = 2100

Output:
2100 is not a leap year
```

**Question 3: Number Comparison**

**Description:**
Write a Python program to compare two numbers and print whether they are equal, greater, or smaller. Use `if-else` statements for the comparison.

**Instructions:**
1. Take two integer inputs, `num1` and `num2`.
2. Compare the numbers and print whether they are equal, greater, or smaller.

**Test Cases:**

Test Case 1:
```python
Input:
num1 = 8
num2 = 5

Output:
8 is greater than 5
```

Test Case 2:
```python
Input:
num1 = 12
num2 = 12

Output:
12 is equal to 12
```

**Question 4: Positive/Negative/Zero Check**

**Description:**
Create a Python program to check if a given number is positive, negative, or zero. Utilize `if-else` statements for the check.

**Instructions:**
1. Take an integer input, `number`.
2. Check if the number is positive, negative, or zero.
3. Print the result.

**Test Cases:**

Test Case 1:
```python
Input:
number = -7

Output:
-7 is a negative number
```

Test Case 2:
```python
Input:
number = 0

Output:
0 is neither positive nor negative
```

**Question 5: Odd/Even Number Check**

**Description:**
Write a Python program to determine if a given number is odd or even. Use `if-else` statements for the check.

**Instructions:**
1. Take an integer input, `num`.
2. Check if the number is odd or even.
3. Print the result.

**Test Cases:**

Test Case 1:
```python
Input:
num = 9

Output:
9 is an odd number
```

Test Case 2:
```python
Input:
num = 14

Output:
14 is an even number
```



IF ELIF ELSE

In Python, there is no direct `switch` statement as in some other programming languages like C or Java. However, I can provide you with alternative scenarios where you might implement a similar functionality using `if-elif-else` constructs.

**Question 1: Day of the Week**

**Description:**
Write a Python program to determine the day of the week based on a given number (1 for Monday, 2 for Tuesday, etc.). Implement a function or conditional statements to achieve this.

**Instructions:**
1. Take an integer input, `day_number`, representing the day of the week.
2. Determine the corresponding day and print it.

**Test Cases:**

Test Case 1:
```python
Input:
day_number = 3

Output:
Wednesday
```

Test Case 2:
```python
Input:
day_number = 6

Output:
Saturday
```

**Question 2: Menu Selection**

**Description:**
Create a Python program to simulate a menu-driven system. Implement a function or conditional statements to execute different actions based on the user's selection.

**Instructions:**
1. Take an integer input, `menu_choice`, representing the user's selection from a menu (e.g., 1 for option A, 2 for option B, etc.).
2. Perform the corresponding action based on the user's choice.

**Test Cases:**

Test Case 1:
```python
Input:
menu_choice = 2

Output:
Executing Option B
```

Test Case 2:
```python
Input:
menu_choice = 4

Output:
Invalid choice. Please select a valid option.
```

**Question 3: Calculator Operations**

**Description:**
Write a Python program to create a basic calculator that can perform addition, subtraction, multiplication, and division. Implement a function or conditional statements to execute the desired operation.

**Instructions:**
1. Take two numbers as input, `num1` and `num2`.
2. Take an integer input, `operation_choice`, representing the operation to be performed (1 for addition, 2 for subtraction, etc.).
3. Perform the selected operation and print the result.

**Test Cases:**

Test Case 1:
```python
Input:
num1 = 10
num2 = 5
operation_choice = 3

Output:
Result: 50
```

Test Case 2:
```python
Input:
num1 = 8
num2 = 2
operation_choice = 5

Output:
Invalid choice. Please select a valid operation.
```

**Question 4: Ticket Price Calculation**

**Description:**
Create a Python program to calculate the price of a movie ticket based on different criteria such as age and day of the week. Implement a function or conditional statements for the calculation.

**Instructions:**
1. Take an integer input, `age`, representing the age of the person.
2. Take an integer input, `day`, representing the day of the week (1 for Monday, 2 for Tuesday, etc.).
3. Calculate the ticket price based on age and day, and print the result.

**Test Cases:**

Test Case 1:
```python
Input:
age = 22
day = 3

Output:
Ticket Price: $10
```

Test Case 2:
```python
Input:
age = 15
day = 7

Output:
Ticket Price: $8
```

**Question 5: Season Determination**

**Description:**
Write a Python program to determine the season based on the month number. Implement a function or conditional statements for this purpose.

**Instructions:**
1. Take an integer input, `month`, representing the month of the year.
2. Determine the corresponding season (e.g., 1-3 for winter, 4-6 for spring, etc.) and print it.

**Test Cases:**

Test Case 1:
```python
Input:
month = 8

Output:
Summer
```

Test Case 2:
```python
Input:
month = 12

Output:
Winter
```



WHILE LOOP


Certainly! Here are five situation-based Python programming questions involving `while` loops, along with two test cases for each:

**Question 1: Guess the Number**

**Description:**
Write a Python program that generates a random number and asks the user to guess it. Use a `while` loop to continue prompting the user until they guess correctly.

**Instructions:**
1. Generate a random number between 1 and 100.
2. Prompt the user to guess the number.
3. Use a `while` loop to continue prompting until the user guesses correctly.
4. Print a congratulatory message after the correct guess.

**Test Cases:**

Test Case 1:
```python
Random Number: 75

User Input:
Guess the number: 50
Guess the number: 80
Guess the number: 75

Output:
Congratulations! You guessed the correct number.
```

Test Case 2:
```python
Random Number: 38

User Input:
Guess the number: 45
Guess the number: 30
Guess the number: 38

Output:
Congratulations! You guessed the correct number.
```

**Question 2: Factorial Calculation**

**Description:**
Write a Python program to calculate the factorial of a given number using a `while` loop.

**Instructions:**
1. Take an integer input, `num`.
2. Calculate and print the factorial of `num` using a `while` loop.

**Test Cases:**

Test Case 1:
```python
Input:
num = 5

Output:
The factorial of 5 is 120
```

Test Case 2:
```python
Input:
num = 8

Output:
The factorial of 8 is 40320
```

**Question 3: Password Validation**

**Description:**
Create a Python program that asks the user to enter a password and keeps prompting until a valid password is provided. Use a `while` loop for this validation.

**Instructions:**
1. Prompt the user to enter a password.
2. Use a `while` loop to check if the password meets certain criteria (e.g., length, complexity).
3. Keep prompting until a valid password is provided.

**Test Cases:**

Test Case 1:
```python
User Input:
Enter a password: weak
Enter a password: Strong123

Output:
Password accepted!
```

Test Case 2:
```python
User Input:
Enter a password: abc
Enter a password: 123456
Enter a password: SecureP@ss

Output:
Password accepted!
```

**Question 4: Sum of Digits**

**Description:**
Write a Python program to calculate the sum of digits of a given number using a `while` loop.

**Instructions:**
1. Take an integer input, `number`.
2. Calculate and print the sum of the digits of `number` using a `while` loop.

**Test Cases:**

Test Case 1:
```python
Input:
number = 123

Output:
The sum of digits in 123 is 6
```

Test Case 2:
```python
Input:
number = 9876

Output:
The sum of digits in 9876 is 30
```

**Question 5: Reverse a String**

**Description:**
Create a Python program to reverse a given string using a `while` loop.

**Instructions:**
1. Take a string input, `input_string`.
2. Use a `while` loop to reverse the string.
3. Print the reversed string.

**Test Cases:**

Test Case 1:
```python
Input:
input_string = "Python"

Output:
The reversed string is nohtyP
```

Test Case 2:
```python
Input:
input_string = "Hello World"

Output:
The reversed string is dlroW olleH
```



FUNCTIONS :


Certainly! Here are 10 situation-based Python programming questions involving functions, along with two test cases for each:

**Question 1: Sum of Two Numbers**

**Description:**
Write a Python program with a function that takes two parameters and returns their sum.

**Function Signature:**
```python
def add_numbers(a, b):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
add_numbers(3, 5)

Output:
8
```

Test Case 2:
```python
Input:
add_numbers(-2, 7)

Output:
5
```

**Question 2: Factorial Calculation**

**Description:**
Write a Python program with a function that calculates the factorial of a given number.

**Function Signature:**
```python
def calculate_factorial(num):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
calculate_factorial(5)

Output:
120
```

Test Case 2:
```python
Input:
calculate_factorial(8)

Output:
40320
```

**Question 3: Check Even or Odd**

**Description:**
Create a Python program with a function that checks whether a given number is even or odd.

**Function Signature:**
```python
def check_even_odd(num):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
check_even_odd(7)

Output:
Odd
```

Test Case 2:
```python
Input:
check_even_odd(14)

Output:
Even
```

**Question 4: Simple Interest Calculation**

**Description:**
Write a Python program with a function that calculates the simple interest.

**Function Signature:**
```python
def calculate_simple_interest(principal, rate, time):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
calculate_simple_interest(1000, 0.05, 2)

Output:
100.0
```

Test Case 2:
```python
Input:
calculate_simple_interest(5000, 0.08, 3)

Output:
1200.0
```

**Question 5: String Reversal**

**Description:**
Create a Python program with a function that reverses a given string.

**Function Signature:**
```python
def reverse_string(input_string):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
reverse_string("Python")

Output:
"nohtyP"
```

Test Case 2:
```python
Input:
reverse_string("Hello World")

Output:
"dlroW olleH"
```

**Question 6: List Summation**

**Description:**
Write a Python program with a function that calculates the sum of elements in a given list.

**Function Signature:**
```python
def calculate_list_sum(nums):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
calculate_list_sum([1, 2, 3, 4, 5])

Output:
15
```

Test Case 2:
```python
Input:
calculate_list_sum([-2, 5, 8, -1, 3])

Output:
13
```

**Question 7: Vowel Count**

**Description:**
Create a Python program with a function that counts the number of vowels in a given string.

**Function Signature:**
```python
def count_vowels(input_string):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
count_vowels("Hello World")

Output:
3
```

Test Case 2:
```python
Input:
count_vowels("Programming is Fun")

Output:
6
```

**Question 8: Power Calculation**

**Description:**
Write a Python program with a function that calculates the power of a number.

**Function Signature:**
```python
def calculate_power(base, exponent):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
calculate_power(2, 3)

Output:
8
```

Test Case 2:
```python
Input:
calculate_power(5, 2)

Output:
25
```

**Question 9: Maximum of Three Numbers**

**Description:**
Create a Python program with a function that finds the maximum of three given numbers.

**Function Signature:**
```python
def find_maximum(num1, num2, num3):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
find_maximum(7, 12, 5)

Output:
12
```

Test Case 2:
```python
Input:
find_maximum(10, 3, 8)

Output:
10
```

**Question 10: Palindrome Check**

**Description:**
Write a Python program with a function that checks whether a given string is a palindrome.

**Function Signature:**
```python
def is_palindrome(input_string):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
is_palindrome("radar")

Output:
True
```

Test Case 2:
```python
Input:
is_palindrome("python")

Output:
False
```

Certainly! Here are another 10 Python programming questions involving functions, along with two test cases for each:

**Question 11: Prime Number Check**

**Description:**
Create a Python program with a function that checks whether a given number is prime.

**Function Signature:**
```python
def is_prime(number):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
is_prime(17)

Output:
True
```

Test Case 2:
```python
Input:
is_prime(25)

Output:
False
```

**Question 12: Fibonacci Series**

**Description:**
Write a Python program with a function that generates the Fibonacci series up to a specified number of terms.

**Function Signature:**
```python
def generate_fibonacci(terms):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
generate_fibonacci(5)

Output:
[0, 1, 1, 2, 3]
```

Test Case 2:
```python
Input:
generate_fibonacci(8)

Output:
[0, 1, 1, 2, 3, 5, 8, 13]
```

**Question 13: Unique Elements in a List**

**Description:**
Create a Python program with a function that returns a list containing only unique elements from a given list.

**Function Signature:**
```python
def get_unique_elements(input_list):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
get_unique_elements([1, 2, 2, 3, 4, 4, 5])

Output:
[1, 2, 3, 4, 5]
```

Test Case 2:
```python
Input:
get_unique_elements(['apple', 'banana', 'apple', 'orange'])

Output:
['apple', 'banana', 'orange']
```

**Question 14: Reverse Words in a String**

**Description:**
Write a Python program with a function that reverses the order of words in a given string.

**Function Signature:**
```python
def reverse_words(input_string):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
reverse_words("Hello World")

Output:
"World Hello"
```

Test Case 2:
```python
Input:
reverse_words("Python is amazing")

Output:
"amazing is Python"
```

**Question 15: List Filtering**

**Description:**
Create a Python program with a function that filters out numbers greater than a specified value from a given list.

**Function Signature:**
```python
def filter_numbers(input_list, threshold):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
filter_numbers([10, 15, 8, 25, 30], 20)

Output:
[10, 15, 8]
```

Test Case 2:
```python
Input:
filter_numbers([-5, 0, 12, -3, 7], 5)

Output:
[-5, 0, -3]
```

**Question 16: Celsius to Fahrenheit Conversion**

**Description:**
Write a Python program with a function that converts temperatures from Celsius to Fahrenheit.

**Function Signature:**
```python
def celsius_to_fahrenheit(celsius):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
celsius_to_fahrenheit(25)

Output:
77.0
```

Test Case 2:
```python
Input:
celsius_to_fahrenheit(-10)

Output:
14.0
```

**Question 17: Binary to Decimal Conversion**

**Description:**
Create a Python program with a function that converts a binary number to its decimal equivalent.

**Function Signature:**
```python
def binary_to_decimal(binary_num):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
binary_to_decimal('1101')

Output:
13
```

Test Case 2:
```python
Input:
binary_to_decimal('10101')

Output:
21
```

**Question 18: Matrix Transposition**

**Description:**
Write a Python program with a function that transposes a given matrix.

**Function Signature:**
```python
def transpose_matrix(matrix):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
transpose_matrix([[1, 2, 3], [4, 5, 6]])

Output:
[[1, 4], [2, 5], [3, 6]]
```

Test Case 2:
```python
Input:
transpose_matrix([[7, 8], [9, 10], [11, 12]])

Output:
[[7, 9, 11], [8, 10, 12]]
```

**Question 19: Check for Anagrams**

**Description:**
Create a Python program with a function that checks whether two given strings are anagrams.

**Function Signature:**
```python
def are_anagrams(str1, str2):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
are_anagrams("listen", "silent")

Output:
True
```

Test Case 2:
```python
Input:
are_anagrams("python", "java")

Output:
False
```

**Question 20: Password Generator**

**Description:**
Write a Python program with a function that generates a random password of a specified length.

**Function Signature:**
```python
def generate_password(length):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
generate_password(8)

Output:
Randomly generated password (example): "5gY9pR2q"
```

Test Case 2:
```python
Input:
generate_password(12)

Output:
Randomly generated password (example): "a3BcD8eF1gH"
```


Certainly! Here are 10 situation-based Python programming questions involving function arguments and return values, along with two test cases for each:

**Question 1: Average of Numbers**

**Description:**
Write a Python program with a function that calculates the average of a list of numbers.

**Function Signature:**
```python
def calculate_average(numbers):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
calculate_average([3, 6, 9, 12, 15])

Output:
9.0
```

Test Case 2:
```python
Input:
calculate_average([1, 2, 3, 4, 5])

Output:
3.0
```

**Question 2: Largest Element in a List**

**Description:**
Create a Python program with a function that finds the largest element in a given list.

**Function Signature:**
```python
def find_largest_element(lst):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
find_largest_element([7, 15, 3, 22, 10])

Output:
22
```

Test Case 2:
```python
Input:
find_largest_element([-2, 0, 5, -1, 3])

Output:
5
```

**Question 3: Factorial with Default Value**

**Description:**
Write a Python program with a function that calculates the factorial of a given number. The function should have a default value of 1.

**Function Signature:**
```python
def calculate_factorial(num=1):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
calculate_factorial(5)

Output:
120
```

Test Case 2:
```python
Input:
calculate_factorial()

Output:
1
```

**Question 4: String Concatenation**

**Description:**
Create a Python program with a function that concatenates two strings and returns the result.

**Function Signature:**
```python
def concatenate_strings(str1, str2):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
concatenate_strings("Hello", "World")

Output:
"HelloWorld"
```

Test Case 2:
```python
Input:
concatenate_strings("Python", "Programming")

Output:
"PythonProgramming"
```

**Question 5: Power Calculation with Exponentiation**

**Description:**
Write a Python program with a function that calculates the power of a number using exponentiation.

**Function Signature:**
```python
def calculate_power(base, exponent):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
calculate_power(2, 3)

Output:
8
```

Test Case 2:
```python
Input:
calculate_power(5, 2)

Output:
25
```

**Question 6: List Filtering with Threshold**

**Description:**
Create a Python program with a function that filters out numbers greater than a specified threshold from a given list.

**Function Signature:**
```python
def filter_numbers(input_list, threshold):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
filter_numbers([10, 15, 8, 25, 30], 20)

Output:
[10, 15, 8]
```

Test Case 2:
```python
Input:
filter_numbers([-5, 0, 12, -3, 7], 5)

Output:
[-5, 0, -3]
```

**Question 7: Matrix Multiplication**

**Description:**
Write a Python program with a function that multiplies two matrices and returns the result.

**Function Signature:**
```python
def matrix_multiplication(matrix1, matrix2):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
matrix_multiplication([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])

Output:
[[58, 64], [139, 154]]
```

Test Case 2:
```python
Input:
matrix_multiplication([[2, 3], [5, 4]], [[1, 2], [7, 8]])

Output:
[[23, 28], [27, 34]]
```

**Question 8: Palindrome Check with Case Sensitivity**

**Description:**
Create a Python program with a function that checks whether a given string is a palindrome, considering case sensitivity.

**Function Signature:**
```python
def is_palindrome(input_string):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
is_palindrome("radar")

Output:
True
```

Test Case 2:
```python
Input:
is_palindrome("Python")

Output:
False
```

**Question 9: Volume of a Cylinder**

**Description:**
Write a Python program with a function that calculates the volume of a cylinder given its radius and height.

**Function Signature:**
```python
def calculate_cylinder_volume(radius, height):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
calculate_cylinder_volume(3, 5)

Output:
141.3716694115407
```

Test Case 2:
```python
Input:
calculate_cylinder_volume(4, 8)

Output:
321.64286468209243
```

**Question 10: Quadratic Equation Solver**

**Description:**
Create a Python program with a function that solves a quadratic equation and returns the roots.

**Function Signature:**
```python
def solve_quadratic_equation(a, b, c):
    # Implementation of the function
```

**Test Cases:**

Test Case 1:
```python
Input:
solve_quadratic_equation(1, -3, 2)

Output:
(2.0, 1.0)
```

Test Case 2:
```python
Input:
solve_quadratic_equation(2, 5, 2)

Output:
(-0.5, -2.0)
```


Certainly! Here are 10 situation-based Python programming questions involving scope and global variables, along with two test cases for each:

**Question 1: Global Variable Modification**

**Description:**
Write a Python program with a global variable `counter`. Implement a function that increments the value of `counter` each time it is called.

**Test Cases:**

Test Case 1:
```python
# Initial counter value
counter = 0

# Function call
increment_counter()

# Updated counter value
print(counter)
```

Test Case 2:
```python
# Initial counter value
counter = 5

# Function call
increment_counter()

# Updated counter value
print(counter)
```

**Question 2: Local and Global Variables**

**Description:**
Create a Python program with a global variable `total` and a function that calculates the sum of a list of numbers. The function should use a local variable `result`.

**Test Cases:**

Test Case 1:
```python
# Initial global variable
total = 0

# Function call
calculate_sum([1, 2, 3, 4, 5])

# Updated global variable
print(total)
```

Test Case 2:
```python
# Initial global variable
total = 10

# Function call
calculate_sum([5, 8, 2, 3])

# Updated global variable
print(total)
```

**Question 3: Local Variable Shadowing**

**Description:**
Write a Python program with a global variable `x` and a function that declares a local variable with the same name `x`. Print both the global and local variables inside the function.

**Test Cases:**

Test Case 1:
```python
# Initial global variable
x = 10

# Function call
print_variables()

# Global variable value
print(x)
```

Test Case 2:
```python
# Initial global variable
x = 7

# Function call
print_variables()

# Global variable value
print(x)
```

**Question 4: Global List Modification**

**Description:**
Create a Python program with a global list `numbers`. Implement a function that appends a new number to the list each time it is called.

**Test Cases:**

Test Case 1:
```python
# Initial global list
numbers = [1, 2, 3]

# Function call
append_number(5)

# Updated global list
print(numbers)
```

Test Case 2:
```python
# Initial global list
numbers = [10, 20]

# Function call
append_number(15)

# Updated global list
print(numbers)
```

**Question 5: Global Variable within a Function**

**Description:**
Write a Python program with a function that uses a global variable `total` to keep track of the cumulative sum of its arguments.

**Test Cases:**

Test Case 1:
```python
# Function call
calculate_cumulative_sum(3, 7, 2)

# Global variable value
print(total)
```

Test Case 2:
```python
# Function call
calculate_cumulative_sum(5, 8, 1)

# Global variable value
print(total)
```

**Question 6: Scope of Parameters**

**Description:**
Create a Python program with a function that takes parameters `a` and `b`. Print the values of `a` and `b` inside and outside the function to observe their scopes.

**Test Cases:**

Test Case 1:
```python
# Initial values
a = 3
b = 9

# Function call
print_parameters(a, b)
```

Test Case 2:
```python
# Initial values
a = 12
b = 6

# Function call
print_parameters(a, b)
```

**Question 7: Nested Functions and Local Variables**

**Description:**
Write a Python program with a function that defines a local variable and a nested function. The nested function should access and modify the local variable.

**Test Cases:**

Test Case 1:
```python
# Function call
outer_function(5)

# Updated local variable value
print(local_variable)
```

Test Case 2:
```python
# Function call
outer_function(10)

# Updated local variable value
print(local_variable)
```

**Question 8: Global Variable in Nested Function**

**Description:**
Create a Python program with a global variable `result` and a function that defines a nested function. The nested function should access and modify the global variable.

**Test Cases:**

Test Case 1:
```python
# Initial global variable
result = 0

# Function call
outer_function(3, 7)

# Updated global variable value
print(result)
```

Test Case 2:
```python
# Initial global variable
result = 10

# Function call
outer_function(5, 4)

# Updated global variable value
print(result)
```

**Question 9: Unpacking Parameters in a Function**

**Description:**
Write a Python program with a function that takes a tuple as a parameter and unpacks its elements to calculate their sum.

**Test Cases:**

Test Case 1:
```python
# Function call
calculate_sum_from_tuple((1, 2, 3, 4, 5))
```

Test Case 2:
```python
# Function call
calculate_sum_from_tuple((10, 15, 8, 7))
```

**Question 10: Recursive Function with Local Variables**

**Description:**
Create a Python program with a recursive function that calculates the factorial of a given number using local variables.

**Test Cases:**

Test Case 1:
```python
# Function call
factorial_result = calculate_factorial_recursive(5)

# Result
print(factorial_result)
```

Test Case 2:
```python
# Function call
factorial_result = calculate_factorial_recursive(8)

# Result
print(factorial_result)
```
""")