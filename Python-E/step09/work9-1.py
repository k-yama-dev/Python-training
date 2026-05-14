report = {'math':80,'science':100}
report['japanese'] = 30
print(report)#{'math': 80, 'science': 100, 'japanese': 30}
print(report.get('science',0))#100
print(report['science'])#100
report['pc']=100
print(report)#{'math': 80, 'science': 100, 'japanese': 30, 'pc': 100}