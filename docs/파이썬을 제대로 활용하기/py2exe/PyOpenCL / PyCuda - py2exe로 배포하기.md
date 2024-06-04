> [Python Snippets](../../../README.md) / [파이썬을 제대로 활용하기](../../README.md) / [py2exe](../README.md) / [PyOpenCL ](README.md) /  PyCuda - py2exe로 배포하기.md
##  PyCuda - py2exe로 배포하기
http://mataeoh.egloos.com/7088524

** 1. setup.py 파일구성 **

```
#python setup.py py2exe
from distutils.core import setup
import py2exe, sys, os, pyopencl

sys.argv.append('py2exe')

setup(
        console=['demo_mandelbrot.py'],
        options={
                "py2exe":{
                        "dll_excludes" : ["MSVCP90.dll", "w9xpopen.exe"],
                        "includes": ["pyopencl", "numpy"]
                }
        }
)
```

** 2. Library.zip에 라이브러리 추가 **

setup.py 를 실행한 후 생성된 Dist폴더에 보면 Library.zip 파일을 열어 일부 포함되지 않은 라이브러리들을 수동으로 추가한다. 단, egg파일이므로 압축을 풀어서 Library.zip 파일에 추가해 주어야 한다.

  * C:\Python27\Lib\site-packages\appdirs-1.4.0-py2.7.egg  
  * C:\Python27\Lib\site-packages\setuptools-15.2-py2.7.egg  
  * C:\Python27\Lib\site-packages\pyopencl-2015.1-py2.7-win32.egg\pyopencl\cl ( 폴더를 통째로 추가해준다. )  
  * 버전은 최신으로 할것



** 3. PyOpenCL의 __init__.py 파일의 경로수정 **

그냥 실행시 아래와 같은 에러메시지가 발생한다. 

```
Traceback (most recent call last):
  File "demo_mandelbrot.py", line 24, in <module>
  File "E:\Work\PythonProject\PyOpenCL\dist\library.zip\pyopencl\__init__.py", l
ine 79, in <module>
  File "E:\Work\PythonProject\PyOpenCL\dist\library.zip\pyopencl\__init__.py", l
ine 71, in _find_pyopencl_include_path
  File "build\bdist.win32\egg\pkg_resources\__init__.py", line 1154, in resource
_filename
  File "build\bdist.win32\egg\pkg_resources\__init__.py", line 425, in get_provi
der
  File "build\bdist.win32\egg\pkg_resources\__init__.py", line 946, in require
  File "build\bdist.win32\egg\pkg_resources\__init__.py", line 833, in resolve
pkg_resources.DistributionNotFound: The 'pyopencl' distribution was not found an
d is required by the application
```

* Library.zip 파일을 열어서 pyopencl폴더에는 \__init\__.pyc 파일밖에 없으므로 python 라이브러리 폴더로 부터 \__init\__.py 파일을 Library.zip 파일에 넣어주도록 한다.

* \_find_pyopencl_include_path() 함수를 살펴보면 pkg_resources 모듈을 통해 경로를 얻어오는데 이 부분에서 에러가 발생한다. 임시방편으로 해결하는 방법.
```
_DEFAULT_INCLUDE_OPTIONS = ["-I", _find_pyopencl_include_path()]
```
이부분을 아래와 같이 수정해준다. 즉, 수동으로 경로를 직접 입력해준다.
```
_DEFAULT_INCLUDE_OPTIONS = ["-I", "pyopencl/cl"]
```

자!!! 이렇게하면 pyopencl을 배포할수 있다~~~!!