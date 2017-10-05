import random


def check(word, guesses):
    answer = True
    for i in word:
        if i not in guesses:
            answer = False
    return answer


def print_word(word, guesses):
    answer = ''
    for i in word:
        if i in guesses:
            answer += i
        else:
            answer += '*'
    print 'The word:', answer
    print


def letter_input():
    return raw_input()


class Game(object):

    def __init__(self):
        self.dictionary = ['kek', 'hello', 'bro', 'lol', 'matan']
        self.word = random.choice(self.dictionary)
        self.mistakes = 5
        self.missed = 0
        self.guesses = set()
        self.boolean = True

    def iteration(self, (word, missed, guesses)):
        letter = letter_input()
        guesses.add(letter)
        if letter in word:
            print 'Hit!\n'
            if check(word, guesses):
                print_word(word, guesses)
                print 'You won!'
                self.boolean = False
        else:
            missed += 1
            print 'Missed, mistake', missed, 'out of', self.mistakes, '\n'
            if missed >= self.mistakes:
                print_word(word, guesses)
                print 'You lost!'
                self.boolean = False
        return missed, guesses

    def play(self):
        while self.boolean:
            print_word(self.word, self.guesses)
            print 'Guess a letter:'
            arguments = (self.word, self.missed, self.guesses)
            self.missed, self.guesses = self.iteration(arguments)


def main():
    new_game = Game()
    new_game.play()
