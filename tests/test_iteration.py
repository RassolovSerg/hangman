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
        new_game.word = 'kek'
        new_game.missed = 3
        new_game.guesses = set(['k'])
        new_game.iteration()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == 'Hit!\n\nThe word: kek\n\nYou won!\n'
    assert new_game.missed == 3
    assert new_game.guesses == set(['k', 'e'])
    # test_2
    captured_output = StringIO.StringIO()
    sys.stdout = captured_output
    new_game = Game()
    with patch('hangman.letter_input') as perm_mock:
        perm_mock.return_value = 'e'
        new_game.word = 'lol'
        new_game.missed = 4
        new_game.guesses = set(['k'])
        new_game.iteration()
    sys.stdout = sys.__stdout__
    printed_str = 'Missed, mistake 5 out of 5 \n\nThe word: ***\n\nYou lost!\n'
    assert captured_output.getvalue() == printed_str
    assert new_game.missed == 5
    assert new_game.guesses == set(['k', 'e'])
