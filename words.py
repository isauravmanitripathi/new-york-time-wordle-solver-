def load_all_words(letter_count = 5):
    with open("/Users/sauravtripathi/Downloads/wordle-solver/all_wordle_words.txt", "r") as word_file:
        return sorted([word.strip().lower() for word in word_file.readlines() if len(word.strip()) == letter_count])

def get_all_wordle_words():
    with open("all_wordle_words.txt", "r") as infile:
        return[line.strip() for line in infile.readlines()]