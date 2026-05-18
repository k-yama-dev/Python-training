def say():
    name = 'taro' #これはローカル変数
    print(name)

say()
print(name)#エラー
#     print(name)
#           ^^^^
# NameError: name 'name' is not defined