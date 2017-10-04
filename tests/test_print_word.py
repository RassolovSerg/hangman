import sys
import StringIO
from hangman import print_word


def test_print_word():
    captured_Output = StringIO.StringIO()
    sys.stdout = captured_Output
    print_word('nano', set(['n', 'o']))
    sys.stdout = sys.__stdout__
    assert captured_Output.getvalue() == 'The word: n*no\n\n'
