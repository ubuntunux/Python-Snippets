[Previous](..)
## ReadTheDoc을 이용한 파이썬 문서화
가장먼저 sphinx모듈 설치
```
>>> pip install sphinx
>>> pip install sphinx_rtd_theme
```
docs/source/conf.py 파일을 열고 기본 테마 설정
```
html_theme = 'sphinx_rtd_theme'
```

나머지 설정 과정은 아래의 링크에서 동영상을 참고할것

한가지 실수하기 쉬운것이 있는데 문서설정시 docs/conf.py 로 설정하는 경우가있는데 docs/source/conf.py로 해야한다. ( conf.py파일이 해당 경로에 있는지 확인해볼것! )

[https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html](https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html)