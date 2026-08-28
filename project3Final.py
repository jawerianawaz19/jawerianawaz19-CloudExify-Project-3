# PYTHON Quiz Game
# CloudExify Python Internship - Month 2 Project 3(final version)
# Jaweria Nawaz | Registration No: CX-INT-2026-PY-0119




import random
import time

QUESTIONS = [
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": {"A": "6", "B": "8", "C": "9", "D": "23"},
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "Which keyword defines a function?",
        "options": {"A": "function", "B": "define", "C": "def", "D": "func"},
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "What data type is: x = [1, 2, 3]?",
        "options": {"A": "tuple", "B": "dict", "C": "string", "D": "list"},
        "answer": "D",
        "difficulty": "easy"
    },
    {
        "question": "How do you get user input?",
        "options": {"A": "get()", "B": "input()", "C": "read()", "D": "scan()"},
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "What does len([1, 2, 3, 4]) return?",
        "options": {"A": "3", "B": "5", "C": "4", "D": "0"},
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "Which loop runs while a condition is True?",
        "options": {"A": "for", "B": "while", "C": "if", "D": "do"},
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "How do you create a comment in Python?",
        "options": {"A": "//", "B": "/**/", "C": "#", "D": "--"},
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "What does print(type(3.14)) output?",
        "options": {"A": "int", "B": "float", "C": "str", "D": "num"},
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "How do you open a file for reading?",
        "options": {"A": "open('f','w')", "B": "open('f','a')", "C": "open('f','r')", "D": "open('f','x')"},
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "What is output of: print('Hello'[0])?",
        "options": {"A": "Hello", "B": "H", "C": "e", "D": "0"},
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "What is the correct way to start an if statement?",
        "options": {"A": "if x > 5 then", "B": "if (x > 5)", "C": "if x > 5:", "D": "if x > 5"},
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "What does range(5) produce?",
        "options": {"A": "1 to 5", "B": "0 to 4", "C": "0 to 5", "D": "1 to 4"},
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "How do you add an item to a list?",
        "options": {"A": "list.add()", "B": "list.append()", "C": "list.insert()", "D": "list.push()"},
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "What is the output of: print(10 // 3)?",
        "options": {"A": "3.33", "B": "3", "C": "4", "D": "3.0"},
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "Which operator is used for string concatenation?",
        "options": {"A": "*", "B": "&", "C": "+", "D": "%"},
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "What is the output of: print([1, 2, 3][1:])?",
        "options": {"A": "[1, 2]", "B": "[2, 3]", "C": "[1, 2, 3]", "D": "[3]"},
        "answer": "B",
        "difficulty": "hard"
    },
    {
        "question": "What does the following return: bool([])?",
        "options": {"A": "True", "B": "False", "C": "None", "D": "Error"},
        "answer": "B",
        "difficulty": "hard"
    },
    {
        "question": "How do you handle exceptions in Python?",
        "options": {"A": "try/except", "B": "catch/throw", "C": "error/handle", "D": "check/raise"},
        "answer": "A",
        "difficulty": "hard"
    },
    {
        "question": "What is a dictionary key requirement?",
        "options": {"A": "Must be string", "B": "Must be mutable", "C": "Must be immutable", "D": "Must be integer"},
        "answer": "C",
        "difficulty": "hard"
    },
    {
        "question": "What does *args allow in a function?",
        "options": {"A": "Keyword arguments", "B": "Variable number of positional arguments", "C": "Default values", "D": "Return multiple values"},
        "answer": "B",
        "difficulty": "hard"
    },
    {
        "question": "What is the result of: 3 * 'ab'?",
        "options": {"A": "ababab", "B": "ab3", "C": "Error", "D": "3ab"},
        "answer": "A",
        "difficulty": "hard"
    },
    {
        "question": "Which method removes and returns the last item of a list?",
        "options": {"A": "remove()", "B": "delete()", "C": "pop()", "D": "clear()"},
        "answer": "C",
        "difficulty": "hard"
    },
    {
        "question": "What does the 'with' statement primarily help with?",
        "options": {"A": "Loops", "B": "Resource management", "C": "Conditionals", "D": "Imports"},
        "answer": "B",
        "difficulty": "hard"
    },
    {
        "question": "What is the output of: print({1, 2, 2, 3})?",
        "options": {"A": "{1, 2, 2, 3}", "B": "{1, 2, 3}", "C": "[1, 2, 3]", "D": "Error"},
        "answer": "B",
        "difficulty": "hard"
    },
    {
        "question": "How do you create a virtual environment in Python?",
        "options": {"A": "python -m venv env", "B": "pip install venv", "C": "python create env", "D": "virtualenv --create"},
        "answer": "A",
        "difficulty": "hard"
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
    print("You have 30 seconds to answer!")
    start_time = time.time()
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        elapsed = time.time() - start_time
        if elapsed > 30:
            print("Time's up! You took more than 30 seconds.")
            correct = question_data["answer"]
            correct_text = question_data["options"][correct]
            print(f"Wrong! Correct answer was {correct}) {correct_text}")
            return False, answer, correct, True
        if answer in ["A", "B", "C", "D"]:
            break
        print("Please enter A, B, C, or D only!")
    correct = question_data["answer"]
    if answer == correct:
        print("CORRECT! Well done!")
        return True, answer, correct, False
    else:
        correct_text = question_data["options"][correct]
        print(f"Wrong! Correct answer was {correct}) {correct_text}")
        return False, answer, correct, False

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

def show_results(score, total, review_list):
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
    print("\n--- ANSWER REVIEW ---")
    for i, item in enumerate(review_list, 1):
        status = "Correct" if item["is_correct"] else "Wrong"
        timed_out = " (Timed Out)" if item["timed_out"] else ""
        print(f"Q{i}: {item['question']}")
        print(f"   Your answer: {item['user_answer']} | Correct: {item['correct_answer']} | {status}{timed_out}")
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

def load_leaderboard():
    leaderboard = []
    try:
        with open("leaderboard.txt", "r") as f:
            for line in f:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    name, score = parts[0], int(parts[1])
                    leaderboard.append((name, score))
    except FileNotFoundError:
        pass
    return sorted(leaderboard, key=lambda x: x[1], reverse=True)

def save_to_leaderboard(name, score):
    leaderboard = load_leaderboard()
    leaderboard.append((name, score))
    leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)[:10]
    with open("leaderboard.txt", "w") as f:
        for n, s in leaderboard:
            f.write(f"{n}:{s}\n")

