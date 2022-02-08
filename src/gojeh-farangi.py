"""
gojeh-farangi.py

"""
import sys
import pandas


class GojehFarangi:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_words(self):
        self.words = pandas.read_excel(self.file_name)
        print(self.words.count())


def main(file_name):
    gf = GojehFarangi(file_name)
    gf.load_words()


if __name__ == "__main__":
    main(sys.argv[1])
