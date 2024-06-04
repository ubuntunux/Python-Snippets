> [Python Snippets](../../README.md) / [파이썬을 제대로 활용하기](../README.md) / [py2exe](README.md) / win32com 모듈을 py2exe로 내보낼때 IOError 해결.md
## win32com 모듈을 py2exe로 내보낼때 IOError 해결
win32com을 사용중인 경우 py2exe로 만들경우 실행파일은 잘 생성되나 실행시 IOError가 발생한다.

에러 내용은 win32com\gen_py\__init__.pyc파일을 찾을수 없다는것.



1. 소스코드에 아래와 같이 추가하여 준다.

2. 생성된 library.zip 파일을 열고 win32com\gen_py 폴더를 지운다.

3. 실행파일을 실행하면 자동으로 __init__.pyc 파일이 생성되고 실행이 된다.



The function EnsureDispatch() in win32.client.gencache allows you specify a prog_id and the gen_py cache wrapper objects are created at runtime if they don't already exist. This is useful if you don't care what version of COM server you use, allowing users to have various versions and still work with your code.

First the gencache code must be allowed to create the cache by setting win32com.gencache.is_readonly = False. Then as the target machine may not have Python installed it is necessary to get the gencache code to use a suitable directory other than the default in lib\site-packages\win32com\client\gen_py. This is achieved by simply removing (or renaming) win32com\client\gen_py and the gen_py cache is then created in %temp% (user's temp). This must be done on the development machine and py2exe will then create code that uses it on the target machine.

A final wrinkle is that the first time you run it the cache is created but an import exception is generated. It appears that py2exe never calls the win32com.client.__init__() in the 'import win32com.client'. This code creates the cache __init__.py file that sets the package module path. A call to gencache.Rebuild() fixes that as calling __init__() doesn't seem to work either.

For example:

The function EnsureDispatch() in win32.client.gencache allows you specify a prog_id and the gen_py cache wrapper objects are created at runtime if they don't already exist. This is useful if you don't care what version of COM server you use, allowing users to have various versions and still work with your code.



First the gencache code must be allowed to create the cache by setting win32com.gencache.is_readonly = False. Then as the target machine may not have Python installed it is necessary to get the gencache code to use a suitable directory other than the default in lib\site-packages\win32com\client\gen_py. This is achieved by simply removing (or renaming) win32com\client\gen_py and the gen_py cache is then created in %temp% (user's temp). This must be done on the development machine and py2exe will then create code that uses it on the target machine.



A final wrinkle is that the first time you run it the cache is created but an import exception is generated. It appears that py2exe never calls the win32com.client.__init__() in the 'import win32com.client'. This code creates the cache __init__.py file that sets the package module path. A call to gencache.Rebuild() fixes that as calling __init__() doesn't seem to work either.



For example:





```
import win32com.client

if win32com.client.gencache.is_readonly == True:
  #allow gencache to create the cached wrapper objects
  win32com.client.gencache.is_readonly = False
  # under p2exe the call in gencache to __init__() does not happen
  # so we use Rebuild() to force the creation of the gen_py folder
  win32com.client.gencache.Rebuild()

  # NB You must ensure that the python...\win32com.client.gen_py dir does not exist
  # to allow creation of the cache in %temp%

# Use SAPI speech through IDispatch
from win32com.client.gencache import EnsureDispatch
from win32com.client import constants
voice = EnsureDispatch("Sapi.SpVoice", bForDemand=0)
voice.Speak( "Hello World.", constants.SVSFlagsAsync )
```