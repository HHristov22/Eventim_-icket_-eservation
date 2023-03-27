import tkinter as tk
import subprocess

class TicketReservationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Eventim Ticket Reservation")

        self.event_label = tk.Label(master, text="Event:")
        self.event_label.grid(row=0, column=0)
        self.event_entry = tk.Entry(master)
        self.event_entry.grid(row=0, column=1)

        self.date_label = tk.Label(master, text="Date:")
        self.date_label.grid(row=1, column=0)
        self.date_entry = tk.Entry(master)
        self.date_entry.grid(row=1, column=1)

        self.quantity_label = tk.Label(master, text="Quantity:")
        self.quantity_label.grid(row=2, column=0)
        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.grid(row=2, column=1)

        self.output_text = tk.Text(master, height=10, width=50)
        self.output_text.grid(row=3, columnspan=2)

        self.reserve_button = tk.Button(master, text="Reserve Tickets", command=self.reserve_tickets)
        self.reserve_button.grid(row=4, columnspan=2)

    def reserve_tickets(self):
        event = self.event_entry.get()
        date = self.date_entry.get()
        quantity = self.quantity_entry.get()

        command = f"python main.py --event='{event}' --date='{date}' --quantity='{quantity}'"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()

        if error:
            self.output_text.insert(tk.END, error.decode())
        else:
            self.output_text.insert(tk.END, output.decode())
            
    def show_main_window(self):
        self.master.withdraw()  # hide the login window
        main_window = tk.Toplevel(self.master)
        main_window.title("Eventim Ticket Reservation")
        main_window.geometry("800x450")

        # set window size and resolution
        screen_width = main_window.winfo_screenwidth()
        screen_height = main_window.winfo_screenheight()
        max_width = int(screen_width * 0.8)
        max_height = int(screen_height * 0.8)
        width = min(max_width, int(max_height * 16 / 9))
        height = min(max_height, int(max_width * 9 / 16))
        x = int((screen_width - width) / 2)
        y = int((screen_height - height) / 2)
        main_window.geometry(f"{width}x{height}+{x}+{y}")

        # add user name label
        user_name = self.username_entry.get()
        self.user_name_label = tk.Label(main_window, text=f"Welcome, {user_name}!", font=("Arial", 12))
        self.user_name_label.place(x=width-200, y=20)

        # add ticket reservation form
        self.event_label = tk.Label(main_window, text="Event Name:")
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


root = tk.Tk()
my_gui = TicketReservationGUI(root)
root.mainloop()
