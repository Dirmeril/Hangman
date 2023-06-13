import customtkinter as ctk
import string
import random
import main

class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, master, attempts, word):
        super().__init__(master)
        self.geometry("400x600")
        self.resizable(1, 1)
        self.columnconfigure(0, weight=1) #grid_
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=3)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        #Import data from main
        self.attempts = attempts
        self.word = word
        self.used_letter = []
        self.user_word = []
        for _ in self.word:
            self.user_word.append('_')

        #Create_text
        self.text = ctk.CTkLabel(self, text='The password consists of {} characters\nYou have {} attempts'.format(len(word), (attempts)))
        self.text.grid(row=0, column=0, sticky='ew')

        #Create_visiual_hangman


        #Create_passoword
        self.label = ctk.CTkLabel(self, text=''.join(self.user_word))
        self.label.grid(row=1, column=0)

        # Create pool to input user_letter and Communicaton
        self.entry = ctk.CTkEntry(self, placeholder_text="Guess letter", corner_radius=10)
        self.entry.grid(row=2, column=0)
        self.label_entry = ctk.CTkLabel(self, text='')
        self.label_entry.grid(row=3, column=0)
        self.b_enter = ctk.CTkButton(self, text='Enter', command=self.user_letter, corner_radius=10)
        self.b_enter.grid(row=4, column=0, sticky="ew")

    def user_letter(self):
        self.u_letter = self.entry.get().lower()
        self.entry.delete(first_index=0, last_index=len(self.u_letter))
        if self.u_letter == 'space':
            u_letter = ' '
        # elif u_letter == 'pass':
        #     # info()
        elif self.u_letter in string.whitespace:
            self.label_entry.configure(text="Don't use tab or space")
        elif self.u_letter in string.punctuation:
            self.label_entry.configure(text="Don't use punctuation!")
        elif self.u_letter in string.digits:
            self.label_entry.configure(text="Don't use digits")
        elif len(self.u_letter) != 1:
            self.label_entry.configure(text='Entry only one letter! Too many symbols: {}'.format(self.u_letter))
        elif self.u_letter in self.used_letter:
            self.label_entry.configure(text="You've used that letter. Try again!")
        else:
            self.used_letter.append(self.u_letter)
            self.found_letter = self.find_indexes(self.word, self.u_letter)
            self.hangman(self.found_letter)



    def find_indexes(self, word, letter):
        indexes = []
        for index, letter_in_word in enumerate(word):
            if letter == letter_in_word:
                indexes.append(index)
        return indexes
    def close_second_window(self):
        self.destroy()
        self.master.deiconify()
    def on_close(self):
        self.destroy()
        self.master.deiconify()

    def hangman(self, found_letter):
        if len(found_letter) == 0:
            self.attempts -= 1
            self.label_entry.configure(text="Wrong letter")
            self.text.configure(text='The password consists of {} characters\nYou have {} attempts'.format(len(self.word), (self.attempts)))
            if self.attempts == 0:
                self.text.configure(text="End game! You've lost all attempts\nThe passwords was: {}".format(self.word))
                self.b_enter.configure(command=self.close_second_window, text="Close window")
                # info()
                # break
        else:
            for index in found_letter:
                self.label_entry.configure(text="Good shot!")
                self.user_word[index] = self.u_letter
                self.label.configure(text=''.join(self.user_word))
            if ''.join(self.user_word) == self.word:
                print("You guessed the password. Congratulations".upper())
                print('Your password:', ''.join(self.user_word))
                input('Press enter to end program')
                # info()
                # break