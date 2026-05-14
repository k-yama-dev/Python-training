report = {'math':80,'English':100}
report['Japanese']=70
print(report)
print(report['English'])
report['Computer Science']=60
print(report)

profile={'age':27,'name':'Kohei','BD':19980916}
print(profile.get('age'))
print(profile.get('name'))
print(profile.get('address','Kagoshima'))

profile.update({'age':25,'name':'Daisuke','BD':20001104})
print(profile)