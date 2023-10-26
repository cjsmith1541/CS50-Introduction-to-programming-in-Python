from sys import argv
from csv import DictReader, DictWriter


def main():
    if len(argv) > 3:
        exit("Too many command-line arguments")
    elif len(argv) < 3:
        exit("Too few command-line arguments")
    else:
        try:
            with open(argv[1], "r") as before_file, open (argv[2], "w") as after_file:
                reader = DictReader(before_file)
                writer = DictWriter(after_file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    row["last"], row["first"] = row["name"].split(',')
                    row["first"], row["last"] = row["first"].strip(), row["last"].strip()
                    row.pop("name")
                    writer.writerow(row)

        except FileNotFoundError:
            exit(f"Could not read {argv[1]}")


if __name__ == "__main__":
    main()