'''
Exercise 4: Primitive Quiz - 30 Marks
In this exercise, you’ll create a simple program that asks the user a question,
evaluates their answer, and provides feedback.
Steps:
1. Write a program that asks the user “What is the capital of France?” and
waits for their response.
2. If the user’s answer is correct (i.e., “Paris”), the program should print a
message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the
answer is wrong.
Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of
the capitalization (e.g., “paris”, “Paris”, and “PaRis” should all be considered
correct). Multiple Questions: Extend the program into a quiz that asks for the
capitals of 10 European countries. Provide feedback for each question.
'''
france = str (input("What is the capital of France? "))
if france .strip().lower() == "paris":
    print ('your answer in correct.')
else:
    print ('your answer in wrong')

Monaco = str (input("What is the capital of Monaco? "))
if Monaco .strip().lower() == "monaco":
    print ('your answer in correct.')
else:
    print ('your answer in wrong')

latvia = str (input("What is the capital of latvia? "))
if latvia .strip().lower() == "riga":
    print ('your answer in correct.')
else:
    print ('your answer in wrong')

Albania = str (input("What is the capital of Albania? "))
if Albania .strip().lower() == "tirana":
    print ('your answer in correct.')
else:
    print ('your answer in wrong')

Austria = str (input("What is the capital of Austria? "))
if Austria .strip().lower() == "Vienna":
    print ('your answer in correct.')
else:
    print ('your answer in wrong')

Belarus = str (input("What is the capital of Belarus? "))
if Belarus.strip().lower() == "minsk":
    print ('your answer in correct.')
else:
    print ('your answer in wrong')

Croatia = str (input("What is the capital of Croatia? "))
if Croatia.strip().lower() == "zagreb":
    print ('your answer in correct.')
else:
    print ('your answer in wrong')

Denmark = str (input("What is the capital of Denmark? "))
if Denmark.strip().lower() == "Copenhagen":
    print ('your answer in correct.')
else:
    print ('your answer in wrong')

Estonia = str (input("What is the capital of Estonia? "))
if Estonia.strip().lower() == "tallinn":
    print ('your answer in correct.')
else:
    print ('your answer in wrong')

Finland = str (input("What is the capital of Finland? "))
if Finland.strip().lower() == "helsinki":
    print ('your answer in correct.')
else:
    print ('your answer in wrong')
