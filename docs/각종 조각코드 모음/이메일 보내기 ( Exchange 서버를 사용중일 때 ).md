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