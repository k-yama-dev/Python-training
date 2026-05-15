your_name = input('名前を入力してください(8文字以上12文字以下) >>> ')
name_length = len(your_name)
if name_length<8 or name_length>12:
    print('12文字以下か、８文字以上にしてください')