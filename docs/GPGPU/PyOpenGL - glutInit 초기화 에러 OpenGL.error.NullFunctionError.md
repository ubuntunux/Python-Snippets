[Previous](..)
## PyOpenGL - glutInit 초기화 에러 OpenGL.error.NullFunctionError
PyOpenGL을 설치하고 glutInit로 초기화하려 할때 에러가 발생하는 경우가 있다.
가장 흔한 경우는 windows의 경우 freeglut.dll이 없는 경우인데 freeglut 사이트를 방문하여 dll을 다운받을수 있다.
ubuntu의 경우는 간단하게 sudo apt-get install freeglut3-dev 명령으로 다운받을 수 있다.

으읔... 그런데 freeglut를 설치하였는데도 불구하고 아래와 같이 glut 초기화 에러가 발생하는 경우가 또 있다..

OpenGL.error.NullFunctionError: Attempt to call an undefined function glutInit, check for bool(glutInit) before calling

이런 경우 원인이 여러가지가 있을수 있지만 나의 경우는 conda install PyOpenGL 명령으로 opengl 모듈을 설치 하였는데
이 과정에서 freeglut 라이브러리가 함께 설치된다. 혹시나 하는 마음에 conda remove freeglut 명령으로 지워보았다~ 잘된다~!! ㅜㅜ
아직 원인은 모르겠지만 conda에서 제공하는 freeglut 라이브러리에 뭔가 문제가 있는 듯 하다.
직접 freeglut 사이트에서 라이브러리를 다운받아 conda에 설치된 glut 라이브러리를 덮어씌워도 된다. ( windows의 경우 freeglut.dll, Linux의 경우 libglut.so.3 파일이다. )