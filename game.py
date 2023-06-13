# import sys
# import string
# import random
# import english_words
#
#
# ###def
# def info():
#     print()
#     print('----'*10)
#     print('''\t\t\tHANGMAN GAME
# Guess the password by guessing the letters in the password.
# The password is a single word.
# In game if you want return to the menu type \"pass\" ''')
#
# def statement_of_game():
#     print()
#     print('*********' * 3)
#     print('password'.upper(), ''.join(user_word))
#     print("Remaining attempts".upper(), attempts)
#     print("used symbols:".upper(), sorted(set(user_letter)))
#     print('*********' * 3)
#     print()
#
# def find_indexes(word, letter):
#     indexes = []
#     for index, letter_in_word in enumerate(word):
#         if letter == letter_in_word:
#             indexes.append(index)
#     return indexes
#
# def choose_level():
#     while True:
#         selection_words = []
#         words = english_words.get_english_words_set(['web2'], lower=True)
#         list_of_words = list(sorted(words))
#         print('---'*10)
#         print('''Choose word length
# 1 - less than six
# 2 - between six and eight
# 3 - greater than eight''')
#         level = input("Choose word length: ")
#         if level == '1':
#             for i in list_of_words:
#                 if len(i) > 3 and len(i) < 6:
#                     selection_words.append(i)
#             attempts = 5
#             break
#         elif level == '2':
#             for i in list_of_words:
#                 if len(i) > 5 and len(i) < 9:
#                     selection_words.append(i)
#             attempts = 6
#             break
#         elif level == '3':
#             for i in list_of_words:
#                 if len(i) > 8:
#                     selection_words.append(i)
#             attempts = 7
#             break
#         else:
#             print('Choose right number')
#
#     return selection_words[random.randrange(0,len(selection_words))], attempts
#
# ###GAME
# info()
# while True:
#     print("\t***MENU***")
#     print('''1 - New game\n2 - Exit''')
#     choose = input("Select: ")
#     if choose == '2':
#         sys.exit(0)
#     elif choose == '1':
#         word, attempts = choose_level()
#         user_letter = []
#         user_word = []
#         for _ in word:
#             user_word.append('_')
#         print()
#         print('The password consists of {} characters'.format(len(word)))
#         print('You have {} attempts'.format(attempts))
#         print('password'.upper(), ''.join(user_word))
#         while True:
#             letter = input('Enter letter: ').lower()
#             if letter == 'space':
#                 letter = ' '
#             elif letter == 'pass':
#                 info()
#                 break
#             elif letter in string.whitespace:
#                 print("Don't use tab or space")
#                 continue
#             elif letter in string.punctuation:
#                 print("Don't use punctuation!")
#                 continue
#             elif letter in string.digits:
#                 print("Don't use digits")
#                 continue
#             elif len(letter) != 1:
#                 print('Entry only one letter! Too many symbols:', letter)
#                 continue
#             elif letter in user_letter:
#                 print("You've used that letter. Try again!")
#                 continue
#
#             user_letter.append(letter)
#             found_letter = find_indexes(word,letter)
#
#             if len (found_letter) == 0:
#                 attempts -= 1
#                 print('Wrong letter')
#
#                 if attempts == 0:
#                     print("End game! You've lost all attempts")
#                     print('The passwords was: '+word)
#                     input('Press enter to end program')
#                     info()
#                     break
#             else:
#                 for index in found_letter:
#                     print("Good shot!")
#                     user_word[index] = letter
#                 if ''.join(user_word) == word:
#                     print("You guessed the password. Congratulations".upper())
#                     print('Your password:',''.join(user_word))
#                     input('Press enter to end program')
#                     info()
#                     break
#
#             statement_of_game()
#
#     else:
#         print("!Choose right number!")
#         print()