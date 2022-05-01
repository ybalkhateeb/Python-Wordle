"""
Main module for the  Wordle.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR


def wordle():

    # choose a word from a list
    chosen_word = FIVE_LETTER_WORDS[random.randint(0, 4999)]

    def binary_search(arr, word):

        left = 0
        right = len(arr) - 1

        while right >= left:
            mid = (left+right) // 2
            if arr[mid] == word:
                return mid
            elif arr[mid] > word:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def enter_action(s):
        r = gw.get_current_row()    # row number
        s = s.lower()   # User word
        IndexOfUserWord = binary_search(FIVE_LETTER_WORDS, s)     # check if word in a list

        if IndexOfUserWord != -1:
            if s == chosen_word:
                for i in range(N_COLS):
                    gw.set_square_color(r, i, CORRECT_COLOR)
                    gw.set_key_color(s[i].upper(), CORRECT_COLOR)

                gw.show_message("nice, it is the correct word")

                return

            # Color the correct letters ( boxes )
            for j in range(N_COLS):
                if s[j] == chosen_word[j]:
                    gw.set_square_color(r, j, CORRECT_COLOR)
                    gw.set_key_color(s[j].upper(), CORRECT_COLOR)

            # Color the present and missing letters ( boxes )
            for j in range(N_COLS):
                if gw.get_square_color(r, j) != CORRECT_COLOR:
                    if s[j] in chosen_word:
                        gw.set_square_color(r, j, PRESENT_COLOR)
                        gw.set_key_color(s[j].upper(), PRESENT_COLOR)
                    else:
                        gw.set_square_color(r, j, MISSING_COLOR)
                        gw.set_key_color(s[j].upper(), MISSING_COLOR)

            gw.set_current_row(r + 1)

        else:
            gw.show_message('the word is not in the list')

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)


if __name__ == "__main__":
    wordle()
