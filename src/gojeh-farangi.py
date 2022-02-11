"""
gojeh-farangi.py

"""
import sys
import pandas
import random


class GojehFarangi:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_words(self):
        self.words = pandas.read_excel(self.file_name)

    def pick_n_words(self, word_count):
        self.picks = self.words.sample(word_count)
        return self.picks

    def output_guesses(self):
        choices = [i for i in range(0, 5)]
        random.shuffle(choices)
        for i, choice in enumerate(choices):
            print(f'{i} {self.picks.iloc[choice, :]["English"]}')


def main(file_name):
    gf = GojehFarangi(file_name)
    gf.load_words()
    picks = gf.pick_n_words(5)
    print(picks.iloc[0, :]['Farsi'])
    gf.output_guesses()


if __name__ == "__main__":
    main(sys.argv[1])
