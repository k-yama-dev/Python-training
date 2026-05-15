while True:
    your_name = input('あなたの名前は？(exitで終了)> ')
    if your_name == 'exit':
        print('処理を終了します')
        break
    else:
        print(your_name)
# あなたの名前は？(exitで終了)> taro
# taro
# あなたの名前は？(exitで終了)> exit
# 処理を終了します