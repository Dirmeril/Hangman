import customtkinter as ctk
import play
import sys
import english_words
import random

class App:
    level: str = 'a'
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry('420x220')
        self.master.resizable(False, False)
        self.master.title('The Hangman')
        self.toplevel_window = None
        self.menu: str = '''HANGMAN GAME
Guess the password by guessing the letters in the password.
The password is a single word.
In game if you want return to the menu type \"pass\" '''

        self.label = ctk.CTkLabel(self.master, text=self.menu, font=('Helvetica bold', 15), justify='center')
        self.label.place(relx=0.5, rely=0.2, anchor='center')

        #Button start and exit
        self.button_start = ctk.CTkButton(self.master,text='Start', command=self.start, corner_radius=10)
        self.button_start.place(relx=0.2, rely=0.5, anchor='center')
        self.button_exit = ctk.CTkButton(self.master,text='Exit', command=self.exit, corner_radius=10)
        self.button_exit.place(relx=0.2, rely=0.8, anchor='center')
        self.optionmenu = ctk.CTkOptionMenu(self.master, values=["Easy", "Medium", "Hard"], corner_radius=10, anchor='center', command=self.optionmenu_callback)
        self.optionmenu.place(relx=0.2, rely=0.65, anchor='center')
        self.optionmenu.set("Choose level")

    def optionmenu_callback(self, level):
        App.level = level

    def exit(self):
        sys.exit(0)
    def start(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            # play.lvl = App.level
            pack_of_words = {"Easy": selection_words_easy, "Medium": selection_words_medium, "Hard": selection_words_hard}
            play.word = pack_of_words.get(App.level)[random.randrange(0, len(pack_of_words.get(App.level)))]
            attempts = {"Easy": 5, "Medium": 6, "Hard": 7}
            play.attempts = attempts.get(App.level)
            self.master.withdraw()
            self.toplevel_window = play.ToplevelWindow()  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it



if __name__ == '__main__':
    selection_words_easy = []
    selection_words_medium = []
    selection_words_hard = []
    words = english_words.get_english_words_set(['web2'], lower=True)
    list_of_words = list(sorted(words))
    #Create lists of words depends of difficult
    for i in list_of_words:
        if len(i) > 3 and len(i) < 6:
            selection_words_easy.append(i)

    for i in list_of_words:
        if len(i) > 5 and len(i) < 9:
            selection_words_medium.append(i)

    for i in list_of_words:
        if len(i) > 8:
            selection_words_hard.append(i)


    app = ctk.CTk()
    gui = App(master=app)
    app.mainloop()