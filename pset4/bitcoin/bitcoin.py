from sys import argv, exit
import requests
import json

def main():
    if len(argv) != 2:
        exit("Missing command-line argument")
    elif isfloat(argv[1]) is False:
        exit("Command-line argument is not a number")
    try:
        bitcoin_json = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = bitcoin_json.json()
        answer = float(argv[1]) * float(o["bpi"]["USD"]["rate_float"])
        print(f"${answer:,.4f}")
    except requests.RequestException:
        exit("Unable to get information")



def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()