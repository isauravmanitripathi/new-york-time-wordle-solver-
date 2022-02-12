from wordle import AttemptVerdict, LetterVerdict, LETTER_COUNT, Wordle
from solver import WordleSolver

class Rewordle(Wordle):
    def __init__(self):
        super().__init__()
        self.attempt = 0

    def __translate_input(self, guess: str, game_verdict: str):
        if game_verdict.lower() == "invalid":
            return AttemptVerdict.INVALID_WORD, None
        if len(game_verdict) > LETTER_COUNT:
            print("Give a valid string")
            return None 
        elif not re.match("[gyb]+", game_verdict.lower()):
            print("Give a valid string containg only GYB")
            return None 

        ret = []

        for i in range(LETTER_COUNT):
            c = game_verdict[i]
            if c == 'g':
                ret.append((guess[i], LetterVerdict.GREEN))
            if c =='y':
                ret.append((guess[i], LetterVerdict.YELLOW))
            if c == 'b':
                ret.append((guess[i], LetterVerdict.GRAY))

        for r in ret:
            if r[1] != LetterVerdict.GREEN:
                return AttemptVerdict.FAILED_ATTEMPT, ret
        
        return AttemptVerdict.WON, ret

    
    def guess(self, word: str):
        print(f"Try: {word}")

        while True:
            game_verdict = input("what did the game say: ")
            translated_message = self.__translate_input(word, game_verdict)
            if translated_message is None:
                continue
            else:
                return translated_message


    def play(self, solver: WordleSolver):
        solver.reset()
        solver.solve(self)

if __name__ == '__main__':
    rewordle = Rewordle()
    rewordle.play(WordleSolver())        