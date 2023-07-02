import tkinter as tk
import tkinter.messagebox as messagebox
# from login_page import LoginPage
# from registration_page import RegistrationPage
# from event_page import EventPage
from preferences import PeferencesPage

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Eventim Ticket")
        self.geometry("650x450")
        
        # self.login_page = LoginPage(self, self.show_registration)
        # self.registration_page = RegistrationPage(self, self.show_login)
        # self.event_page = EventPage(self, self.show_event_page)
        self.preferences_page = PeferencesPage(self, self.showPreferences)
        
        # self.show_login()
        self.showPreferences()

    def showPreferences(self):
        # self.registration_page.grid_remove()
        self.preferences_page.grid()
        
    # def show_login(self):
    #     self.registration_page.grid_remove()
    #     self.login_page.grid()

    # def show_registration(self):
    #     self.login_page.grid_remove()
    #     self.registration_page.grid()
        
    # def show_event_page(self):
    #     self.login_page.grid_remove()
    #     self.event_page.grid()

    def showInfoMessage(self, title, message):
        messagebox.showinfo(title, message)

    def showErrorMessage(self, title, message):
        messagebox.showerror(title, message)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
