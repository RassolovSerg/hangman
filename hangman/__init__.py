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

    def iteration(self):
        letter = letter_input()
        self.guesses.add(letter)
        if letter in self.word:
            print 'Hit!\n'
            if check(self.word, self.guesses):
                print_word(self.word, self.guesses)
                print 'You won!'
                self.boolean = False
        else:
            self.missed += 1
            print 'Missed, mistake', self.missed, 'out of', self.mistakes, '\n'
            if self.missed >= self.mistakes:
                print_word(self.word, self.guesses)
                print 'You lost!'
                self.boolean = False

    def play(self):
        while self.boolean:
            print_word(self.word, self.guesses)
            print 'Guess a letter:'
            self.iteration()


def main():
    new_game = Game()
    new_game.play()
    return True
