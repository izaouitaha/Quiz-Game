import tkinter as tk
from pathlib import Path
import json

# Data
with open("data.json", "r") as file:
    questions = json.load(file)

# Variables

current_q = 0
score = 0

# Window

root = tk.Tk()
root.title("Quiz Game")
root.geometry("500x400")
root.config(bg="saddlebrown")


# Widgets

title = tk.Label(root, text="Quiz Game", font=("Arial", 20, "bold"), bg="saddlebrown", fg="white")
title.pack(pady=10)

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, bg="saddlebrown", fg="white")
question_label.pack(pady=20)

buttons = []

for i in range(3):
    btn = tk.Button(root, text="", width=25, font=("Arial", 12))
    btn.pack(pady=5)
    buttons.append(btn)

feedback_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="saddlebrown", fg="white")
feedback_label.pack(pady=10)

next_btn = tk.Button(root, text="Next", state="disabled", command=lambda: next_question())
next_btn.pack(pady=10)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 12), bg ="saddlebrown", fg="white")
score_label.pack(pady=10)

restart_btn = tk.Button(root, text="Restart", command=lambda: restart_game())
restart_btn.pack(pady=10)


# Functions

def load_question():
    global current_q

    if current_q < len(questions):
        q = questions[current_q]
        question_label.config(text=q["question"])
        feedback_label.config(text="")
        next_btn.config(state="disabled")

        for i in range(3):
            buttons[i].config(
                text=q["choices"][i],
                state="normal",
                bg="SystemButtonFace",
                command=lambda choice=q["choices"][i]: check_answer(choice)
            )
    else:
        question_label.config(text=f"مبروك انتهيت! نتيجتك هي: {score}/{len(questions)}")
        for btn in buttons:
            btn.config(state="disabled")
        next_btn.config(state="disabled")


def check_answer(choice):
    global score

    correct = questions[current_q]["answer"]

    for btn in buttons:
        btn.config(state="disabled")

    if choice == correct:
        score += 1
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text=f"خطأ! الإجابة الصحيحة هي: {correct}", fg="gold")

    score_label.config(text=f"Score: {score}")
    next_btn.config(state="normal")


def next_question():
    global current_q
    current_q += 1
    load_question()


def restart_game():
    global current_q, score
    current_q = 0
    score = 0
    score_label.config(text="Score: 0")
    load_question()


# Start

load_question()
root.mainloop()