# PYTHON Quiz Game
# CloudExify Python Internship - Month 2 Project 3 
# Jaweria Nawaz | Registration No: CX-INT-2026-PY-0119
# 

import random

QUESTIONS = [
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": {"A": "6", "B": "8", "C": "9", "D": "23"},
        "answer": "B"
    },
    {
        "question": "Which keyword defines a function?",
        "options": {"A": "function", "B": "define", "C": "def", "D": "func"},
        "answer": "C"
    },
    {
        "question": "What data type is: x = [1, 2, 3]?",
        "options": {"A": "tuple", "B": "dict", "C": "string", "D": "list"},
        "answer": "D"
    },
    {
        "question": "How do you get user input?",
        "options": {"A": "get()", "B": "input()", "C": "read()", "D": "scan()"},
        "answer": "B"
    },
    {
        "question": "What does len([1, 2, 3, 4]) return?",
        "options": {"A": "3", "B": "5", "C": "4", "D": "0"},
        "answer": "C"
    },
    {
        "question": "Which loop runs while a condition is True?",
        "options": {"A": "for", "B": "while", "C": "if", "D": "do"},
        "answer": "B"
    },
    {
        "question": "How do you create a comment in Python?",
        "options": {"A": "//", "B": "/**/", "C": "#", "D": "--"},
        "answer": "C"
    },
    {
        "question": "What does print(type(3.14)) output?",
        "options": {"A": "int", "B": "float", "C": "str", "D": "num"},
        "answer": "B"
    },
    {
        "question": "How do you open a file for reading?",
        "options": {"A": "open('f','w')", "B": "open('f','a')", "C": "open('f','r')", "D": "open('f','x')"},
        "answer": "C"
    },
    {
        "question": "What is output of: print('Hello'[0])?",
        "options": {"A": "Hello", "B": "H", "C": "e", "D": "0"},
        "answer": "B"
    },
    {
        "question": "What is the correct way to start an if statement?",
        "options": {"A": "if x > 5 then", "B": "if (x > 5)", "C": "if x > 5:", "D": "if x > 5"},
        "answer": "C"
    },
    {
        "question": "What does range(5) produce?",
        "options": {"A": "1 to 5", "B": "0 to 4", "C": "0 to 5", "D": "1 to 4"},
        "answer": "B"
    },
    {
        "question": "How do you add an item to a list?",
        "options": {"A": "list.add()", "B": "list.append()", "C": "list.insert()", "D": "list.push()"},
        "answer": "B"
    },
    {
        "question": "What is the output of: print(10 // 3)?",
        "options": {"A": "3.33", "B": "3", "C": "4", "D": "3.0"},
        "answer": "B"
    },
    {
        "question": "Which operator is used for string concatenation?",
        "options": {"A": "*", "B": "&", "C": "+", "D": "%"},
        "answer": "C"
    },
]

def ask_question(question_data, q_number, total):
    print(f"\nQuestion {q_number} of {total}")
    print("-" * 40)
    print(question_data["question"])
    print()
    for letter, option in question_data["options"].items():
        print(f"   {letter}) {option}")
    print()
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        print("Please enter A, B, C, or D only!")
    correct = question_data["answer"]
    if answer == correct:
        print("CORRECT! Well done!")
        return True
    else:
        correct_text = question_data["options"][correct]
        print(f"Wrong! Correct answer was {correct}) {correct_text}")
        return False

def get_grade(score, total):
    percentage = (score / total) * 100
    if percentage >= 90:
        return "A", "Excellent! Outstanding performance!"
    elif percentage >= 80:
        return "B", "Great job! Very good performance!"
    elif percentage >= 70:
        return "C", "Good. You passed with decent marks."
    elif percentage >= 60:
        return "D", "You passed but needs improvement."
    else:
        return "F", "You did not pass. Keep practicing!"

def show_results(score, total):
    percentage = (score / total) * 100
    grade, message = get_grade(score, total)
    print("\n" + "=" * 40)
    print("      QUIZ COMPLETED!")
    print("=" * 40)
    print(f"  Score      : {score} / {total}")
    print(f"  Percentage : {percentage:.1f}%")
    print(f"  Grade      : {grade}")
    print(f"  Result     : {message}")
    print("=" * 40)

def load_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def save_high_score(score):
    current_high = load_high_score()
    if score > current_high:
        with open("highscore.txt", "w") as f:
            f.write(str(score))
        print(f"NEW HIGH SCORE: {score}!")
        return True
    return False

def play_quiz():
    questions = QUESTIONS.copy()
    random.shuffle(questions)
    game_questions = questions[:10]
    score = 0
    total = len(game_questions)
    high_score = load_high_score()
    print("=" * 40)
    print("  CLOUDEXIFY PYTHON QUIZ GAME")
    print("=" * 40)
    print(f"  Questions: {total}")
    print(f"  High Score: {high_score}")
    print("  Answer with A, B, C, or D")
    print("=" * 40)
    input("  Press Enter to start...")
    for i, question in enumerate(game_questions, 1):
        is_correct = ask_question(question, i, total)
        if is_correct:
            score += 1
    show_results(score, total)
    save_high_score(score)

def main():
    while True:
        play_quiz()
        print()
        again = input("Play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()