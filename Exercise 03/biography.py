'''
Exercise 3: Biography - 25 Marks

In this exercise, you’ll create a program that stores and prints your name, home-
town, and age to the console using a Python dictionary.

Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a
dictionary.
2. Print the values on separate lines using a single print() statement.
3. Use variables with appropriate data types for each piece of information.
'''

biography = {
    "name": "John Doe",
    "hometown": "New York",
    "age": 25
}
print(f"Name: {biography['name']}\nHometown: {biography['hometown']}\nAge: {biography['age']}")