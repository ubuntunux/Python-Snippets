TCP 로 서비스를 하려고 하면 port 를 구해야 합니다.
물론 1024 이하의 Well-Known Port 라 하여
/etc/services 에 있는 것과 같이 자주 사용하는
포트 번호도 있지만 그렇지 않고 필요에 따라 
시스템에서 사용하고 있지 않은 포트를 구하고 싶을 때가 있습니다.

요즘에 스택오버플로우에 한글 질문 및 답을 달자는 청원도 있듯이
개발자들에게 정말 주옥같은 문답이 많이 있는데요,
스택 오버플로우에 해당 답이 있어 테스트 해보고 올려 봅니다.

우선 소스는,

    $ cat getopen.py 
    #!/usr/bin/env python
    #coding=utf8
    def get_open_port():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port
    
    print "tcp port to use = %d" % get_open_port()
    print "tcp port to use = %d" % get_open_port()
    print "tcp port to use = %d" % get_open_port()
    print "tcp port to use = %d" % get_open_port()
    print "tcp port to use = %d" % get_open_port()

와 같이 만들었습니다.

이 결과를 돌려보면,

    $ python getopen.py 
    tcp port to use = 48985
    tcp port to use = 55482
    tcp port to use = 60957
    tcp port to use = 54231
    tcp port to use = 52344