def main():
    print(convert(input()))

def convert(emoji):
    emoji = emoji.replace(":)", "🙂")
    emoji = emoji.replace(":(", "🙁")
    return emoji
main()