def sayurname(name="名無し"):
    print(name)


sayurname()
sayurname("kohei")
sayurname(name="Yamaguchi")


def syn(name, name2="名無し"):
    print(name, name2)


syn(name2="KKK", name="YYY")
syn("kope")


def sn(name, na, me="名無し"):
    print(name, na, me)


sn("ate", "ike")


def nt(*names):
    for name in names:
        print(name)


nt("kohe", "yama", "dai")


def sm(to, *cc, frm="frm@a.com"):
    print("to:", to, end=",")
    for c in cc:
        print("cc:", c, end=",")
    print("from:", frm)


sm('k.yama@g.com','9i6@g.com')

def sp(**pls):
    for key,value in pls.items():
        print(key,value)

sp(height=164,weight=58,name='kohei')

# 可変長位置引数、可変長キーワード引数
def ka(*args,**kwargs):
    for ar in args:
        print('ar:',ar)
    for kwar in kwargs.items():
        print('kwar:',kwar)
ka('a','b','c',a='Aa',b='Bb')
    
def sml(to,*,frm='taro@gmail.com',cc='cc@c.com',bcc='bcc@d.com'):
    print(to,frm,cc,bcc)

sml('to@a.com')
sml('to@a.com',frm='frm@a.com')
# sml('to@a.com','frm@a.com') # キーワードナシはできない

print('ワーク')
# def skk(to='t',fm):
    # print()
print('①')

def aa(to,tr):
    print()

def aaa(d='a',s='u'):
    print()

def ii(*a,**k):
    print()
    pass



def sh(h='おはよう',n='名無し'):
    print(h,n)

sh()
sh('こんにちは')
sh('こんばんは','田中')

