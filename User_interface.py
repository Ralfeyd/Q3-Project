#Luke Duran 04/13/25

import tkinter as tk
import sqlite3
from Question import Question
from tkinter import messagebox

#Part 1 user GUI menu
def start_user_quiz(root):
    select_frame = tk.Frame(root)
    select_frame.pack(pady=20)

    course_var = tk.StringVar()
    course_var.set("ProgrammingLogicAndAnalyticalThinking")

    tk.Label(select_frame, text="Select a Quiz Category:", font=("Arial", 14)).pack(pady=10)
    course_menu = tk.OptionMenu(select_frame, course_var,
        "ProgrammingLogicAndAnalyticalThinking",
        "BusinessDatabaseManagement",
        "DataDrivenDecisionMaking",
        "BusinessApplicationsDevelopment",
        "PrinciplesOfAccountingII"
    )
    course_menu.pack()

    def begin_quiz():
        selected_course = course_var.get()
        select_frame.destroy()
        display_quiz_questions(root, selected_course)

    tk.Button(select_frame, text="Start Quiz", command=begin_quiz).pack(pady=10)

# Part 2 displays quiz questions all at once
def display_quiz_questions(root, course_name):
    quiz_frame = tk.Frame(root)
    quiz_frame.pack(pady=10)

    conn = sqlite3.connect("Quiz.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {course_name}")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        tk.Label(quiz_frame, text="No questions found for this quiz.").pack()
        return

    questions = []
    user_answers = []

    for i, row in enumerate(rows):
        q_id, text, a, b, c, d, correct = row
        q = Question(text, [a, b, c, d], correct)
        questions.append(q)

        tk.Label(quiz_frame, text=f"Q{i+1}: {q.question_text}", wraplength=600, justify="left", anchor="w").pack(anchor="w", pady=5)

        selected = tk.StringVar()
        user_answers.append(selected)

        for opt_idx, opt_label in enumerate(['A', 'B', 'C', 'D']):
            tk.Radiobutton(
                quiz_frame,
                text=f"{opt_label}: {q.options[opt_idx]}",
                variable=selected,
                value=opt_label
            ).pack(anchor="w")

    def submit_quiz():
        score = 0
        total = len(questions)
        unanswered = 0

        for i, q in enumerate(questions):
            answer = user_answers[i].get()
            if answer == "":
                unanswered += 1
            elif q.check_answer(answer):
                score += 1

        messagebox.showinfo("Quiz Completed", f"You scored {score}/{total}.\nUnanswered: {unanswered}")
        quiz_frame.destroy()
# submit button
    tk.Button(quiz_frame, text="Submit Quiz", command=submit_quiz).pack(pady=20)

