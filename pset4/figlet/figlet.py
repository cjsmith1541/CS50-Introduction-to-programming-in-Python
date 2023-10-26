from pyfiglet import Figlet
from sys import argv, exit
from random import shuffle

figlet = Figlet()
figs = figlet.getFonts()

if len(argv) == 1:
    shuffle(figs)
    figlet.setFont(font=figs[0])
    print(figlet.renderText(input("Input: ")))
elif len(argv) == 3 and (argv[1] == "-f" or argv[1] == "-font") and argv[2] in figs:
    figlet.setFont(font=argv[2])
    print(figlet.renderText(input("Input: ")))
else:
    exit("Invalid usage")