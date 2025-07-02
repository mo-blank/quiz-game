import json
import random
import time

def load_questions(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def filter_questions_by_difficulty(questions, level):
    return [q for q in questions if q.get('difficulty', 'easy') == level]

def ask_question(question_data, question_num, total_questions, time_limit=15):
    print(f"\n📘 Question {question_num} of {total_questions}")
    print(question_data['question'])

    options = question_data['options']
    random.shuffle(options)

    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    start_time = time.time()
    while True:
        try:
            user_input = input(f"Answer (you have {time_limit} seconds): ")
            elapsed = time.time() - start_time

            if elapsed > time_limit:
                print("⏰ Time's up!")
                return False

            user_choice = int(user_input)
            if 1 <= user_choice <= len(options):
                selected = options[user_choice - 1]
                if selected == question_data['answer']:
                    print("✅ Correct!")
                    return True
                else:
                    print(f"❌ Incorrect. The correct answer was: {question_data['answer']}")
                    return False
            else:
                print("Invalid option number.")
        except ValueError:
            print("Please enter a valid number.")

def save_score(name, score, total, filename="scores.txt"):
    with open(filename, "a") as file:
        file.write(f"{name} scored {score}/{total}\n")

def run_quiz(file_path):
    print("🎓 Welcome to the Python Quiz Game!")
    name = input("Enter your name: ")

    all_questions = load_questions(file_path)
    easy_questions = filter_questions_by_difficulty(all_questions, "easy")
    hard_questions = filter_questions_by_difficulty(all_questions, "hard")

    random.shuffle(easy_questions)
    random.shuffle(hard_questions)

    # Set how many to use from each difficulty
    easy_limit = min(10, len(easy_questions))
    hard_limit = min(5, len(hard_questions))
    total_questions = easy_limit + hard_limit

    score = 0
    question_number = 1

    for q in easy_questions[:easy_limit]:
        if ask_question(q, question_number, total_questions):
            score += 1
        question_number += 1

    if hard_limit > 0:
        print("\n⚠️ Difficulty increasing to HARD level!\n")

    for q in hard_questions[:hard_limit]:
        if ask_question(q, question_number, total_questions):
            score += 1
        question_number += 1

    print(f"\n🏁 {name}, your final score is {score}/{total_questions}")
    save_score(name, score, total_questions)

if __name__ == "__main__":
    run_quiz("questions.json")
