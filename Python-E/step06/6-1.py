my_list = ['hello',10,True,False,None]
empty_list = []
str_list = list('hello')
print(str_list)
print(my_list)

#リストのインデクシングとスライシング
foods = ['カレー','チャーハン','寿司','ツナ缶']
print(foods[0])#カレー
print(foods[-1])#ツナ缶
print(foods[1:])#['チャーハン', '寿司', 'ツナ缶']
print(foods[::-1])#['ツナ缶', '寿司', 'チャーハン', 'カレー']

#リストのメソッド
foods.append('シチュー')
print(foods)#['カレー', 'チャーハン', '寿司', 'ツナ缶', 'シチュー']
print(foods.pop())#シチュー
print(foods)#['カレー', 'チャーハン', '寿司', 'ツナ缶']
print(foods.pop(0))#カレー
print(foods)#['チャーハン', '寿司', 'ツナ缶']
foods.remove('寿司')
print(foods)#['チャーハン', 'ツナ缶']
del foods[0]
print(foods)#['ツナ缶']