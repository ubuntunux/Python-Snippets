anaconda 설치후 패키지를 다운받거나 할때 아래와 같이 보안관련 에러가 뜰수있다. ( https가 막혀있거나 등등 )


    Fetching packages ...
    INFO:print:Fetching packages ...
    Could not connect to https://repo.continuum.io/pkgs/free/win-64/decorator-4.0.4-py34_0.tar.bz2
    INFO:stderrlog:Could not connect to https://repo.continuum.io/pkgs/free/win-64/decorator-4.0.4-py34_0.tar.bz2
    
    Error: Connection error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:600): https://repo.continuum.io/pkgs/free/win-64/decorator-4.0.4-py34_0.tar.bz2


해결방법
아래와 같이 명령을 실행하면 된다.

` conda config --set ssl_verify False`