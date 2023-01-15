vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

answer = input("Input: ")
print("Output: ", end="")
for c in answer:
    if c in vowels:
        print("", end="")
    else:
        print(c, end="")
print()