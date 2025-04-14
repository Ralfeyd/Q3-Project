#Luke Duran 04/13/25

import tkinter as tk
from tkinter import messagebox

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
