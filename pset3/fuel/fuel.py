while True:
    try:
        answer = input("Faction: ").split('/')
        if not int(answer[0]) > int(answer[1]) or not answer[1].isnumeric():
            percent = (100 / int(answer[1])) * int(answer[0])
            break
    except (ValueError, ZeroDivisionError):
        pass

if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(f"{round(percent)}%")