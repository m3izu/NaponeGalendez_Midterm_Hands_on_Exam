import random

# Generate two random integers from 1 to 99
num1 = random.randint(1, 99)
num2 = random.randint(1, 99)

# Choose a random operation
operation = random.choice(["+", "-", "*", "/"])

# Generate the math question based on the chosen operation
if operation == "+":
    question = f"What is {num1} + {num2}?"
elif operation == "-":
    question = f"What is {num1} - {num2}?"
elif operation == "*":
    question = f"What is {num1} x {num2}?"
else:
    question = f"What is {num1} / {num2}?"

# Display the question to the student
print(question)

# Get the student's answer
student_answer = int(input())

# Calculate the correct answer
correct_answer = eval(f"{num1}{operation}{num2}")

# Check if the student's answer is correct
if student_answer == correct_answer:
    print(f"{num1}{operation}{num2} = {correct_answer}")
    print("Your answer is correct!")
else:
    print(f"{num1}{operation}{num2} = {correct_answer}")
    print("Your answer is incorrect!")
