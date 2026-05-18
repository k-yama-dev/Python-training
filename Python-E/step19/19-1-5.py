def say():
    global name
    name = 'taro' #これはローカル変数
    print(name)#taro

say()
print(name)#taro
