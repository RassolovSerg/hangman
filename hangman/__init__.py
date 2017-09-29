import random


def reader(name):
    with open(name, 'r') as dictionary_file:
        return dictionary_file.read().split('\n')[:-1]


def print_word(word, guesses):
    answer = ''
    for i in word:
        if i in guesses:
            answer += i
        else:
            answer += '*'
    print 'The word:', answer
    print


def check(word, guesses):
    answer = True
    for i in word:
        if i not in guesses:
            answer = False
    return answer


def initial(name):
    diction = reader(name)
    word = random.choice(diction)
    mistakes = 5
    missed = 0
    guesses = set()
    boolean = True
    return word, mistakes, missed, guesses, boolean


def main():
    word, mistakes, missed, guesses, boolean = initial('dictionary.dat')

    while boolean:
        print_word(word, guesses)
        print 'Guess a letter:'
        letter = raw_input()
        guesses.add(letter)
        if letter in word:
            print 'Hit!'
            print
            if check(word, guesses):
                print_word(word, guesses)
                print 'You won!'
                boolean = False
        else:
            missed += 1
            print 'Missed, mistake', missed, 'out of', mistakes
            if missed >= mistakes:
                print_word(word, guesses)
                print 'You lost!'
                boolean = False
