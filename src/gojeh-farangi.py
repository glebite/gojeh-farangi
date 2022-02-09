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
        picks = self.words.sample(word_count)
        return picks


def main(file_name):
    gf = GojehFarangi(file_name)
    gf.load_words()
    picks = gf.pick_n_words(5).head()
    print(picks.iloc[0])
    for row in picks.iloc[1:]:
        print(row)


if __name__ == "__main__":
    main(sys.argv[1])
