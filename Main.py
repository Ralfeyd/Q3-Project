#Luke Duran 04/13/25

import tkinter as tk
from Admin_interface import admin_login_screen, add_question_form, view_questions_form

def start_admin_flow():
    admin_menu = tk.Frame(root)
    admin_menu.pack(pady=50)

    tk.Label(admin_menu, text="Admin Panel", font=("Arial", 16)).pack(pady=10)

    tk.Button(admin_menu, text="Add Question", width=25, command=lambda: [admin_menu.destroy(), add_question_form(root)]).pack(pady=5)
    tk.Button(admin_menu, text="View Questions", width=25, command=lambda: [admin_menu.destroy(), view_questions_form(root)]).pack(pady=5)

def start_app():
    login_frame = tk.Frame(root)
    login_frame.pack(pady=50)

    tk.Label(login_frame, text="Quiz Bowl App", font=('Arial', 18)).pack(pady=10)
    tk.Button(login_frame, text="Admin", width=20, command=lambda: [login_frame.destroy(), admin_login_screen(root, start_admin_flow)]).pack(pady=5)
    tk.Button(login_frame, text="Take Quiz", width=20).pack(pady=5)  # Placeholder for quiz user interface

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quiz Bowl")
    root.geometry("500x500")
    start_app()
    root.mainloop()
