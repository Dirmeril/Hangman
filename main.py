import customtkinter as ctk
import game
import sys

class App:
    def __init__(self, master: ctk.CTk):
        self.n = None
        self.master = master
        self.master.geometry('500x700')
        self.master.resizable(False, False)
        self.master.title('The Hangman')
        self.toplevel_window = None
        self.menu: str = '''HANGMAN GAME
Guess the password by guessing the letters in the password.
The password is a single word.
In game if you want return to the menu type \"pass\" '''

        self.label = ctk.CTkLabel(self.master, text=self.menu, font=('Helvetica bold', 15))
        self.label.place(relx=0.5, rely=0.1, anchor='center')


        #Button start and exit
        self.button_start = ctk.CTkButton(self.master,text='Start', command=self.start, corner_radius=10)
        self.button_start.place(relx=0.3, rely=0.2, anchor='center')
        self.button_exit = ctk.CTkButton(self.master,text='Exit', command=self.exit, corner_radius=10)
        self.button_exit.place(relx=0.7, rely=0.2, anchor='center')

    def exit(self):
        sys.exit(0)
    def start(self):
        self.button_start.destroy()
        self.button_exit.destroy()
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow()  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(relx=0.5, rely=0.15)



if __name__ == '__main__':
    app = ctk.CTk()
    gui = App(master=app)
    app.mainloop()