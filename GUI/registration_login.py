import tkinter as tk
import json
import os

class TicketReservationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Eventim Ticket Reservation")
        master.geometry("1280x720+100+100")
        master.resizable(True, True)
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        self.width = int(self.screen_width * 0.8)
        self.height = int(self.width * 9/16)
        master.geometry(f"{self.width}x{self.height}+{int((self.screen_width-self.width)/2)}+{int((self.screen_height-self.height)/2)}")

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.grid(row=0, column=0)
        self.username_entry = tk.Entry(master)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.grid(row=1, column=1)

        self.sign_up_button = tk.Button(master, text="Sign Up", command=self.sign_up)
        self.sign_up_button.grid(row=2, columnspan=2)

        self.sign_in_button = tk.Button(master, text="Sign In", command=self.sign_in)
        self.sign_in_button.grid(row=3, columnspan=2)

    def sign_up(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            # tk.messagebox.showerror("Error", "Username and password fields are required.")
            return

        if os.path.exists("./GUI/users.json"):
            with open("./GUI/users.json", "r") as f:
                users = json.load(f)
        else:
            users = {}

        if username in users:
            # tk.messagebox.showerror("Error", "Username already exists.")
            return

        users[username] = {"password": password}

        with open("./GUI/users.json", "w") as f:
            json.dump(users, f)

        # tk.messagebox.showinfo("Success", "User created successfully.")

    def sign_in(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            # tk.messagebox.showerror("Error", "Username and password fields are required.")
            return

        if not os.path.exists("./GUI/users.json"):
            # tk.messagebox.showerror("Error", "No users found. Please sign up first.")
            return

        with open("./GUI/users.json", "r") as f:
            users = json.load(f)

        if username not in users or users[username]["password"] != password:
            # tk.messagebox.showerror("Error", "Invalid username or password.")
            return

        self.show_main_window()

    def show_main_window(self):
        self.master.withdraw()
        main_window = tk.Toplevel(self.master)
        main_window.geometry(f"{self.width}x{self.height}+{int((self.screen_width-self.width)/2)}+{int((self.screen_height-self.height)/2)}")
        main_window.title("Eventim Ticket Reservation")
        main_window.resizable(True, True)

        self.event_label = tk.Label(main_window, text="Event:")
        self.event_label.grid(row=0, column=0)
        self.event_entry = tk.Entry(main_window)
        self.event_entry.grid(row=0, column=1)

        self.date_label = tk.Label(main_window, text="Date:")
        self.date_label.grid(row=1, column=0)
        self.date_entry = tk.Entry(main_window)
        self.date_entry.grid(row=1, column=1)

        self.time_label = tk.Label(main_window, text="Time:")
        self.time_label.grid(row=2, column=0)
        self.time_entry = tk.Entry(main_window)
        self.time_entry.grid(row=2, column=1)

        self.tickets_label = tk.Label(main_window, text="Number of Tickets:")
        self.tickets_label.grid(row=3, column=0)
        self.tickets_entry = tk.Entry(main_window)
        self.tickets_entry.grid(row=3, column=1)

        self.submit_button = tk.Button(main_window, text="Submit", command=self.submit)
        self.submit_button.grid(row=4, columnspan=2)

        main_window.protocol("WM_DELETE_WINDOW", self.close_main_window)

    def submit(self):
        event = self.event_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        tickets = self.tickets_entry.get()

        if not event or not date or not time or not tickets:
            # tk.messagebox.showerror("Error", "All fields are required.")
            return

        try:
            tickets = int(tickets)
            if tickets <= 0:
                raise ValueError
        except ValueError:
            # tk.messagebox.showerror("Error", "Invalid number of tickets.")
            return

        with open("./GUI/tickets.txt", "a") as f:
            f.write(f"{event}, {date}, {time}, {tickets}\n")

        # tk.messagebox.showinfo("Success", "Tickets reserved successfully.")

    def close_main_window(self):
        # if # tk.messagebox.showerror("Exit", "Are you sure you want to exit?"):
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    ticket_reservation_gui = TicketReservationGUI(root)
    root.mainloop()
