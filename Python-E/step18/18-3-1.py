#可変長キーワード引数
def say_profiles(**profiles):
    for key, value in profiles.items():
        print(key,value)

say_profiles(height=170,weight=60,name='taro')
# height 170
# weight 60
# name taro

#位置引数、可変長位置引数、デフォルト引数、可変長キーワード引数
def say_all(iti,*kahen,data='abc',**datas):
    print('iti:',iti)
    for k in kahen:
        print('kahen:',k)
    print('data:',data)
    for k,v in datas.items():
        print('datas:',k,v)

say_all(1,2,2,2,data='data3',iro='ao',haikei='siro')
# iti: 1
# kahen: 2
# kahen: 2
# kahen: 2
# data: data3
# datas: iro ao
# datas: haikei siro

# say_all(1,2,data='data3',iro='ao',haikei='siro')
# iti: 1
# kahen: 2
# data: data3
# datas: iro ao
# datas: haikei siro

# say_all(1,2,iro='ao',haikei='siro')
# iti: 1
# kahen: 2
# data: abc
# datas: iro ao
# datas: haikei siro

# say_all(1)
# iti: 1
# data: abc

# def say_all2(iti,*kahen,**datas,data='abc'):#エラー
