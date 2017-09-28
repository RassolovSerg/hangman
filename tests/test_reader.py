from hangman import reader


def test_reader():
    name = 'kakashka.dat'
    with open(name, 'w') as kakashka:
        kakashka.write('kek' + '\n')

    assert reader(name) == ['kek']
