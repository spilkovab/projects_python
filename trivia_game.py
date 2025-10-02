from trivia_questions import questions
import random

def trivia():
    # Put only questions to a list
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    # Select random questions
    selected_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(selected_questions):
        # Print the question
        print(f"{idx +1}. {question}")
        # Let user answer
        user_answer = input(f"Your answer: ").lower().strip()
        # Fetch the correct answer
        correct = questions[question]

        # Check if answer is correct
        if user_answer==correct.lower():
            print("Correct!\n")
            score+=1
        else:
            print(f"Wrong! The correct answer is: {correct}.\n")
        
        print(f"Game over! Your score is {score}/{total_questions}")

trivia()