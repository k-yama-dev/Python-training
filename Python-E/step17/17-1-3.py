def say_hello():
    print('Hello!')
print('World') #この行はsay_hello関数の外

def say_hello2():
    print('Hello!')
    print('World') #この行はsay_hello関数の外

say_hello()
say_hello2()

# World
# Hello!