[Previous](..)
## error: Unable to find vcvarsall.bat 
http://mataeoh.egloos.com/7066046

cython이나 각종 파이썬 라이브러리들을 빌드하다보면 아래와 같은 메세지와 함께 빌드가 되지 않는 경우가 있다.

`error: Unable to find vcvarsall.bat`

아래와 같이 환경변수를 설정 해주면 된다.

    Visual Studio 2010 (VS10): SET VS90COMNTOOLS=%VS100COMNTOOLS%
    Visual Studio 2012 (VS11): SET VS90COMNTOOLS=%VS110COMNTOOLS%
    Visual Studio 2013 (VS12): SET VS90COMNTOOLS=%VS120COMNTOOLS%