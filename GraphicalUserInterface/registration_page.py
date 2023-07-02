# Dosen't use
import tkinter as tk
from json_handler import readUsers, writeUsers, encryptPassword

class RegistrationPage(tk.Frame):
    def __init__(self, parent, login_page):
        """
        shit 2
        """
        super().__init__(parent)
        self.parent = parent
        self.username_entry_label = tk.Label(self,text="Email:")
        self.username_entry = tk.Entry(self)
        self.password_entry_label = tk.Label(self,text="Password:")
        self.password_entry = tk.Entry(self, show="*")
        self.confirm_password_entry_label = tk.Label(self,text="Confirm password:")
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.login_button = tk.Button(self, text="Back to Login", command=login_page)

        self.username_entry_label.pack(pady=2)
        self.username_entry.pack(padx=150, pady=2)
        self.password_entry_label.pack(pady=2)
        self.password_entry.pack(pady=2)
        self.confirm_password_entry_label.pack(pady=2)
        self.confirm_password_entry.pack(pady=2)
        self.register_button.pack(pady=2)
        self.login_button.pack(pady=2)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        if username == "" or password == "":
            tk.messagebox.showerror("Registration Failed", "Fill all fields")
            return
        
        if password != confirm_password:
            tk.messagebox.showerror("Registration Failed", "Passwords do not match")
            return

        users = readUsers()
        for user in users:
            if user["username"] == username:
                tk.messagebox.showerror("Registration Failed", "Username already exists")
                return

        new_user = {
            "username": username,
            "password": encryptPassword(password)
        }

        users.append(new_user)
        writeUsers(users)

        tk.messagebox.showinfo("Registration Successful", "Registered successfully! You can now login.")

