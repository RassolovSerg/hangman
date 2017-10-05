from hangman import command_line
from mock import patch


def test_command_line():

    with patch('hangman.main') as perm_mock:
        perm_mock.return_value = True
        result = command_line.main()
    assert result
