[CONTENTS](README.md)
## Kivy - Buildozer 각종 오류 해결하기
1. kivy 1.9.0 버전을 buildozer로 apk를 만들경우 몇가지 버전을 맞추어주어야 한다.

cython 0.21
android build tool revision 22.0
pygments 설치
ant 1.9.3

2. buildozer.spec 파일에 pygments와 같은 추가 모듈이 있는 경우 available module 목록에 없다며 에러를 뱉어내는 경우가 있다.
아래와 같이 python 가상환경을 실행후 buildozer android debug or release를 다시 실행해주면 빌드가 된다.

virtualenv --python=python2.7 ./venv