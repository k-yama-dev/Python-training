my_dict = {'abc': 10}
#clear
my_dict.clear()
print(my_dict)#{}
my_dict = {'age': 20}
#copy
my_dict2 = my_dict.copy()
print(my_dict2)#{'age': 20}
#get
print(my_dict.get('age',20))#20
print(my_dict.get('abc',30))#30
#fromkey
print(my_dict.fromkeys([1,2,'age'],100))#{1: 100, 2: 100, 'age': 100}
print(my_dict)#{'age': 20}
#pop
my_dict['name'] = '太郎'
print(my_dict.pop('name'))#太郎
#popitem
my_dict['name'] = '太郎'
print(my_dict.popitem())#('name', '太郎')
#setdefault
my_dict.setdefault('height',170)
print(my_dict)#{'age': 20, 'height': 170}
#update
my_dict['name'] = '太郎'
my_dict.update({'name':'次郎'})
print(my_dict)#{'age': 20, 'height': 170, 'name': '次郎'}
