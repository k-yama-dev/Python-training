numbers = [4,1,5,7,11,3,4,5]
found = False
for num in numbers:
    if num >= 10:
        found = True

if found:
    print('10以上の整数があります')
else:
    print('ありませんでした')