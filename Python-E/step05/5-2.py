#インデクシング
text = '今日は良い天気です'
print(text[0])#今
print(text[1])#日
print(text[-1])#す
print(text[-2])#で
# print(text[100])#エラー

#スライシング
print(text[1:4])#日は良
print(text[1:8])#日は良い天気で
print(text[5:])#天気です
print(text[-3:])#気です
print(text[:5])#今日は良い
print(text[:7])#今日は良い天気
print(text[:-2])#今日は良い天気
print(text[:100])#今日は良い天気です

#スライシング (start:end:step)
print(text[1:5:2])#日良
print(text[::2])#今はい気す
print(text[::-1])#すで気天い良は日今
