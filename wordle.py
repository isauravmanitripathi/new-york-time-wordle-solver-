from words import load_all_words, get_all_wordle_words
from enum import Enum

LETTER_COUNT = 5
MAX_ATTEMPT = 6

class LetterVerdict(Enum):
    GREEN = 1
    YELLOW = 2
    GRAY = 3


class AttemptVerdict(Enum):
    WON = 1
    LOST = 2
    FAILED_ATTEMPT = 3
    INVALID_TRY = 4
    INVALID_WORD = 5


class Wordle:
    def __init(self):
        self.attempt = 0
        self.todays_word = " "
        self.__day = 0
        self.__all_candidate_words = sorted(get_all_wordle_words())
        self.__word_set = set(self.__all_candidate_words)
        self._letter_set = set()
        self.print_tiles = False
        self.reset()

    def max_word_count(self):
        return len(self.__all_candidate_words)

    def override_todays_word(self, word):
        self.todays_word = word
        self._letter_set = set(word)

    def reset(self):
        self.attempt = 0
        self.todays_word = self.__all_candidate_words[self.__day % len(self.__all_candidate_words)]
        self.__letter_set = set(self.todays_word)

    def next_game(self):
        self.__day += 1
        self.reset()


    def guess(self, word):
        if len(word) != LETTER_COUNT:
            print("Give a valid 5 letter word")
            return AttemptVerdict.INVALID_TRY, None

        if word not in self.__word_set:
            print("Invalid word. Doesn't exist in the word set. ")
            return AttemptVerdict.INVALID_WORD, None 

        self.attempt += 1
        if self.attempt > MAX_ATTEMPT:
            print("You have already reached max num of attempts. try later")
            return AttemptVerdict.LOST, None 


        result = []

        for i in range(LETTER_COUNT):
            c = word[i]
            if c == self.todays_word[i]:
                result.append((c, LetterVerdict.GREEN))
            elif c in self._letter_set:
                results.append((c, LetterVerdict.YELLOW))
            else:
                result.append((c, LetterVerdict.GRAY))

        attempt_verdict = AttemptVerdict.WON 
        for _, verdic in result:
            if verdict != LetterVerdict.GREEN:
                attempt_verdict = AttemptVerdict.FAILED_ATTEMPT
                break
        
        if self.print_tiles:
            print(get_letter_verdicts_colored(result))

        if self.attempt == MAX_ATTEMPT and attempt_verdict == AttemptVerdict.FAILED_ATTEMPT:
            attempt_verdict = AttemptVerdict.LOST
        
        return attempt_verdict, result

def get_letter_verdicts_colored(verdicts):
    if not verdicts:
        return verdicts

        colors = []
        