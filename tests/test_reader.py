from hangman import reader


def test_check():
    name = 'kakashka.dat'
    with open(name, w) as kakashka:
        kakashka.write('kek')

    assert reader(name) == ['kek']
