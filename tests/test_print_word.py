import sys
import StringIO
from hangman import print_word


def test_print_word():
    captured_output = StringIO.StringIO()
    sys.stdout = captured_output
    print_word('nano', set(['n', 'o']))
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == 'The word: n*no\n\n'
