import customtkinter as ctk
import string
import random


class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs, ):
        super().__init__(*args, **kwargs)
        self.geometry("400x600")
        self.resizable(0, 0)
        self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)
        # self.rowconfigure(2, weight=1)
        # self.rowconfigure(3, weight=1)
        self.attempts = attempts
        self.word = word
        self.used_letter = []
        self.user_word = []
        for _ in word:
            self.user_word.append('_')
        #Create_text
        self.text = ctk.CTkLabel(self, text='The password consists of {} characters'.format(len(word)),)
        self.text.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

        #Create_passoword
        self.label = ctk.CTkLabel(self, text=''.join(self.user_word))
        self.label.grid(row=1, column=0, padx=20, pady=20)


        # Create pool to input user_letter
        self.entry = ctk.CTkEntry(self, placeholder_text="Guess letter", corner_radius=10)
        # self.entry.place(relx=0.5, rely=0.5, anchor="center")
        self.entry.grid(row=2, column=0, padx=20, pady=20)
        self.b_enter = ctk.CTkButton(self, text='Start', command=self.user_letter, corner_radius=10)
        # self.b_enter.place(relx=0.5, rely=0.65, anchor="center")
        self.b_enter.grid(row=3, column=0, padx=20, pady=20)

    def user_letter(self):
        u_letter = self.entry.get()
        self.entry.delete(first_index=0, last_index=len(u_letter))