def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and len(s) < 7 and len(s) > 1:
        for i in range(2, len(s)):
            if s[i].isdecimal() and s[i:len(s)].isdecimal() and s[i] != "0":
                return True
            elif s[i:len(s)].isalpha():
                return True
            elif s[i] == "0" and s[0:1].isalpha():
                return False
            elif s[i].isdecimal() == False and s[i].isalpha() == False:
                return False
    else:
        return False


main()