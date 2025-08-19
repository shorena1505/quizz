import random
print("Welcome to the Simple Multiplication Quizz!")

i = 1
while i <= 5:
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    answer = num_1 * num_2

    user_input = int(input(f"Problem {i}: What is {num_1} x {num_2}? "))
    if not user_input.isdigit():
        print("Please enter only a number!")
    if user_input == answer:
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer is {answer}")

    i += 1
