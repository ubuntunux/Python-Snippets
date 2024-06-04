[CONTENTS](README.md)
## gcc: error trying to exec 'cc1plus': execvp: Not a directory
파이썬에서 모듈을 설치할때 python setup.py install 명령을 자주 사용하게 되는데 소스코드로 부터 빌드할 경우 C컴파일러를 필요로 하게 된다.
Python으로 setup.py 파일을 설치할때 아래와 같이 gcc 에러가 나는 경우가 있다.

    gcc: error trying to exec 'cc1plus': execvp: Not a directory
error: command 'gcc' failed with exit status 1

이 에러에 대해 찾아보면 거의 대부분 gcc, g++ 을 다시 설치해보라는 답변들 뿐이다.... 아~ 짜증~
하지만 이리저리 해본결과 두가지 해결책이 있다.

에러는 c++ 컴파일러로 빌드를 해야하는데 c 컴파일러인 gcc로 빌드가 되어 발생하는 에러로 보인다.

**해결책**

    CC=g++ python setup.py install

짜잔~~ 이렇게 간단히 해결된다. 그런데...  불행히도 에러나는 경우가 한가지 더 있다.

특수하게 가상환경으로 파이썬을 만든 경우 모든게 정상인데도 gcc 오류가 발생하는 경우가 있다.
이때 sudo권한으로 설치하면 해결되는데 주의해야 할점은 sudo로 실행하는 경우 가상환경의 파이썬이 아니라 시스템에 설치된 파이썬이 실행되므로 전혀 다른곳에 모듈이 설치되어 버린다. 즉 제대로 설치하기 위해선 아래와 같이 sudo를 붙여주고 가상환경 파이썬의 경로까지 적어주어야 한다.

**예제)**
    $ sudo ~/anaconda3/envs/python3/python setup.py install 