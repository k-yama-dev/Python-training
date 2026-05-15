your_name = input('名前を入力してください(8文字以上12文字以下) >>> ')
if len(your_name)<8 or len(your_name)>12:
    print('12文字以下か、８文字以上にしてください')