from hangman import game
import unittest
import mock
import __builtin__

class Test(unittest.TestCase):
    @mock.patch.object(__builtin__, 'raw_input')
    def test_stuff(self, mock_raw_input):
        new_game = game()
        mock_raw_input.return_value = 7
        self.assertEqual(new_game.input(), 7)
