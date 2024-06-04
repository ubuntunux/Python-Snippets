> [Python Snippets](../README.md) / [GPGPU](README.md) / pyglet get_devices() error - ctypes.ArgumentError - wrong type.md
## pyglet get_devices() error - ctypes.ArgumentError: argument 2: <class 'TypeError'>: wrong type
pyglet.input.get_devices() 실행시 아래와 같은 에러가 발생

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/python3.5/site-packages/pyglet/input/__init__.py", line 163, in get_devices
    xinput_get_devices(display))
  File "/python3.5/site-packages/pyglet/input/x11_xinput.py", line 332, in get_devices
    if not _have_xinput or not _check_extension(display):
  File "/python3.5/site-packages/pyglet/input/x11_xinput.py", line 325, in _check_extension
    ctypes.byref(first_error))
ctypes.ArgumentError: argument 2: <class 'TypeError'>: wrong type
```


참 별것아니지만 발견하기 까다로운 에러다. pyglet가 설치된 라이브러리 폴더를 찾아가서 x11_xinput.py파일을 열고 아래의 문자열 'XInputExtension'을 b'XInputExtension'으로 바꿔주면 된다.

```
def _check_extension(display):
    major_opcode = ctypes.c_int()
    first_event = ctypes.c_int()
    first_error = ctypes.c_int()
    xlib.XQueryExtension(display._display, b'XInputExtension', 
        ctypes.byref(major_opcode), 
        ctypes.byref(first_event),
        ctypes.byref(first_error))
    return bool(major_opcode.value)
```