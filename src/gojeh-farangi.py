"""
gojeh-farangi.py

"""
import sys
import pandas
import random


class GojehFarangi:
    def __init__(self, file_name):
        # 5 games/tries
        self.counter = 5
        self.file_name = file_name

    def load_words(self):
        self.words = pandas.read_excel(self.file_name)

    def pick_n_words(self, word_count):
        self.picks = self.words.sample(word_count)
        return self.picks

    def create_guesses(self):
        self.choices = [i for i in range(0, 5)]
        random.shuffle(self.choices)
        return self.choices

    def play(self):
        self.load_words()
        picks = self.pick_n_words(5)
        print(f'pick: {picks.iloc[0, :]["Farsi"]}')
        self.create_guesses()
        for i in self.choices:
            print(i, picks.iloc[i, :]['English'], picks.iloc[i, :]['Farsi'])


def main(file_name):
    gf = GojehFarangi(file_name)
    gf.load_words()
    picks = gf.pick_n_words(5)
    gf.create_guesses()
    gf.play()


if __name__ == "__main__":
    main(sys.argv[1])
