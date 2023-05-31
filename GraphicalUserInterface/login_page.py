import tkinter as tk
from json_handler import read_users, encrypt_password

class LoginPage(tk.Frame):
    def __init__(self, parent, registration_page):
        """
        shit
        """
        super().__init__(parent)
        self.parent = parent
        self.username_entry_label = tk.Label(self,text="Email:")
        self.username_entry = tk.Entry(self)
        self.password_entry_label = tk.Label(self,text="Password:")
        self.password_entry = tk.Entry(self,show="*")
        self.login_button = tk.Button(self, text="Login", command=self.redirect_to_login)
        self.register_button = tk.Button(self, text="Register", command=registration_page)

        self.username_entry_label.pack(pady=2)
        self.username_entry.pack(padx=150, pady=2)
        self.password_entry_label.pack(pady=2)
        self.password_entry.pack(pady=2)
        self.login_button.pack(pady=5)
        self.register_button.pack()

    def redirect_to_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        users = read_users()
        for user in users:
            if user["username"] == username and user["password"] == encrypt_password(password):
                tk.messagebox.showinfo("Login Successful", "Logged in successfully!")
                self.redirect_to_event_page()  # Call the method to open the Event page
                return

        tk.messagebox.showerror("Login Failed", "Invalid username or password")

    def redirect_to_event_page(self):
        self.parent.show_event_page()  # Call the method in the parent Application class to open the Event page
