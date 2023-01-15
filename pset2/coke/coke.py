due = 50
while due > 0:
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        due -= coin
print(f"Change Owed: {abs(due)}")