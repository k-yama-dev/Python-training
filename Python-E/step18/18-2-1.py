#可変長　位置引数
#variable length positional augument

def say_names(*names): #引数をタプルで受ける
    for name in names:
        print(name)

say_names('taro','jiro','saburo')
# taro
# jiro
# saburo

say_names(('taro','jiro'),'saburo')
# ('taro', 'jiro')
# saburo
