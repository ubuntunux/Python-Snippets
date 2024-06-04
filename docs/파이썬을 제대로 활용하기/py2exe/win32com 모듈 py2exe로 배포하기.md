[Previous](..)
## win32com 모듈 py2exe로 배포하기
```
#python setup.py py2exe
from distutils.core import setup
import py2exe

setup(
        console=['HansoftMailParser.py'],
        options={
                "py2exe":{
                        #"skip_archive":1,
                        "excludes": ["win32com.gen_py",],
                        "includes": ["win32api", "win32com", "win32com.client", "win32com.client.gencache"],
                        "dll_excludes" : ["MSVCP90.dll", "w9xpopen.exe"]
                }
        }
)
```