http://mataeoh.egloos.com/7066025


가끔씩 쓰는 cython이다보니 자꾸 사용법을 잊어버린다... 적어놓자~~

1) 아래와 같이 작성한후 helloworld.pyx 파일로 저장하자

    print "Hello World"


2) setup.py 파일을 만들고 아래와 같이 코딩

    from distutils.core import setup
    from Cython.Build import cythonize
    setup( ext_modules = cythonize("helloworld.pyx") )  


3) 아래와 같이 실행하여 동적라이브러리 파일을 만들어보자.

    python setup.py build_ext --inplace



4) 이제 동적라이브러리가 만들어 졌으니 아래처럼 import하여 사용하면 끝~~~

    >>> import helloworld
    Hello World