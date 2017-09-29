from hangman import initial

def test_initial():
    with open('dictionary.tmp', 'w') as file_to_write:
        file_to_write.write('kakashka\n')
    word, mistakes, missed, guesses, boolean = initial('dictionary.tmp')
    assert word == 'kakashka'
    assert mistakes == 5
    assert missed == 0
    assert guesses == set()
    assert boolean == True
