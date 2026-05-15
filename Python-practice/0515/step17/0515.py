def sayhowlow():
    print("How Low")


sayhowlow()
sayhowlow()
sayhowlow()


def sayurname(n):
    print(n)


sayurname("K")
sayurname(n="D")


def syn(n1, n2, n3):
    print(n1, n2, n3)


syn("K", "D", "A")


def check_name(nam):
    if len(nam) < 8:
        return False
    else:
        return True


orname = input("Your Name? > ")
if check_name(orname):
    print("gotcha")
else:
    print("You Are Lier")


def testfunc():
    return (
        1,
        2,
        3,
        4,
        5,
    )


rslt = testfunc()
print(rslt)

a, b, c, d, e = testfunc()
print(a, b, c, d, e)


def say():
    print("say hi")


say()


def createnum():
    return [1, 2, 3, 4, 5]


nmmms = createnum()
print(nmmms)


def hello(greet,name):
    print(greet ,'、', name)

hello(name = '太郎', greet='こんにちは')
   
