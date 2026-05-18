def say_your_name(name,name2='名無し'):
    print(name,name2)

say_your_name('taro')#taro 名無し
# say_your_name(name2='taro','jiro')#SyntaxError: positional argument follows keyword argument
say_your_name(name2='taro',name='jiro')#キーワードをすべて指定するならば順番は問わない

def say_your_names(name,name2,name3='名無し'):
    print(name,name2,name3)

say_your_names('taro','jiro')
# say_your_names(name2='dareka','taro')#positional argument follows keyword argument
#位置引数がキーワード引数の後ろにあるのでエラー

def say_your_namess(name,name2='名前はまだない',name3='名無し'):
    print(name,name2,name3)

say_your_namess('jiro')
