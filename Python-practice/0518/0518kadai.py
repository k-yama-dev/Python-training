print('課題1:getMin(リスト)という関数でリストの最小値を返しなさい')
print('      ※ ただし、組み込みMinは使わない')

def getMin(int_list):
    min=int_list[0]
    for num in int_list:
        if num<min:
            min=num
    return min

tl=[12,45,93,13,22,3]
rslt = getMin(tl)
print(rslt)

w2 = [34,25,67,15,77,32,2]
rslt2 = getMin(w2)
print(rslt2)