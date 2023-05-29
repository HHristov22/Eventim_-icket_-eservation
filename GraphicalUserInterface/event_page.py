import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from json_handler import write_event_data

class EventPage(tk.Frame):
    def __init__(self, parent, back_callback):
        super().__init__(parent)
        self.parent = parent
        self.back_callback = back_callback

        self.event_var = tk.StringVar()
        self.start_date_var = tk.StringVar()
        self.end_date_var = tk.StringVar()
        self.ticket_var = tk.StringVar()

        self.event_dropdown = tk.OptionMenu(self, self.event_var, "")
        self.event_label = tk.Label(self,text="Event: ")
        self.start_date_entry = tk.Entry(self, textvariable=self.start_date_var)
        self.end_date_entry = tk.Entry(self, textvariable=self.end_date_var)
        self.ticket_dropdown = tk.OptionMenu(self, self.ticket_var, "")
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_data)
        self.back_button = tk.Button(self, text="Back", command=self.back_callback)

        self.event_dropdown.pack(pady=2)
        self.event_label.pack(pady=2)
        self.start_date_entry.pack(padx=150,pady=2)
        self.end_date_entry.pack(pady=2)
        self.ticket_dropdown.pack(pady=2)
        self.submit_button.pack(pady=2)
        self.back_button.pack(pady=2)

        self.populate_event_dropdown()
        self.populate_ticket_dropdown()
    
    def populate_event_dropdown(self):
        # Placeholder implementation to populate the event dropdown
        events = ["Event 1", "Event 2", "Event 3"]
        self.event_var.set(events[0])  # Set default value
        menu = self.event_dropdown["menu"]
        menu.delete(0, "end")
        for event in events:
            menu.add_command(label=event, command=lambda value=event: self.update_selected_event(value))

    def update_selected_event(self, event):
        self.event_label.config(text="Event: " + event)

    def populate_ticket_dropdown(self):
        # Placeholder implementation to populate the ticket dropdown
        tickets = [1, 2, 3, 4, 5, 6, 7, 8]
        self.ticket_var.set(tickets[0])  # Set default value
        menu = self.ticket_dropdown["menu"]
        menu.delete(0, "end")
        for ticket in tickets:
            menu.add_command(label=ticket, command=lambda value=ticket: self.ticket_var.set(value))

    def submit_data(self):
        event = self.event_var.get()
        start_date = self.start_date_var.get()
        end_date = self.end_date_var.get()
        ticket = self.ticket_var.get()

        # Validate the input data
        if event and start_date and end_date and ticket:
            # Convert start_date and end_date to datetime objects
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                end_date = datetime.strptime(end_date, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Invalid Date", "Please enter dates in the format YYYY-MM-DD")
                return

            # Check if start_date is before end_date
            if start_date > end_date:
                messagebox.showerror("Invalid Date", "Start date cannot be after end date")
                return

            # Prepare the data to be saved
            data = {
                "event": event,
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "ticket": ticket
            }

            # Save the data to a JSON file
            write_event_data(data)

            messagebox.showinfo("Data Saved", "Event data has been saved successfully!")
        else:
            messagebox.showerror("Missing Fields", "Please fill in all the fields")

        # Clear the input fields
        self.event_var.set("")
        self.start_date_var.set("")
        self.end_date_var.set("")
        self.ticket_var.set("")

