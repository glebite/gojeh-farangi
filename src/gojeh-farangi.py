"""
gojeh-farangi.py

"""
import sys
import pandas
import random
import getopt

GAME_SIZE = 5
NUMBER_OF_GAMES = 5


class GojehFarangi:
    """
    """
    def __init__(self, file_name, game_size=NUMBER_OF_GAMES):
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
        self.choices = [i for i in range(0, GAME_SIZE)]
        random.shuffle(self.choices)
        return self.choices

    def play(self):
        """play - play the game: wheeee!

        Essentially, loops through NUMBER_OF_GAMES and presents
        the user with a words written in Farsi, and 5 choices to
        pick from with the English definition.  The user picks from
        0 to 4 and if there is a match, the player scores a success.

        In the case of a failure, the list of failed words gets stored
        in a failures.txt file to be consumed in future implementations.

        params:
        n/a

        returns:
        n/a

        raises:
        n/a
        """
        self.load_words()
        for game in range(0, GAME_SIZE):
            picks = self.pick_n_words(GAME_SIZE)
            print(f'Game: {game}')
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


def usage():
    print("How to use this tool...")


def main():
    """main - takes the brunt of fun from the if dunder name

    TODO: IOU more checking, change to getopts?

    params:
    args - list of parameters originating from sys.argv

    returns:
    n/a

    raises:
    n/a
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   "h",
                                   ["help", "file=", "game_size="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    file_name = None
    number_of_games = NUMBER_OF_GAMES
    for o, a in opts:
        print(o, a)
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("--file"):
            file_name = a
        elif o in ("--game_size"):
            number_of_games = a

    gf = GojehFarangi(file_name, number_of_games)
    gf.load_words()
    gf.play()


if __name__ == "__main__":
    main()
