> [Python Snippets](../../README.md) / [파이썬을 제대로 활용하기](../README.md) / [py2exe](README.md) / py2exe 다른 글.md
## py2exe 다른 글
[원문] : [http://www.gamedevforever.com/235](http://www.gamedevforever.com/235)

요즘 파이썬을 만지작 거리며 재미를 붙이고 있는 친절한티스입니다. 요게 쓰면 쓸수록 매력적인 언어네요. 최근에는 파이썬을 이용해 Unity Build Maker를 만들어 유용하게 사용 중입니다. 
 
그런데 이 파이썬 스크립트가 기본적으로는 파이썬이 설치 되어있는 환경에서만 작동이 됩니다. 만약 제가 파이썬으로 유용한 툴을 만들었는데 이것을 다른 컴퓨터에서 쓰기 위해서는 그 컴퓨터에도 파이썬을 설치 해주어야 합니다. 조금 껄쩍찌근 해지죠. 하지만 작성한 파이썬 스크립트를 실행 파일로 만들수 있다면 단지 그 실행 파일만 복사해서 실행만 해주면 됩니다. 참으로 편리 해지겠죠?
 

 
파이썬 스크립트를 실행 파일 형태로 변환 하는것은 의외로 간단합니다. 이미 py2exe 라는 유용한 변환 라이브러리가 존재합니다. 일단, py2exe 홈페이지에 가서 자신의 파이썬 버전에 맞는 라이브러리 버전을 다운로드 하여 설치합니다.
 

py2exe 바로 가기 
 
그 다음 setup.py 파일을 하나 만들어서 아래와 같이 코드를 추가해줍니다.
view plaincopy to clipboardprint?
from distutils.core import setup  
import py2exe  
  
setup(console=['hello.py'])  
hello.py 부분에는 실행 파일로 변환 시키고픈 자신의 파이썬 스크립트 파일명을 적어주시면 됩니다. 그 다음 명령창에 아래와 같이 입력을 하시면...

> python setup.py py2exe
 
무언가가 마구마구 실행되는 듯 하더니 dist 폴더 안에 짠~ 하고 실행 파일로 변환된 자신의 파이썬 스크립트 파일이 나타납니다.


 
그런데 dist 폴더안에 실행 파일만 있는 것이 아니라 기타 잡스러운 파일들도 많이 보입니다. 막상 실행 파일만 떼어다가 다른 곳에서 실행 시켜보면 정상 작동을 안하고, 같이 있던 잡스러운 파일들을 같이 넣어주어야만 작동을 하는 것을 확인 할 수 있습니다.
 

잡스러운 파일들의 용도 
 
실행 파일로 변환 된것은 좋은데 꼭 잡스러운 파일들까지 같이 딸려보낼려니까 왠지 찝찝한 기분을 떨쳐낼수가 없습니다. 파일 하나로 깔끔하게 변환할 수 있는 방법은 없는지 좀더 찾아 보니 방법이 존재하더군요.
 
아까 생성한 setup.py의 코드를 아래와 같이 변경 시켜줍니다.
view plaincopy to clipboardprint?
from distutils.core import setup  
import py2exe, sys, os  
  
sys.argv.append('py2exe')  
  
setup(  
    options = {'py2exe': {'bundle_files': 1}},  
    windows = [{'script': "hello.py"}],  
    zipfile = None,  
)  
아까와 같이 hello.py 에는 자신의 파이썬 스크립트 명을 적어줍니다. 그 다음 명령창에 다시 명령어를 입력해주면... 짜잔!! 아까와 다르게 dist 폴더에 잡다한 파일은 없어지고, 실행 파일 하나만 생성된 것을 확인 할 수 있습니다.
 
