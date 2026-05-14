profile = {'name':'sato','age':27,'phone':'000-0000-0000','address':'北海道'}
print(profile)#{'name': 'sato', 'age': 27, 'phone': '000-0000-0000', 'address': '北海道'}
profile2 = {'name':'yosida','age':28,'address':'東京'}
print(profile2)#{'name': 'yosida', 'age': 28, 'address': '東京'}
profile.update(profile2)
print(profile)#{'name': 'yosida', 'age': 28, 'phone': '000-0000-0000', 'address': '東京'}