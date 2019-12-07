import random
import string

def generate():
    sentence = ""

    for _ in range(28):
        character = random.choice(string.ascii_lowercase + " ")
        sentence += character

    return sentence

def score(string, string_goal):
    s = 0
    i = 0

    for char in string:
        if char == string_goal[i]:
            s += 3.574
        i += 1

    return s

def checker(goal):
    runs = 0
    best = 0

    while score != 100:
        sentence = generate()
        s = score(sentence, goal)

        if runs % 1000 == 0:
            print("Score after 1000 runs: " + str(best))

        if s > best:
            best = s
            print("Best sentence so far: " + sentence)

        runs += 1

    print("Total amount of runs: " + str(runs))

    return 0

checker("methinks it is like a weasel")