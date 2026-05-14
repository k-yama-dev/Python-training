mutable = {'list','dict','set'}
imutable = {'str','number','tuple'}
seq = {'list','tuple','str'}

#積集合 & ミュータブルでありかつシーケンス型
print(mutable & seq)#list
print(mutable.intersection(seq))#list

#和集合 | ミュータブルまたはシーケンス型
print(mutable | seq)#{'set', 'tuple', 'list', 'dict', 'str'}
print(mutable.union(seq))#{'set', 'tuple', 'list', 'dict', 'str'}

#差集合 - イミュータブルでシーケンス型ではないもの
print(imutable - seq)#{'number'}
print(imutable.difference(seq))#{'number'}

#排他的論理 ^ EOR ミュータブルまたはシーケンス型だがミュータブルかつシーケンスなものを除く
print(mutable ^ seq)#{'dict', 'set', 'tuple', 'str'}
print(mutable.symmetric_difference(seq))#{'dict', 'set', 'tuple', 'str'}