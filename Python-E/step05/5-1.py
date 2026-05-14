name = 'taro'
print(name.title())#Taro
print(name.upper())#TARO
print(name)#taro
name = name.upper()
print(name)#TARO

#format
print('{}さん、{}'.format('taro','こんにちは'))
print('{0}、{1}'.format('Hello','taro'))
print('{name}さん!'.format(name='taro'))

#replace
print('Hello World'.replace('Hello','Hi'))
hello = 'Hello World'
# print(hello.replcae('Hello','Hi'))#エラー

#count
print('Hello World'.count('l'))#3

#index
print('Hello World'.index('Hello'))#0
