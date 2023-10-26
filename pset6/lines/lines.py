from sys import argv, exit

def main():
    number_of_lines = 0
    if len(argv) > 2:
        exit("Too many command-line arguments")
    elif len(argv) < 2:
        exit("Too few command-line arguments")
    elif not argv[1].endswith(".py"):
        exit("Not a Python file")
    else:
        try:
            with open(argv[1], "r") as file:
                for line in file:
                    if line.lstrip().startswith("#"):
                        pass
                    elif line.strip() == "":
                        pass
                    else:
                        number_of_lines += 1
        except FileNotFoundError:
            exit("File does not exist")
    print(number_of_lines)


if __name__ == "__main__":
    main()