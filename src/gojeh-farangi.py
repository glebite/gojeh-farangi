"""
gojeh-farangi.py

"""
import sys
import pandas
import random

GAME_SIZE = 5


class GojehFarangi:
    """
    """
    def __init__(self, file_name, game_size=GAME_SIZE):
        """__init__ - constructor like usual

        params:
        file_name - string - file containing CSV with
                             Farsi word, pronounciation, and English
        game_size - int    - number of rounds to play

        returns:
        n/a

        raises:
        n/a
        """
        self.counter = int(game_size)
        self.file_name = file_name
        self.success = 0
        self.failures = 0
        self.failed_words = list()

    def load_words(self):
        """load_words - read in from the file 

        TODO: IOU file existence checking and errors
        """
        self.words = pandas.read_excel(self.file_name)

    def pick_n_words(self, word_count):
        """pick_n_words - select a random selection of words

        params:
        word_count - int - a count of words to pick_n_words

        returns:
        self.picks - list - list of random words from the file

        raises:
        n/a
        """
        self.picks = self.words.sample(word_count)
        return self.picks

    def create_guesses(self):
        """create_guesses - take the choices and randomize them

        params:

        returns:

        raises:

        """
        self.choices = [i for i in range(0, self.counter)]
        random.shuffle(self.choices)
        return self.choices

    def play(self):
        """
        """
        self.load_words()
        for game in range(0, self.counter):
            picks = self.pick_n_words(5)
            print(f'\npick: {picks.iloc[0, :]["Farsi"]}'
                  f' => {picks.iloc[0, :]["Pronunciation"]}')
            self.create_guesses()
            for j, i in enumerate(self.choices):
                print(f"\t{j} {picks.iloc[i, :]['English']}")
            value = int(input('Please enter a number choice: '))
            if self.choices[value] == 0:
                self.success += 1
            else:
                self.failures += 1
                print(f'Should have been: {picks.iloc[0]["English"]}')
                self.failed_words.append(picks.iloc[0, :]['Farsi'])
            print(f'Pass: {self.success} Fail: {self.failures}')
        print(self.failed_words)
        with open('failures.txt', 'a') as fp:
            for word in self.failed_words:
                fp.write(word + '\n')


def main(args):
    """
    """
    print(args)
    gf = GojehFarangi(args[1], args[2])
    gf.load_words()
    gf.play()


if __name__ == "__main__":
    main(sys.argv)
