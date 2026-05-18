def getMax(ldata):
    max = ldata[0]
    for i in ldata:
        if max < i:
            max = i
    return max

mdata = getMax([3,6,1,8,9,2])
print(mdata)
#1