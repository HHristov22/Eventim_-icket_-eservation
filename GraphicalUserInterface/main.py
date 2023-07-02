import tkinter as tk
import tkinter.messagebox as messagebox
from preferences import PeferencesPage

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Eventim Ticket")
        self.geometry("650x450")
        self.preferences_page = PeferencesPage(self, self.show_preferences)
        
        self.show_preferences()

    def show_preferences(self):
        self.preferences_page.grid()

    def showInfoMessage(self, title, message):
        messagebox.showinfo(title, message)

    def showErrorMessage(self, title, message):
        messagebox.showerror(title, message)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
