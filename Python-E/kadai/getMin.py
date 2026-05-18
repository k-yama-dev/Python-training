def getMin(ldata):
    min = ldata[0]
    for i in ldata:
        if min > i:
            min = i
    return min

mdata = getMin([3,6,1,8,9,2])
print(mdata)
#1