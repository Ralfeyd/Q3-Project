#Luke Duran 04/13/25

import tkinter as tk
from Admin_interface import admin_login_screen, add_question_form

def start_admin_flow():
    add_question_form(root)

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
