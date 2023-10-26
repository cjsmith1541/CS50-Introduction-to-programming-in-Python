from random import randint

while True:
    try:
        n = int(input("Level: "))
        assert n > 0
        answer = randint(1, n)
        while True:
            try:
                guess = int(input("Guess: "))
                assert guess > 0
                if guess < answer:
                    print("Too small!")
                elif guess > answer:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
            except (AssertionError, ValueError):
                pass
        break
    except (AssertionError, ValueError):
        pass
