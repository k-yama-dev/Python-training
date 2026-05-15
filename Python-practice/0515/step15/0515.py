# 0から9まで繰り返す
for i in range(10):
    print(i, end=" ")
print()

# 1から10まで繰り返す
for j in range(1, 11):
    print(j, end=" ")
print()

# 1から10まで、1つ飛ばしで出力する
for k in range(1, 11, 2):
    print(k, end=" ")
print()

nms = range(10)
print(nms)
print(type(nms))  # class 'range'

nmss = list(range(10))
print(nmss)
print(type(nmss))  # class 'list'

meats = ["pork", "chicken", "beef", "muton"]
for i in range(len(meats)):
    print(i, meats[i])


meat = ["pork", "chicken", "beef", "muton"]
for i, m in enumerate(meat):
    print(i, m)


mets = ["pork", "chicken", "beef", "muton"]
m1 = list(enumerate(mets))
m2 = dict(enumerate(mets))
print(m1)
print(m2)


ms = ["pork", "chicken", "beef", "muton"]
vs = ["bro", "let", "car", "avo"]
for n, y in zip(ms, vs):
    print(n, y)

print("ワーク")

for i in range(0, 10, 2):
    print(i, end=",")
print()

for i in range(1, 4):
    for j in range(1, 4):
        rslt = "{0}*{1}={2}".format(j, i, i * j)
        print(rslt)

heights = [170, 180, 165, 171, 170]
for i, hi in enumerate(heights):
    print(i, hi)
