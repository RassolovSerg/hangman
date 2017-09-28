def check(word, guesses):
    answer = True
    for i in word:
        if i not in guesses:
            answer = False
    return answer
