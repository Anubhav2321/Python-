# Quiz App in Python

def welcome():
    print("🎯 Welcome to the Python Quiz App!")
    name = input("Enter your name: ")
    print(f"\nHello, {name}! Let's begin the quiz.\n")
    print("-" * 40)

def ask_questions():
    score = 0
    questions = [
        {
            "question": "1️⃣ What is the capital of France?",
            "options": ["A. Paris", "B. Rome", "C. Madrid", "D. Berlin"],
            "answer": "A"
        },
        {
            "question": "2️⃣ What does CPU stand for?",
            "options": ["A. Central Processing Unit", "B. Computer Personal Unit", "C. Central Processor Utility", "D. None"],
            "answer": "A"
        },
        {
            "question": "3️⃣ Which programming language is known as the language of AI?",
            "options": ["A. Python", "B. C++", "C. Java", "D. Prolog"],
            "answer": "D"
        },
        {
            "question": "4️⃣ Who developed Python?",
            "options": ["A. Dennis Ritchie", "B. Guido van Rossum", "C. James Gosling", "D. Bjarne Stroustrup"],
            "answer": "B"
        },
        {
            "question": "5️⃣ What is 5 * 6?",
            "options": ["A. 11", "B. 25", "C. 30", "D. 56"],
            "answer": "C"
        }
        ,
        {
            "question": "6️⃣ what is the process called when liquid turns into gas?",
            "options": ["A.condensation", "B.Evaporation", "C.Sublimation", "D.Melting"],
            "answer": "B"
        }
        ,
            {
                "question": "7️⃣ What is the largest ocean on Earth?",
                "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
                "answer": "D"
            },
            {
                "question": "8️⃣ How many colors are in a Rainbow?",
                "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
                "answer": "C"
            }
        ]

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        ans = input("Your answer (A/B/C/D): ").strip().upper()

        if ans == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}\n")
        print("-" * 40)

    return score, len(questions)

def show_result(score, total):
    print("\n🎉 Quiz Completed!")
    print(f"Your final score: {score}/{total}")
    percentage = (score / total) * 100
    print(f"That's {percentage:.2f}%!")

    if percentage == 100:
        print("🏆 Excellent! Perfect score!")
    elif percentage >= 60:
        print("👍 Good job! Keep it up.")
    else:
        print("📘 Keep practicing — you’ll get better!")

def main():
    welcome()
    score, total = ask_questions()
    show_result(score, total)

if __name__ == "__main__":
    main()
