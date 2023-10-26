def main():
    print(f"Output: {shorten(input('Input: '))}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    answer = ""
    for c in word:
        if c in vowels:
            answer += ""
        else:
            answer += c
    return str(answer)

if __name__ == "__main__":
    main()