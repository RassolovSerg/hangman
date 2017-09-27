from hangman import check


def test_check():
    assert check('hello', set('h','e','l','o')) == True
