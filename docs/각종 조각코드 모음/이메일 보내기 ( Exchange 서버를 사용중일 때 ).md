> [Python Snippets](../README.md) / [각종 조각코드 모음](README.md) / 이메일 보내기 ( Exchange 서버를 사용중일 때 ).md
## 이메일 보내기 ( Exchange 서버를 사용중일 때 )
    import smtplib
    
    # login
    serverURL = 'outlook.smilegate.local'
    conn = smtplib.SMTP(serverURL,587)
    conn.starttls()
    user,password = ('user@gmail.com', 'password')
    try:
        conn.login(user,password)
    except:
        
    
    # Send email
    message = 'From: FROMADDR\nTo: TOADDRLIST\nSubject: Your subject\n\n{}'
    fromAddr = 'user@gmail.com'
    toAddrs = 'other@gmail.com'
    txt = 'This is my message'
    conn.sendmail(fromAddr, toAddrs, message.format(txt))