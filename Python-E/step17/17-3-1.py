def check_name(name):
    #名前チェック。8文字以上ならばTrueを返す
    if len(name) < 8:
        return False
    else:
        return True

your_name = input('君の名は > ')
if check_name(your_name):
    print('OK')
else:
    print('名前が不正です')