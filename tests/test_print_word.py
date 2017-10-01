import sys
import os
from hangman import print_word


def test_print_word():
    name = 'file.tmp'
    sys.stdout = open(name, 'w')
    print_word('nano', set(['n', 'o']))
    sys.stdout.close()
    with open(name, 'r') as file_output:
        data = file_output.read()
    assert data == 'The word: n*no\n\n'
    os.remove(name)
