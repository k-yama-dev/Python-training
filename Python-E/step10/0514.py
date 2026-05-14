nums = {1, 2, 3, 4, 5}
print(nums)
empty_set = set()
print(empty_set)

num = {1, 2, 1, 3, 1, 2, 5}
print(num)
print(set([1, 2, 1, 1, 1, 3, 4, 1]))
num.add(6)
print(num)
num.remove(6)
print(num)

mutable = {"list", "dict", "set"}
immutable = {"str", "number", "tuple"}
seq = {"list", "tuple", "str"}

print(mutable & seq)
print(mutable.intersection(seq))

print(mutable | seq)
print(mutable.union(seq))

print(immutable - seq)
print(immutable.difference(seq))

print(mutable ^ seq)
print(mutable.symmetric_difference(seq))

ns = set()
ns.add(1)
ns.add(1)
ns.add(1)
print(ns)

nbs = [1, 1, 1, 1, 1]
nbs = set(nbs)
print(nbs)
