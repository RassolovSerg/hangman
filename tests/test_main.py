from hangman import main, Game
from mock import patch


def test_main():

    def new_play(self):
        self.boolean = False

    with patch.object(Game, 'play', new_play):
        result = main()
    assert result
