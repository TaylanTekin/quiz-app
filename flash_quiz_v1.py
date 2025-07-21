question_1 = "What is the capital of France?"
question_2 = "What does CPU stand for?"
question_3 = "What is 2 + 2?"

answer_1 = "paris"
answer_2 = "central processing unit"
answer_3 = "4"


while True:
    score = 0
    print("Flashcard Quiz")
    input_1 = input(f"{question_1}: ")
    if input_1.strip().lower() != answer_1:
        print("Wrong! The correct answer was Paris.")
    else:
        print("Correct!")
        score += 1
        
    input_2 = input(f"{question_2}: ")
    if input_2.strip().lower() != answer_2:
        print("Wrong! The correct anwser was Central Processing Unit.")
    else:
        print("Correct!")
        score += 1
    input_3 = input(f"{question_3}: ")
    if input_3 != answer_3:
        print("Wrong! The correct answer was 4.")
    else:
        print("Correct!")
        score += 1
    print(f"\nYou got {score} out of 3 correct!")
    
    again = input("Do you want to take the quiz again? (y/n): ")
    if again.strip().lower() != "y":
        print("Goodbye!")
        break
    else:
        continue