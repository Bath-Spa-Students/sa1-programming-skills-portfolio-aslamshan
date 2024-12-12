'''
Exercise 6: Brute Force Attack - 30 Marks
Write a program that simulates a password entry system. The correct password
is defined as 12345. The program should keep asking the user to enter the
password until they provide the correct one.
Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the
correct one is entered.
3. Output an appropriate message when the correct password is entered.'''
correct_password = "12345"
while True:
    # Ask the user to enter the password
    user_password = input("Enter the password: ")

    # Check if the user's password matches the correct password
    if user_password == correct_password:
        # Step 3: Output an appropriate message when the correct password is entered
        print(f"Correct password!")
        break
    else:
        print("Incorrect password. Try again!")
