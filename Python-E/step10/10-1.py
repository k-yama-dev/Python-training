numbers = {1,2,3,4,5}
print(numbers)#
empty_set = set()
print(empty_set)
print(type(empty_set))#set
empty_set2 = {}
print(empty_set2)#{}
print(type(empty_set2))#dict

numbers = {1,2,1,3,1,2,5}
print(numbers)#{1, 2, 3, 5}
print(set([1,2,1,1,1,1,3,4,1]))#{1, 2, 3, 4}
numbers.add(6)
print(numbers)#{1, 2, 3, 5, 6}
numbers.remove(6)#key指定
print(numbers)#{1, 2, 3, 5}
#入力順は無視
numbers = {5,4,3,2,1}
print(numbers)#{1, 2, 3, 4, 5}
datas = {'b','a','c'}
print(datas)#{'b', 'c', 'a'}???{'b', 'a', 'c'}やるたび違う