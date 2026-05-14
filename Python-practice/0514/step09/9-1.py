report = {'math':80,'science':100}
print(report)
print(report['math'])#80
print(report['science'])#100
empty_dict = {}
print(empty_dict)

print(dict([['sato','taro'],['tanaka','jiro']]))
print(dict(['ab','cd','ef']))

report['japanese'] = 70
print(report)
del report['science']
print(report.pop('japanese'))#70
print(report)#{'math':80}
report['math'] = 100
print(report)#
print(report['japanese'])