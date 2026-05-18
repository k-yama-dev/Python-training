def send_mail(to,*cc,frm='frm@a.com'):
    print('to:'+to,end=',')
    for c in cc:
        print('cc:'+c,end=',')
    print('from:'+frm)

send_mail('Hisanaga','habu','harada')
send_mail('taguti')
send_mail('suzuki','kawabata','abc@c.com')
