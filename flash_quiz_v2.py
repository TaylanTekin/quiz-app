import random
import os

def choose_quiz_file():
    print("Available quiz files in this folder:")
    files = [f for f in os.listdir() if f.endswith(".txt") and f not in ("highscore.txt", "missed.txt") and is_valid_quiz_file(f)]

    if not files:
        print("No valid quiz files found. Please create a quiz file in the format 'question|answer|topic'.")
        return None

    for i, f in enumerate(files, start=1):
        print(f"{i}. {f}")

    while True:
        try:
            choice = input("\nEnter the number of the quiz file you want to load: ").strip()
            index = int(choice) - 1
            if 0 <= index < len(files):
                return files[index]
            else:
                print("Invalid number. Please choose a valid file number.")
        except ValueError:
            print("Please enter a valid number.")

def is_valid_quiz_file(filename):
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) >= 2:
                    return True
        return False
    except:
        return False

def load_questions(filename):
    questions = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    q, a, topic = parts
                    questions.append((q, a.strip().lower(), topic.strip().lower()))
                elif len(parts) == 2:
                    q, a = parts
                    questions.append((q, a.strip().lower(), "general"))
    return questions

def load_missed(filename):
    missed = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                if "---" in line or "|" not in line:
                    continue
                parts = line.strip().split("|")
                if len(parts) >= 2:
                    q = parts[0].strip()
                    a = parts[1].strip()
                    missed.append((q, a))
    return missed

if not os.path.exists("highscore.txt") or os.path.getsize("highscore.txt") == 0:
    with open("highscore.txt", "w") as file:
        file.write("0")
missed_this_session = []

while True:
    import time
    start_time = time.time()

    missed = 0
    total_questions = 0
    correct_amount = 0

    missed_questions = []

    quiz_file = choose_quiz_file()
    questions = load_questions(quiz_file)
    if not questions:
        print("No questions found. Please add questions to 'questions.txt'.")
        break

    topics = list(set(topic for _, _, topic in questions))
    print("Available topics:", ", ".join(topics))
    chosen_topic = input("Enter a topic (or 'all' for all topics): ").strip().lower()

    if chosen_topic != "all":
        questions = [q for q in questions if q[2] == chosen_topic]
        if not questions:
            print(f"No questions found for topic '{chosen_topic}'.")
            break

    with open("highscore.txt", "r") as file:
        content = file.read().strip()
        high_score = int(content) if content.isdigit() else 0
    score = 0
    random.shuffle(questions)
    for q, a, _ in questions:
        total_questions += 1
        user = input(f"{q}: ")
        if user.strip().lower() == a.strip().lower():
            print("Correct!")
            correct_amount += 1
        else:
            print(f"Wrong! The correct answer was {a.title()}.")
            missed_questions.append(f"{q} | {a} | Your answer: {user.strip()}")
            missed += 1
            missed_this_session.append((q, a))
            with open("missed.txt", "a") as f:
                f.write(f"{q}|{a}|{user.strip().lower()}\n")

    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("\n===Quiz Session Summary===")
    print(f"Total questions: {total_questions}")
    print(f"Correct answers: {correct_amount}")
    print(f"Missed questions: {missed}")
    print(f"Time taken: {minutes} minutes and {seconds} seconds")
    print(f"High score: {high_score}")
    print("===End of Quiz Session===")

    if missed_questions:
        with open("missed.txt", "w") as missed_file:
            missed_file.write("\n--- New Session ---\n")
            for item in missed_questions:
                missed_file.write(f"{item}\n")
        print("Your missed questions have been saved to 'missed.txt'.")

    if missed > 0:
        retry = input("Do you want to retry the missed questions? (y/n): ")
        if retry.strip().lower() == "y":
            print("\nRetrying missed questions...")
            missed = load_missed("missed.txt")
            for q, a in missed:
                user = input(f"{q}: ")
                if user.strip().lower() == a.strip().lower():
                    print("Correct!")
                    score += 1
                else:
                    print(f"Better luck next time! The correct answer was {a.title()}.")
        else:
            print("Goodbye!")
            break

    if missed_this_session:
        retry = input("Do you want to retry the missed questions from this session? (y/n): ")
        if retry.strip().lower() == "y":
            print("\nRetrying missed questions from this session...")
            for q, a in missed_this_session:
                user = input(f"{q}: ")
                if user.strip().lower() == a.strip().lower():
                    print("Correct!")
                    score += 1
                else:
                    print(f"Better luck next time! The correct answer was {a.title()}.")
        else:
            print("Goodbye!")
            break

    again = input("Do you want to take the quiz again? (y/n): ")
    if again.strip().lower() != "y":
        print("Goodbye!")
        break
    else:
        continue