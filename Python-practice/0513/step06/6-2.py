my_list = ['カレー','チャーハン','寿司','ツナ缶']
my_list.append(10)
print(my_list)#['カレー', 'チャーハン', '寿司', 'ツナ缶', 10]
my_list.clear()
print(my_list)#[]
my_list = [1,2,3].copy()
print(my_list)#[1,2,3]
print(my_list.count(1))#3
my_list.extend([4,5,6])
print(my_list)#[1,2,3,4,5,6]
print(my_list.index(5))#4
my_list.insert(0,'追加データ')
print(my_list)#['追加データ', 1, 2, 3, 4, 5, 6]
print(my_list.pop())#[ 1, 2, 3, 4, 5, 6]
my_list.remove(2)
print(my_list)
print(my_list.pop(0))
my_list.sort(reverse=True)
print(my_list)#[5, 4, 3, 1]
