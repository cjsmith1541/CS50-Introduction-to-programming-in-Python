from sys import argv
from os.path import splitext
from PIL import Image, ImageOps

def main():
    if len(argv) > 3:
        exit("Too many command-line arguments")
    elif len(argv) < 3:
        exit("Too few command-line arguments")
    elif not argv[1].endswith((".png", ".jpg", ".jpeg")):
        exit("Invalid input")
    elif not argv[2].endswith((".png", ".jpg", ".jpeg")):
        exit("Invalid output")
    elif extension(argv[1]) != extension(argv[2]):
        exit("Input and output have different extensions")
    else:
        try:
            shirt, photo = Image.open("shirt.png"), Image.open(argv[1])
            size = shirt.size
            new_photo = ImageOps.fit(photo, size)
            new_photo.paste(shirt, shirt)
            new_photo.save(argv[2])
        except FileNotFoundError:
            exit("Input does not exist")


def extension(argument):
    split = splitext(argument)
    return split[1]

if __name__ == "__main__":
    main()