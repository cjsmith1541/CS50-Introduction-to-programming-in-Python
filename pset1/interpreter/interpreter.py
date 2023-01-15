x, y, z = input("Expression: ").split()
if y == "+":
    answer = float(x) + float(z)
elif y == "-":
    answer = float(x) - float(z)
elif y == "/":
    answer = float(x) / float(z)
elif y == "*":
    answer = float(x) * float(z)
print(answer)