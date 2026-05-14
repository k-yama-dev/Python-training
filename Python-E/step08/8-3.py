my_tuple = 'hello',10,True,False,None
print(my_tuple[0])#hello

a,b = 1,2
print(a)#1
print(b)#2

a,b = 1,2
a,b = b,a
print(a)#2
print(b)#1
# a[0],b = b,a#エラー
