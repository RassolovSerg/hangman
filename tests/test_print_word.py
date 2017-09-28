from hangman import print_word
import sys


def test_print_word():
    sys.stdout = open('file.tmp', 'w')
    print_word('nano', set(['n', 'o']))
    sys.stdout.close()
    with open('file.tmp', 'r') as file_output:
        data = file_output.read()
    assert data == 'The word: n*no\n\n'
