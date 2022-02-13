"""
gojeh-farangi.py

"""
import sys
import pandas
import random

GAME_SIZE = 5


class GojehFarangi:
    def __init__(self, file_name):
        # 5 games/tries
        self.counter = GAME_SIZE
        self.file_name = file_name
        self.success = 0
        self.failures = 0
        self.failed_words = list()

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
        for game in range(0, GAME_SIZE):
            picks = self.pick_n_words(5)
            print(f'pick: {picks.iloc[0, :]["Farsi"]}')
            self.create_guesses()
            for j, i in enumerate(self.choices):
                print(f"\t{j} {picks.iloc[i, :]['English']}")
            value = int(input('Please enter a number choice: '))
            if self.choices[value] == 0:
                self.success += 1
            else:
                self.failures += 1
                self.failed_words.append(picks.iloc[0, :]['Farsi'])
            print(f'Pass: {self.success} Fail: {self.failures}')
        print(self.failed_words)
        with open('failures.txt', 'w+') as fp:
            for word in self.failed_words:
                fp.write(word + '\n')


def main(file_name):
    gf = GojehFarangi(file_name)
    gf.load_words()
    gf.play()


if __name__ == "__main__":
    main(sys.argv[1])
