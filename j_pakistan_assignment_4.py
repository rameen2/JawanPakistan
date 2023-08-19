# -*- coding: utf-8 -*-
"""j.Pakistan. assignment #4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NhcKf_mC-mJA55AjEYucNYy-3ZtWR4gC
"""

### 1. Make a calculator using Python with addition , subtraction ,
#multiplication ,division and power.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Quit")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice == '6':
        print("Calculator exiting.")
        break

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
    else:
        print("Invalid input")

### 2. Write a program to check if there is any numeric value in list using for loop.
def contains_numeric_value(lst):
    for item in lst:
        if isinstance(item, (int, float)):
            return True
    return False
my_list = [1, 'apple', 3.14, 'banana', True]

if contains_numeric_value(my_list):
    print("The list contains numeric values.")
else:
    print("The list does not contain numeric values.")
#In this program, the function contains_numeric_value takes a list as an argument and iterates through each item in the list using a for loop. It uses the isinstance() function to check if the current item is either an integer or a float (numeric types). If any such item is found, the function returns True, indicating that the list contains numeric values. If no numeric value is found after iterating through the entire list, the function returns False.

### 3. Write a Python script to add a key to a dictionary.
# Initial dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Key-value pair to add
new_key = 'occupation'
new_value = 'engineer'

# Adding the new key-value pair to the dictionary
my_dict[new_key] = new_value

# Printing the updated dictionary
print("Updated Dictionary:", my_dict)

### 4. Write a Python program to sum all the numeric items in a dictionary.
def sum_numeric_values(dictionary):
    total_sum = 0
    for value in dictionary.values():
        if isinstance(value, (int, float)):
            total_sum += value
    return total_sum

# Example dictionary
my_dict = {'a': 5, 'b': 3.14, 'c': 'apple', 'd': 10, 'e': 'banana'}

numeric_sum = sum_numeric_values(my_dict)
print("Sum of numeric values:", numeric_sum)
#In this program, the function sum_numeric_values takes a dictionary as an argument and iterates through the values of the dictionary using a for loop. It checks if each value is an instance of either an integer or a float (numeric types). If the value is numeric, it adds it to the total_sum variable. Finally, the function returns the total_sum.

#You can replace the my_dict dictionary with your own dictionary containing numeric and non-numeric values. The program will calculate and print the sum of the numeric values present in the dictionary.

### 5. Write a program to identify duplicate values from list.
def find_duplicate_values(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

# Example list
my_list = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]

duplicate_values = find_duplicate_values(my_list)
print("Duplicate values:", duplicate_values)

### 6. Write a Python script to check if a given key already exists in a dictionary
# Example dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Key to check
key_to_check = 'age'

if key_exists(my_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")