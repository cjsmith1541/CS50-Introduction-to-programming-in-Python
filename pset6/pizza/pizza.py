from tabulate import tabulate
from sys import argv
from csv import DictReader

def main():
    if len(argv) > 2:
        exit("Too many command-line arguments")
    elif len(argv) < 2:
        exit("Too few command-line arguments")
    elif not argv[1].endswith(".csv"):
        exit("Not a CSV file")
    else:
        try:
            with open(argv[1], "r") as file:
                reader = DictReader(file)
                print(tabulate(reader, headers="keys", tablefmt="grid"))
        except FileNotFoundError:
            exit("File does not exist")


if __name__ == "__main__":
    main()