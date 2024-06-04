> [Python Snippets](../README.md) / [GPGPU](README.md) / PyOpenGL - glutInit 초기화시 에러가 발생할때 .md
## PyOpenGL - glutInit 초기화시 에러가 발생할때.. 
http://mataeoh.egloos.com/7088520

* Error Message

Traceback (most recent call last):
  File "main.py", line 35, in __init__
    glutInit(sys.argv)
  File "C:\Python27\lib\site-packages\OpenGL\GLUT\special.py", line 324, in glut
Init
    _base_glutInit( ctypes.byref(count), holder )
TypeError: 'NoneType' object is not callable


위와 같이 glutInit(sys.argv)를 실행하면 에러가 나는 경우가 있다.
해결방법은 http://freeglut.sourceforge.net/ 사이트를 방문하여 freeglut 라이브러리를 다운받아 설치하면 된다.
설치경로는 소스코드가 있는 폴더에 freeglut.dll을 복사해주거나 아래와 같이 OS 시스템에 맞는 폴더에 복사해주면 된다.

Window x64(64bit) 일 경우는 C:\Windows\SysWOW64
Window x86(32bit) 일 경우는 C:\Windows\System32

주의 : 당연한 얘기지만 freeglut.dll 파일의 경우 64bit와 32bit 버전이 있다. OS의 환경에 맞추는 것이 아니라 python이 32bit or 64bit 인지에 맞춰서 freeglut파일을 복사해 주어야 한다.