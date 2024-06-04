> [Python Snippets](../../README.md) / [파이썬을 제대로 활용하기](../README.md) / [py2exe](README.md) / PyOpenGL - py2exe로 배포하기.md
## PyOpenGL - py2exe로 배포하기
[http://mataeoh.egloos.com/7088522](http://mataeoh.egloos.com/7088522)

I played with getting a py2exe executable created from PyOpenGL today, and it is very close to working.  The basics:

```
from distutils.core import setup
import py2exe, sys
import glob, os
import OpenGL

sys.argv.append('py2exe')

data_files = [
    (
        os.path.join('OpenGL','DLLS'),
        glob.glob( os.path.join( os.path.dirname( OpenGL.__file__ ), 'DLLS', '*.*' ))
    ),
]

if __name__ == "__main__":
    setup(
        windows=['glutplane.py'],
        options={
            "py2exe": {
                "includes": [
                    "ctypes", "logging",
                    'OpenGL.platform.win32',
                ] + [
                    'OpenGL.arrays.%s'%x for x in [
                        'ctypesarrays','ctypesparameters','ctypespointers',
                        'lists','nones','numbers','numpymodule','strings','vbo'
                    ]
                ],
                'skip_archive': True,
            },
        },
        data_files = data_files,
    )
print("Done")
```

Which collects all of PyOpenGL's plugins that are applicable for use in Win32 (basically the platform plugin and all of the major array plugins) and suppresses packing the collected Python files into a zip-file (skip_archive) so that the PyOpenGL code that looks for precompiled GLUT and GLE in OpenGL/DLLS will work. Unfortunately, at least on my test VM the PyOpenGL b2 doesn't actually include the contents of the DLLS directory after installation :( . I corrected that manually for now, but will need to fix that properly at some point.
 Problem is, even with that, the resulting exe (which I'm testing with the PyOpenGL_demo GLUT shaders test) just silently exits on my XP virtual machine. No traceback. Nothing. Just exits. The built directory structure seems fine, and it properly limits the PyOpenGL code to those extensions you actually import, but there's no actual, you know, 3D graphics. It could be that my ancient VM just can't handle the truth, but for now I've run out of time to play with it. It would be nice if there were a way in py2exe to specify e.g. don't pack *this* module, something like "not egg safe" in setuptools, so that the rest of the app can be packed normally and just the one module would get unpacked into the filesystem.