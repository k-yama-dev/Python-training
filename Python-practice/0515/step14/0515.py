nms = [1, 2, 3, 4, 5]
for n in nms:
    print(n**2)

score = {"math": 25, "eng": 50, "sci": 15}
for value in score.values():  # 辞書のvalueを抜き出す
    print(value)

score = {"math": 25, "eng": 50, "sci": 15}
for valueee in score.keys():  # 辞書のkeyを抜き出す
    print(valueee)

score = {"math": 25, "eng": 50, "sci": 15}
for valuee in score.items():  # 辞書のitemを抜き出す
    print(valuee)

prfs = [
    ("Kurt", 174, "Nirvana"),
    ("MAH", 168, "SiM"),
    ("Chester", 178, "Linkin Park"),
]
for n, h, b in prfs:
    print(n, h, b)

nbs = [4, 1, 5, 7, 11, 3, 4, 5]
found = False
for nm in nbs:
    if nm >= 10:
        found = True
if found:
    print("10以上の整数有り")
else:
    print("なし")

nbs = [4, 1, 5, 7, 11, 3, 4, 5]
found = False
for nm in nbs:
    if nm >= 10:
        found = True
        break  # 10以上の整数が見つかればループ終了
if found:
    print("10以上の整数有り")
else:
    print("なし")

nbe = [4, 1, 5, 7, 11, 3, 4, 5]
for nbee in nbe:
    if nbee >= 10:
        print("10以上の整数有り")
        break  # 10以上の静誠意が見つかればループ終了
else:  # このelseは、breakされなければ実行される
    print("10以上の整数なし")

print("ワーク")

nrs = [1, 2, 3, 4, 5]
for nrss in nrs:
    print(nrss)

menu = ["チャーハン", "ラーメン", "餃子"]
for food in menu:
    print(food)

men = {"チャーハン": 680, "ラーメン": 700}
for k, v in men.items():
    print(k, v)

nss = [1, 2, 3, 4, 5]
nss.reverse()
for nmm in nss:
    print(nmm)
