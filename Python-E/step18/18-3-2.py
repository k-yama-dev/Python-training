#可変長位置引数、可変長キーワード引数
def test_func(*args,**kwargs):
    for ar in args:
        print('ar:',ar)
    for k,v in kwargs.items():
        print('kw:',k,v)

test_func('a','b',iro='white',haikei='black')
