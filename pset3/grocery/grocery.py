items = {}
while True:
    try:
        item = input().upper()
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    except KeyError:
        pass
    except EOFError:
        print("\n")
        break

for item in sorted(items):
    print(str(items[item]), item)