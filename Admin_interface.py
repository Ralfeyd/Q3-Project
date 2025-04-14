#Luke Duran 04/13/25

import tkinter as tk
import sqlite3
from tkinter import messagebox

# Admin login + GUI framework
ADMIN_PASSWORD = "Password1"  #Password for admin access!!

def admin_login_screen(root, open_admin_panel):
    def check_password():
        entered = password_entry.get()
        if entered == ADMIN_PASSWORD:
            login_frame.destroy()
            open_admin_panel()
        else:
            messagebox.showerror("Access Denied", "Incorrect password!")

    login_frame = tk.Frame(root)
    login_frame.pack(pady=100)

    tk.Label(login_frame, text="Admin Login", font=('Arial', 16)).pack(pady=10)
    tk.Label(login_frame, text="Enter Admin Password:").pack()
    password_entry = tk.Entry(login_frame, show="*")
    password_entry.pack(pady=5)

    tk.Button(login_frame, text="Login", command=check_password).pack(pady=10)


# admitted admin GUI framework for adding,editing, and deleting questions below

def add_question_form(root):
    form_frame = tk.Frame(root)
    form_frame.pack(pady=10)

    # Dropdown for course
    course_var = tk.StringVar()
    course_var.set("ProgrammingLogicAndAnalyticalThinking")
    tk.Label(form_frame, text="Select Course:").grid(row=0, column=0, sticky="e")
    course_menu = tk.OptionMenu(form_frame, course_var,
        "ProgrammingLogicAndAnalyticalThinking",
        "BusinessDatabaseManagement",
        "DataDrivenDecisionMaking",
        "BusinessApplicationsDevelopment",
        "PrinciplesOfAccountingII"
    )
    course_menu.grid(row=0, column=1)

    # Question + options
    labels = ["Question", "Option A", "Option B", "Option C", "Option D", "Correct Option (A-D)"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(form_frame, text=label + ":").grid(row=i+1, column=0, sticky="e")
        entry = tk.Entry(form_frame, width=50)
        entry.grid(row=i+1, column=1, padx=5, pady=2)
        entries.append(entry)

    def submit_question():
        table = course_var.get()
        question, a, b, c, d, correct = [e.get() for e in entries]

        if correct.upper() not in ['A', 'B', 'C', 'D']:
            messagebox.showerror("Invalid", "Correct answer must be A, B, C, or D.")
            return

        try:
            conn = sqlite3.connect("Quiz.db")
            cur = conn.cursor()
            cur.execute(f'''
                INSERT INTO {table} (question, option_a, option_b, option_c, option_d, correct_option)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (question, a, b, c, d, correct.upper()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Question added successfully!")
            for e in entries:
                e.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(form_frame, text="Add Question", command=submit_question).grid(row=7, column=0, columnspan=2, pady=10)
