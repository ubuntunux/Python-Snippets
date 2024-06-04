> [Python Snippets](../../README.md) / [파이썬을 제대로 활용하기](../README.md) / [py2exe](README.md) / py2exe 간단예제.md
## py2exe 간단예제
```
from distutils.core import setup
import py2exe, sys, os, pyopencl

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1,
                          "includes":["pyopencl","twisted",
                                      "zope","QueueReader",
                                      "numpy"]}},
    console=[{'script' : 'phoenix.py'}],
    data_files=["C:\\Users\\Nicklas\\Desktop\\Phoenix-Miner\\kernels\\poclbm\\kernel.cl"],
    zipfile = None,
)
```