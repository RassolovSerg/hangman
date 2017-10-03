from hangman import initial


def test_initial():
    word, mistakes, missed, guesses, boolean = initial()
    assert word in ['kek', 'hello', 'bro', 'lol', 'matan']
    assert mistakes == 5
    assert missed == 0
    assert guesses == set()
    assert boolean
