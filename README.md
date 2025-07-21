# 🧠 Quiz App v2

A powerful terminal-based **Quiz App** written in Python.  
Includes **dynamic file loading**, **missed question retrying**, **high score tracking**, and full support for `.txt` quiz files.

---

## 🚀 Features

- 📂 **Load external quiz files** (`.txt`)
- 🔁 **Retry missed questions** from this or previous sessions
- 💾 **Track and save high scores**
- 📊 **Filter compatible `.txt` quiz files** only
- ✏️ **Clean and customizable input system**
- 📈 Automatically logs missed questions to `missed.txt`
- 🧠 Fully offline — just Python

---

## 🖥️ Demo

```bash
Welcome to the Quiz App!
Choose a quiz file:
1. questions.txt
2. history_quiz.txt

Starting quiz...

Q: What is the capital of Germany?
Your answer: berlin
✅ Correct!

Q: What is the square root of 49?
Your answer: 6
❌ Incorrect! Correct answer: 7

...

Quiz finished. You scored 8 out of 10 (80.0%)
Missed questions saved to missed.txt.
```

---

## 📁 File Overview

| File              | Description                                  |
|-------------------|----------------------------------------------|
| `quiz_app_v2.py`  | Main program                                 |
| `questions.txt`   | Sample quiz file                             |
| `missed.txt`      | Missed questions across sessions             |
| `highscore.txt`   | Stores your top score                        |
| `quiz_app_v1.py`  | Old version (optional for reference)         |

---

## 📦 Installation

> **Requirements:** Python 3.8+

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/quiz-app-v2.git
cd quiz-app-v2
```

2. **Run the app**
```bash
python quiz_app_v2.py
```

---

## 🧾 How to Write Quiz Files

Each question must be written on **one line**, in the following format:

```txt
Question?;answer
```

✔️ Examples:
```txt
What is 2+2?;4
What is the capital of France?;paris
```

**Important:**
- Only use `;` to separate question from answer
- One question per line
- Save as `.txt` in the same directory

---

## 🔄 Retry Missed Questions

After any quiz:
- Incorrect answers are automatically added to `missed.txt`
- On next run, you'll be asked if you want to **retry missed questions first**

---

## 🏆 High Score Tracking

After each quiz, your score will be saved to `highscore.txt`.  
If your new score is higher than the previous best, it replaces the old one.

---

## 📌 Planned Features (Future Ideas)

- UI version using **Tkinter** or **Web (Flask/React)**
- AI question generation and learning
- Leaderboard (local or online)
- User accounts and profiles
- Time-limited questions & difficulty settings

---

## 👤 Author

**Taylan Tekin**  
📍 15 y/o Python Developer | Germany  
Working toward building high-impact, intelligent software and scalable platforms.  
💬 *"Always pushing to learn faster, build smarter, and go further."*

---

## 📜 License

MIT License — feel free to use, improve, and share.

---

## ⭐️ Like This Project?

Give it a ⭐ on GitHub — it helps others find it and shows your support!
