meats = ['豚肉','牛肉','鶏肉','羊肉']
vegetables = ['ブロッコリー','レタス','ニンジン','アボカド']
for m,v in zip(meats,vegetables):
    print(m,v)

# 豚肉 ブロッコリー
# 牛肉 レタス
# 鶏肉 ニンジン
# 羊肉 アボカド

datas = zip(meats,vegetables)
print(datas)#<zip object at 0x00000208DA443E40>