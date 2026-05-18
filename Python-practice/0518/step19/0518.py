name = "jiro"


def say():
    name = "taro"
    print(name)


say()
print(name)


def cil(ns=[]):
    for i in range(10):
        ns.append(i)
    return ns


ns = cil()
print(ns)

ns2 = cil()
print(ns2)


def cil1(nms=None):
    if nms is None:
        nms = []
    for i in range(10):
        nms.append(i)
    return nms


nms = cil1()
print(nms)

print("ワーク")


def g():
    m = "How Low!?"


g()
print()

message = "Hi!!!"


def gr():
    message = "How Low?!"


gr()
print(message)

ne = "taro"


def cn(on):
    global name
    name = on


cn('jiro')
print(name)
