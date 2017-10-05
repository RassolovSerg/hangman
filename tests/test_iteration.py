import sys
import StringIO
from hangman import Game
from mock import patch


def test_iteration():
    # test_1
    captured_output = StringIO.StringIO()
    sys.stdout = captured_output
    new_game = Game()
    with patch('hangman.letter_input') as perm_mock:
        perm_mock.return_value = 'e'
        missed, guesses = new_game.iteration(('kek', 3, set(['k'])))
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == 'Hit!\n\nThe word: kek\n\nYou won!\n'
    assert missed == 3
    assert guesses == set(['k', 'e'])
    # test_2
    captured_output = StringIO.StringIO()
    sys.stdout = captured_output
    new_game = Game()
    with patch('hangman.letter_input') as perm_mock:
        perm_mock.return_value = 'e'
        missed, guesses = new_game.iteration(('lol', 4, set(['k'])))
    sys.stdout = sys.__stdout__
    printed_str = 'Missed, mistake 5 out of 5 \n\nThe word: ***\n\nYou lost!\n'
    assert captured_output.getvalue() == printed_str
    assert missed == 5
    assert guesses == set(['k', 'e'])
