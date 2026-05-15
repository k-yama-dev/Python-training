flag = True
while flag:
    command = input('exitで終わり > ')
    if command == 'exit':
        print('終了します。')
        flag=False
    if command == '0':
        print('0番の処理を開始')
    elif command == '1':
        print('1番の処理を開始')

# exitで終わり > 0
# 0番の処理を開始
# exitで終わり > 1
# 1番の処理を開始
# exitで終わり > exit
# 終了します。