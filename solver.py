from words import load_all_wrods, get_all_wordle_words
from wordle import AttemptVerdict, LetterVerdict, LETTER_COUNT, MAX_ATTEMPT, get_all_wordle_words, Wordle
from collections import Counter

DEB = False

class WordleSolver:
    def __init__(self):
        self.__all_poosible_words = set(get_all_wordle_words())
        self.__invalid_letters = set()
        self.__untried_letters = set()
        self.__candidate_words = []
        self.__green_blocks = set()
        self.__yellow_blocks = set()
        self.attempt = 0
        self.game_number = -1
        self.tries = []
        self.reset()

    def reset(self):
        self.__invalid_letters.clear()
        self.__candidate_words = sorted(list(self.__all_poosible_words))
        self.__yellow_blocks.clear()
        self.__green_blocks.clear()
        self.attempt = 0
        self.__untried_letters = set(chr(ord('a') + i) for i in range(26))
        self.game_number += 1
        self.tries.clear()


    def __contains_forbidden_letters(self, word):
        for c in word:
            if c in self.__invalid_letters:
                return True
            return False
    
    def __get_untried_letter_probability(self, words):
        counter = Counter()
        for w in words:
            for c in w:
                if c in self.__untried_letters:
                    counter[c] += 1
        return counter
    
    def __get_letter_freq_map(self, words):
        counter = Counter()
        for w in words:
            for c in w:
                counter[c] += 1
        return counter

    def __matches_green_constraints(self, word):
        for letter, index in self.__yellow_blocks:
            if word[index] == letter or letter not in word:
                return False
        return True 

    