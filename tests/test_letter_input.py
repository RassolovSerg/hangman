import unittest
import __builtin__
import mock
from hangman import letter_input


class Test(unittest.TestCase):
    @mock.patch.object(__builtin__, 'raw_input')
    def test_stuff(self, mock_raw_input):
        mock_raw_input.return_value = 7
        self.assertEqual(letter_input(), 7)
