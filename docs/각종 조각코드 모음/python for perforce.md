> [Python Snippets](../README.md) / [각종 조각코드 모음](README.md) / python for perforce.md
## python for perforce
help : http://www.perforce.com/perforce/doc.current/manuals/p4script/chapter.python.html

    from P4 import P4, P4Exception
    import Tkinter
    
    p4 = P4()
    p4.port = "intranet.company.net:1666"
    p4.user = "myusername"
    p4.password = "mypassword"
    #p4.client = "clientname"
    p4.connect()
    print p4.connected()
    p4.run_login()
    
    
    # conversion time stamp
    #import datetime
    #myDate = datetime.datetime.utcfromtimestamp( int(timestampValue) )
    
    
    # Get p4 infos
    try:
        info = p4.run( "info" )        # Run "p4 info" (returns a dict)
        for key in info[0]:            # and display all key-value pairs
            print key, "=", info[0][key]
    except P4Exception:
      for e in p4.errors:            # Display errors
          print e
    
    print "-" * 40
    opened = p4.run_opened()
    
    for i in opened:
        print i
    print "-" * 40
    
    
    try:
      p4.connect()
      p4.exception_level = 1
      # ignore "File(s) up-to-date"s
      #files = p4.run_sync("//tripod_graphics/9.TA/Tool/HansoftMailParser/")
      print "Sync :", p4.run("sync", "//tripod_graphics/9.TA/Tool/HansoftMailParser/*.*")
    
    except P4Exception:
      for e in p4.errors:
        print e
      print "-" * 40  
    
    finally:
      p4.disconnect()
      print p4.connected()