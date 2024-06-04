Windows7에서 아나콘다를 설치하고 나서 파이썬을 실행을 하려고 했더니 아래와 같은 오류를 뿜어댔다...
처음겪어본 상황이라 난감했다...

    E:\Anaconda>python
    Fatal Python error: Py_Initialize: unable to load the file system codec
      File "c:\Python27\lib\encodings\__init__.py", line 123
        raise CodecRegistryError,\
                                ^
    SyntaxError: invalid syntax
    
    Current thread 0x00000fc0 (most recent call first):

테스트 해본결과 환경변수 PYTHONHOME, PYTHONPAT 값이 현재실행하려는 파이썬 버전과 맞지않는 경로에 설정된 경우에 해당 오류가 발생하였다.

PYTHONHOME, PYTHONPATH 환경변수를 삭제하면 문제는 해결된다.

PYTHONHOME, PYTHONPATH 환경변수를 현재실행하려 하는 파이썬 폴더로 설정해도 되긴하는데 anaconda 배포판을 설치한 경우 conda명령이 제대로 동작하지 않으므로 차라리 환경변수를 없애는 편이 좋다.