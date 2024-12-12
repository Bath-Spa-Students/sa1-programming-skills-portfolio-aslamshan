'''
Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the
values. Try giving both your first and second name when asked for your name.
What happens? How can you handle multiple words in Python? Test the
program by entering a string value for age (e.g., “twenty”). What happens?
How can you prevent this issue?'''
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
age = (input("Enter your age: "))
biography = {
    "name": name,
    "hometown": hometown,
    "age": age
}
print(f"Name: {biography['name']}\nHometown: {biography['hometown']}\nAge: {biography['age']}")