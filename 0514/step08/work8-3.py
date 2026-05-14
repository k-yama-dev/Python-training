numbers = 10,5,4,1,3
a,b,c,d,e = numbers
print(a,b,c,d,e)#10 5 4 1 3
a,b,c,d,e = b,c,d,e,a
print(a,b,c,d,e)#5 4 1 3 10
print(a,end='')#改行なし
print(b,end='')
