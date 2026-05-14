numbers1 = [6,3,5,4,1,2]
numbers2 = numbers1
numbers2.sort()
print(numbers2)#[1, 2, 3, 4, 5, 6]
print(numbers1)#[1, 2, 3, 4, 5, 6]
#number2もsortされてしまう

numbers1 = [6,3,5,4,1,2]
numbers2 = numbers1.copy()
numbers2.sort()
print(numbers2)#[1, 2, 3, 4, 5, 6]
print(numbers1)#[6, 3, 5, 4, 1, 2]
