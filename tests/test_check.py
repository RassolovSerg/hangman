from hangman import check


def test_check():
    assert check('hello', set(['h', 'e', 'l', 'o']))
    assert not check('hello', set(['h', 'e', 'l']))
