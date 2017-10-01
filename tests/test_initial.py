import os
from hangman import initial


def test_initial():
    name = 'dictionary.tmp'
    with open(name, 'w') as file_to_write:
        file_to_write.write('kakashka\n')
    word, mistakes, missed, guesses, boolean = initial(name)
    assert word == 'kakashka'
    assert mistakes == 5
    assert missed == 0
    assert guesses == set()
    assert boolean
    os.remove(name)
