import sys
import StringIO
from hangman import Game
import hangman
from mock import patch


def test_iteration():
    captured_output = StringIO.StringIO()
    sys.stdout = captured_output
    new_game = Game()
    with patch('hangman.letter_input') as perm_mock:
        perm_mock.return_value = 'e'
        missed, guesses = new_game.iteration(('kek', 3, set(['k'])))
        print missed, guesses, captured_output.getvalue()
    # body of test
    sys.stdout = sys.__stdout__
    # assert captured_output.getvalue() ==
