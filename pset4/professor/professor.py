import random
from sys import exit

def main():
    level = get_level()
    correct = 0
    for turn in range(10):
        int1, int2 = generate_integer(level), generate_integer(level)
        right_answer = int1 + int2
        for attempt in range(3):
            try:
                answer = int(input(f"{int1} + {int2} = "))
                assert answer == right_answer
                correct += 1
                break
            except (AssertionError, ValueError):
                print("EEE")
                if attempt == 2:
                    print(f"{int1} + {int2} = {right_answer}")
                pass
    print(f"Score: {correct}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            assert level > 0 and level < 4
            return level
        except (AssertionError, ValueError):
            pass


def generate_integer(level):
    if level == 1:
        return random.randrange(0, 10)
    elif level == 2:
        return random.randrange(10, 100)
    elif level == 3:
        return random.randrange(100, 1000)
    else:
        return ValueError

if __name__ == "__main__":
    main()