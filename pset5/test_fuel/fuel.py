def main():
    while True:
        try:
            answer = convert(input("Faction: "))
            break
        except (ValueError, ZeroDivisionError,):
            pass
    print(gauge(answer))


def convert(fraction):
    answer = fraction.split('/')
    if not answer[0].isnumeric():
        raise ValueError
    elif int(answer[1]) == 0:
        raise ZeroDivisionError
    elif int(answer[0]) > int(answer[1]):
        raise ValueError
    else:
        return round((100 / int(answer[1])) * int(answer[0]))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()