def show_leaderboard():
    leaderboard = load_leaderboard()
    print("\n--- LEADERBOARD (Top 10) ---")
    if not leaderboard:
        print("No scores yet.")
    else:
        for i, (name, score) in enumerate(leaderboard, 1):
            print(f"{i}. {name}: {score}")
    print("=" * 40)

def select_difficulty():
    print("\nSelect Difficulty:")
    print("1. Easy")
    print("2. Hard")
    print("3. Mixed (All questions)")
    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice == "1":
            return "easy"
        elif choice == "2":
            return "hard"
        elif choice == "3":
            return "mixed"
        print("Please enter 1, 2, or 3 only!")

def play_quiz():
    name = input("Enter your name: ").strip()
    if not name:
        name = "Player"
    difficulty = select_difficulty()
    if difficulty == "easy":
        filtered = [q for q in QUESTIONS if q["difficulty"] == "easy"]
    elif difficulty == "hard":
        filtered = [q for q in QUESTIONS if q["difficulty"] == "hard"]
    else:
        filtered = QUESTIONS.copy()
    questions = filtered.copy()
    random.shuffle(questions)
    game_questions = questions[:10] if len(questions) >= 10 else questions
    score = 0
    total = len(game_questions)
    high_score = load_high_score()
    review_list = []
    print("=" * 40)
    print("  CLOUDEXIFY PYTHON QUIZ GAME")
    print("=" * 40)
    print(f"  Player     : {name}")
    print(f"  Difficulty : {difficulty.upper()}")
    print(f"  Questions  : {total}")
    print(f"  High Score : {high_score}")
    print("  Timer      : 30 seconds per question")
    print("  Answer with A, B, C, or D")
    print("=" * 40)
    input("  Press Enter to start...")
    for i, question in enumerate(game_questions, 1):
        is_correct, user_ans, correct_ans, timed_out = ask_question(question, i, total)
        review_list.append({
            "question": question["question"],
            "user_answer": user_ans if not timed_out else "TIMEOUT",
            "correct_answer": correct_ans,
            "is_correct": is_correct,
            "timed_out": timed_out
        })
        if is_correct:
            score += 1
    show_results(score, total, review_list)
    save_high_score(score)
    save_to_leaderboard(name, score)
    show_leaderboard()

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