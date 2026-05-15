array = [3,9,4,1,7,5,2,8]

for i in range(len(array)-1):
    for j in range(i+1,len(array)):
        print('i:{0}, j:{1} , {2} - {3}'.format(i,j,array[i],array[j]),end=' ')
        if array[i] > array[j]:
            array[i],array[j] = array[j],array[i]
            print(array,'change',end='')
        print()

print(array)
