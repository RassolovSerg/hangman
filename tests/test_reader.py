import os
from hangman import reader


def test_reader():
    name = 'kakashka.tmp'
    with open(name, 'w') as kakashka:
        kakashka.write('kek' + '\n')

    assert reader(name) == ['kek']
    os.remove(name)
