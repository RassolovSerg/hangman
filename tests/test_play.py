import sys
import StringIO
from hangman import Game
from mock import patch


def test_play():

    def new_iteration(self):
        self.boolean = False

    captured_output = StringIO.StringIO()
    sys.stdout = captured_output
    with patch.object(Game, 'iteration', new_iteration):
        new_game = Game()
        new_game.word = 'hello'
        new_game.play()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == 'The word: *****\n\nGuess a letter:\n'
    assert not new_game.boolean
