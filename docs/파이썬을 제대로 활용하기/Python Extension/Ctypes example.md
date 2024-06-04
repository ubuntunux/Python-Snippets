> [Python Snippets](../../README.md) / [파이썬을 제대로 활용하기](../README.md) / [Python Extension](README.md) / Ctypes example.md
#### 구조체(Structure) pack, unpack

```
from ctypes import *

class Example(Structure):
    _fields_ = [
        ("index", c_int),
        ("counter", c_int),
        ]

def Pack(ctype_instance):
    buf = string_at(byref(ctype_instance), sizeof(ctype_instance))
    return buf

def Unpack(ctype, buf):
    cstring = create_string_buffer(buf)
    ctype_instance = cast(pointer(cstring), POINTER(ctype)).contents
    return ctype_instance

if __name__ == "__main__":
    e = Example(12, 13)
    buf = Pack(e)
    e2 = Unpack(Example, buf)
```


#### Structure

```
from ctypes import *

def convert_bytes_to_structure(st, byte):
    # sizoef(st) == sizeof(byte)
    memmove(addressof(st), byte, sizeof(st))


def convert_struct_to_bytes(st):
    buffer = create_string_buffer(sizeof(st))
    memmove(buffer, addressof(st), sizeof(st))
    return buffer.raw


def conver_int_to_bytes(number, size):
    return (number).to_bytes(size, 'big')
```