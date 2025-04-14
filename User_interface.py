#Luke Duran 04/13/25

import tkinter as tk
import sqlite3
from Question import Question
from tkinter import messagebox

#Part 1 user GUI menu
def start_user_quiz(root, return_home_callback):

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
        display_quiz_questions(root, selected_course, return_home_callback)

    tk.Button(select_frame, text="Start Quiz", command=begin_quiz).pack(pady=10)

# Part 2 displays quiz questions all at once- and with scroll 
def display_quiz_questions(root, course_name, return_home_callback):

    # Frame that holds the scrollable quiz content
    outer_frame = tk.Frame(root)
    outer_frame.pack(fill="both", expand=True)

    # Canvas + Scrollbar setup
    canvas = tk.Canvas(outer_frame)
    scrollbar = tk.Scrollbar(outer_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    # Allow scrolling as inner frame grows
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    # Attach the scrollable frame to the canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Load questions from database
    conn = sqlite3.connect("Quiz.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {course_name}")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        tk.Label(scrollable_frame, text="No questions found for this quiz.").pack()
        return

    questions = []
    user_answers = []

#score tracker
    answered_var = tk.StringVar()
    answered_var.set("Answered: 0 / " + str(len(rows)))

# Tracker label
    tk.Label(scrollable_frame, textvariable=answered_var, font=("Arial", 12, "bold")).pack(pady=10)

    # Display each question and multiple-choice options
    for i, row in enumerate(rows):
        q_id, text, a, b, c, d, correct = row
        q = Question(text, [a, b, c, d], correct)
        questions.append(q)

        tk.Label(scrollable_frame, text=f"Q{i+1}: {q.question_text}", wraplength=600, justify="left", anchor="w").pack(anchor="w", pady=5)

        selected = tk.StringVar()
        def make_tracer(index):
            def tracer(*args):
                answered_count = sum(1 for ans in user_answers if ans.get() != "")
                answered_var.set(f"Answered: {answered_count} / {len(questions)}")
            return tracer

        selected.trace_add("write", make_tracer(i))
        user_answers.append(selected)

        for opt_idx, opt_label in enumerate(['A', 'B', 'C', 'D']):
            tk.Radiobutton(
                scrollable_frame,
                text=f"{opt_label}: {q.options[opt_idx]}",
                variable=selected,
                value=opt_label
            ).pack(anchor="w")

    # Final score screen on submission
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

        # Remove the quiz screen
        outer_frame.destroy()

        # Final score screen
        result_frame = tk.Frame(root)
        result_frame.pack(pady=100)

        tk.Label(result_frame, text="Quiz Completed!", font=("Arial", 20)).pack(pady=10)
        tk.Label(result_frame, text=f"Score: {score} / {total}", font=("Arial", 16)).pack(pady=5)
        tk.Label(result_frame, text=f"Unanswered: {unanswered}", font=("Arial", 14)).pack(pady=5)

        def return_home():
            result_frame.destroy()
            return_home_callback()

        tk.Button(result_frame, text="Return to Home", command=return_home, width=20).pack(pady=20)

    # submit button
    tk.Button(scrollable_frame, text="Submit Quiz", command=submit_quiz).pack(pady=20)
