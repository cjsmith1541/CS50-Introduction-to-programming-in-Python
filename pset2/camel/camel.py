answer = input("camelCase: ")

for c in answer:
    if c.isupper():
        print(f"_{c.swapcase()}", end="")
    else:
        print(c, end="")
print()