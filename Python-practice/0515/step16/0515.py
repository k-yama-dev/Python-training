now = 1
while now <= 10:
    print(now, end=" ")
    now += 1

print()

meats = ["pork", "beef", "chicken", "mutton"]
i = 0
while i < len(meats):
    print(meats[i], end=" ")
    i += 1

print()

flag = True
while flag:
    command = input("exit when you write it > ")
    if command == "exit":
        print("exit")
        flag = False
    if command == "0":
        print("start case 0")
    elif command == "1":
        print("start case 1")

print()

flag = False
while True:
    command = input("exit when you write it > ")
    if command == "exit":
        print("exit")
        break
    if command == "0":
        print("start case 0")
    elif command == "1":
        print("start case 1")

print("ワーク")
print("基礎① 3")

n = 10
while n >= 1:
    print(n, end=" ")
    n -= 1
print()

while True:
    urnm = input("Who Are You?(input exit for end) > ")
    if urnm == "exit":
        print("gotcha you still exit")
        break
    else:
        print(f"You Are {urnm} ? Aren't You?")
