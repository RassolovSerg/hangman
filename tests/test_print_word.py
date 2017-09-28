from hangman import print_word
import sys

def test_print_word():
    sys.stdout = open('file', 'w')
    print_word('nano', set(['n','o']))
    sys.stdout.close()
    with open('file', 'r') as ff:
        data = ff.read()
    assert data == 'The word: n*no\n\n'
