import random


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


class Game():

    def __init__(self):
        self.dictionary = ['kek', 'hello', 'bro', 'lol', 'matan']
        self.word = random.choice(self.dictionary)
        self.mistakes = 5
        self.missed = 0
        self.guesses = set()
        self.boolean = True

    def input(self):
        return raw_input()

    def iteration(self, (word, mistakes, missed, guesses)):
        boolean = True

        letter = self.input()
        guesses.add(letter)
        if letter in word:
            print 'Hit!\n'
            if check(word, guesses):
                print_word(word, guesses)
                print 'You won!'
                boolean = False
        else:
            missed += 1
            print 'Missed, mistake', missed, 'out of', mistakes, '\n'
            if missed >= mistakes:
                print_word(word, guesses)
                print 'You lost!'
                boolean = False
        return boolean, missed, guesses

    def play(self):
        while self.boolean:
            print_word(self.word, self.guesses)
            print 'Guess a letter:'
            arguments = self.word, self.mistakes, self.missed, self.guesses
            self.boolean, self.missed, self.guesses = self.iteration(arguments)


def main():
    new_game = game()
    new_game.play()
