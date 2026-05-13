#インデクシング
text = '今日は良い天気です'
print(text[0])
print(text[1])
print(text[-1])
print(text[-2])
# print(text[100])

#スライシング
print(text[1:4])
print(text[1:8])
print(text[5:])
print(text[-3:])
print(text[:5])
print(text[:7])
print(text[:-2])
print(text[:100])

#スライシング(start:end:step)
print(text[1:5:2])
print(text[::2])
print(text[::-1])

#ワーク
print('こんにちは、{}さん'.format('佐藤'))
print('こんにちは、{0}さん'.format('佐藤'))
print('こんにちは、{name}さん'.format(name='佐藤'))
# print('こんにちは、{0}さん'.replace('佐藤'))　←エラー!

text = 'Python'
print(text[0])
print(text[5])
print(text[-1])

text = '明日は雨が降ります'
print(text[1:3:2])
print(text[1:6:2]) # ←正解!
print(text[:8:2])
print(text[:6:2])


