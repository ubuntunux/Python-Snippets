[CONTENTS](README.md)
## Python FFI with ctypes and cffi
[원문] : [http://eli.thegreenplace.net/2013/03/09/python-ffi-with-ctypes-and-cffi/](http://eli.thegreenplace.net/2013/03/09/python-ffi-with-ctypes-and-cffi/)

이전 글에서는 libffi를 사용하여 C 코드에 대한 동적 호출을 수행하는 방법을 설명했습니다. 여기서 "완전 동적"은 인수 및 반환 값의 유형조차도 런타임에 결정된다는 것을 의미합니다.

여기에서는 PyPy 팀이 개발 한 기존 stdlib ctypes 패키지와 새로운 cffi 라이브러리 및 향후 Python stdlib에 포함될 후보와 같은 작업이 파이썬에서 어떻게 수행되는지에 대해 설명하고자합니다.

## With ctypes
앞서 논의한 공유 객체로 시작하겠다. 다음 코드는 ctypes를 사용하여 파이썬에서로드하고 실행합니다. 파이썬 3.2에서 테스트했지만 다른 버전도 (2.7 포함) 작동해야합니다.

```
from ctypes import cdll, Structure, c_int, c_double, c_uint

lib = cdll.LoadLibrary('./libsomelib.so')
print('Loaded lib {0}'.format(lib))

# Describe the DataPoint structure to ctypes.
class DataPoint(Structure):
    _fields_ = [('num', c_int),
                ('dnum', c_double)]

# Initialize the DataPoint[4] argument. Since we just use the DataPoint[4]
# type once, an anonymous instance will do.
dps = (DataPoint * 4)((2, 2.2), (3, 3.3), (4, 4.4), (5, 5.5))

# Grab add_data from the library and specify its return type.
# Note: .argtypes can also be specified
add_data_fn = lib.add_data
add_data_fn.restype = DataPoint

print('Calling add_data via ctypes')
dout = add_data_fn(dps, 4)
print('dout = {0}, {1}'.format(dout.num, dout.dnum))
```

이것은 매우 간단합니다. 동적 언어 FFI가 실행되는 한 ctype은 꽤 좋습니다. 그러나 우리는 더 잘할 수 있습니다. ctypes의 주된 문제점은 특정 API를 사용하여 ctypes에 대한 C 선언을 완전히 반복해야한다는 것입니다. 예를 들어, DataPoint 구조에 대한 설명을 참조하십시오. 리턴 유형도 명시 적으로 지정해야합니다. 이것은 사소한 C 라이브러리를 래핑하기위한 많은 작업 일뿐만 아니라 오류가 발생하기 쉽습니다. C 헤더를 ctypes 설명으로 잘못 번역하면 런타임시 segfault가 생길 수 있습니다. 디버그 빌드를 사용하지 않고 디버그하기는 쉽지 않습니다. ctypes를 사용하면 형식 검사의 일부 측정을 위해 함수에 argtypes를 명시 적으로 지정할 수 있지만 파이썬 코드 내에서만 가능합니다. 올바른 선언을 얻었 으면 올바른 유형의 객체를 전달하는 데 도움이됩니다. 그러나 선언문을 올바르게 작성하지 않으면 아무 것도 당신을 구할 수 없습니다.

## How does it work?
ctypes는 libffi를 둘러싼 파이썬 래퍼입니다. CPython 프로젝트는 libffi 버전을 가지고 있으며, ctypes는 libffi에 링크하는 C 확장 모듈과 필요한 접착제를위한 Python 코드로 구성됩니다. libffi 사용법을 이해한다면 ctypes의 작동 방식을 쉽게 이해할 수 있습니다.

libffi는 매우 강력하지만, ctypes에 적용 할 수있는 몇 가지 제한이 있습니다. 예를 들어, 동적으로로드 된 함수에 union을 값으로 전달하는 것은 지원되지 않습니다. 그러나 전반적으로 장점은 한계를 뛰어 넘는 데, 필요한 경우 해결하기가 어렵지 않습니다.

## With cffi
cffi는 흥미로운 접근법을 사용하여 ctypes를 개선하려고합니다. 이를 통해 실제 C 선언을 구문 분석하고 필수 데이터 유형 및 함수 시그니처를 자동으로 추론함으로써 ctype 표기법으로 C 선언을 다시 작성하지 않아도됩니다. 다음은 cffi로 구현 된 동일한 예제입니다 (Python 3.2에서 cffi 0.5로 테스트 됨).

```
from cffi import FFI

ffi = FFI()

lib = ffi.dlopen('./libsomelib.so')
print('Loaded lib {0}'.format(lib))

# Describe the data type and function prototype to cffi.
ffi.cdef('''
typedef struct {
    int num;
    double dnum;
} DataPoint;

DataPoint add_data(const DataPoint* dps, unsigned n);
''')

# Create an array of DataPoint structs and initialize it.
dps = ffi.new('DataPoint[]', [(2, 2.2), (3, 3.3), (4, 4.4), (5, 5.5)])

print('Calling add_data via cffi')
# Interesting variation: passing invalid arguments to add_data will trigger
# a cffi type-checking exception.
dout = lib.add_data(dps, 4)
print('dout = {0}, {1}'.format(dout.num, dout.dnum))
```

지루하게 파이썬에 대한 C 선언을 설명하는 대신, cffi는 직접 사용하여 필요한 모든 접착제를 자동으로 생성합니다. 일을 잘못하고 세그 폴트에 빠지게하는 것이 훨씬 어렵습니다.

이것은 cffi가 ABI 레벨이라고 부르는 것을 보여줍니다. 시스템 C 컴파일러를 사용하여 선언의 누락 부분을 자동 완성하는 cffi의 또 다른 야심적인 사용이 있습니다. C 컴파일러가 필요 없기 때문에 여기서 ABI 레벨에 초점을 맞추고 있습니다. 어떻게 작동합니까? 아래쪽으로, cffi도 실제 낮은 수준의 호출을 생성하는 libffi에 의존합니다. C 선언을 파싱하려면 pycparser를 사용합니다.

cffi에 대한 또 다른 멋진 점은 PyPy 생태계의 일부인 PyPy의 JIT 기능을 실제로 활용할 수 있다는 것입니다. 이전 게시물에서 언급했듯이 libffi를 사용하는 것은 컴파일러가 생성 한 호출보다 훨씬 느립니다. 왜냐하면 각 호출에 대해 많은 인수 설정 작업이 필요하기 때문입니다. 하지만 일단 실제로 실행을 시작하면 실제적으로 호출 된 함수의 서명이 변경되지 않습니다. 따라서 JIT 컴파일러는 더 스마트 해지고 더 빠르고 직접적인 호출을 생성 할 수 있습니다. PyPy가 이미 cffi로이 작업을 수행하고 있는지 여부는 알 수 없지만 실제로 계획대로 진행되고 있습니다.

## 좀 더 복잡한 예제
필자는 POSIX readdir_r (readdir의 재진입 버전)이라는 더 복잡한 함수를 보여주는 또 다른 예제를 보여주고 싶습니다. 이 예제는 cffi 소스 트리의 일부 데모 / 코드를 기반으로합니다. 다음은 ctypes를 사용하여 디렉토리의 내용을 나열하는 코드입니다.

```
from ctypes import (CDLL, byref, Structure, POINTER, c_int,
                    c_void_p, c_long, c_ushort, c_ubyte,
                    c_char, c_char_p, c_void_p)

# CDLL(None) invokes dlopen(NULL), which loads the currently running
# process - in our case Python itself. Since Python is linked with
# libc, readdir_r will be found there.
# Alternatively, we can just explicitly load 'libc.so.6'.
lib = CDLL(None)
print('Loaded lib {0}'.format(lib))

# Describe the types needed for readdir_r.
class DIRENT(Structure):
    _fields_ = [('d_ino', c_long),
                ('d_off', c_long),
                ('d_reclen', c_ushort),
                ('d_type', c_ubyte),
                ('d_name', c_char * 256)]

DIR_p = c_void_p
DIRENT_p = POINTER(DIRENT)
DIRENT_pp = POINTER(DIRENT_p)

# Load the functions we need from the C library. Specify their
# argument and return types.
readdir_r = lib.readdir_r
readdir_r.argtypes = [DIR_p, DIRENT_p, DIRENT_pp]
readdir_r.restype = c_int

opendir = lib.opendir
opendir.argtypes = [c_char_p]
opendir.restype = DIR_p

closedir = lib.closedir
closedir.argtypes = [DIR_p]
closedir.restype = c_int

# opendir's path argument is char*, hence bytes.
path = b'/tmp'
dir_fd = opendir(path)
if not dir_fd:
    raise RuntimeError('opendir failed')

dirent = DIRENT()
result = DIRENT_p()

while True:
    # Note that byref() here is optional since ctypes can do it on its
    # own by observing the argtypes declared for readdir_r. I keep byref
    # for explicitness.
    if readdir_r(dir_fd, byref(dirent), byref(result)):
        raise RuntimeError('readdir_r failed')
    if not result:
        # If (*result == NULL), we're done.
        break
    # dirent.d_name is char[], hence we decode it to get a unicode
    # string.
    print('Found: ' + dirent.d_name.decode('utf-8'))

closedir(dir_fd)
```

여기서는 한 걸음 더 나아가 실제로 가져온 함수에 필요한 인수 유형을 설명했습니다. 다시 한번, 이것은 단지 어느 정도 오류를 피하는 데 도움이됩니다. 코드가 지루하다는 점에 동의해야합니다. cffi를 사용하여 C 선언을 "복사하여 붙여 넣기"하고 실제 호출에 집중할 수 있습니다.

```
from cffi import FFI

ffi = FFI()
ffi.cdef("""
    typedef void DIR;
    typedef long ino_t;
    typedef long off_t;

    struct dirent {
        ino_t          d_ino;       /* inode number */
        off_t          d_off;       /* offset to the next dirent */
        unsigned short d_reclen;    /* length of this record */
        unsigned char  d_type;      /* type of file; not supported
                                       by all file system types */
        char           d_name[256]; /* filename */
    };

    DIR *opendir(const char *name);
    int readdir_r(DIR *dirp, struct dirent *entry, struct dirent **result);
    int closedir(DIR *dirp);
""")

# Load symbols from the current process (Python).
lib = ffi.dlopen(None)
print('Loaded lib {0}'.format(lib))

path = b'/tmp'
dir_fd = lib.opendir(path)
if not dir_fd:
    raise RuntimeError('opendir failed')

# Allocate the pointers passed to readdir_r.
dirent = ffi.new('struct dirent*')
result = ffi.new('struct dirent**')

while True:
    if lib.readdir_r(dir_fd, dirent, result):
        raise RuntimeError('readdir_r failed')
    if result[0] == ffi.NULL:
        # If (*result == NULL), we're done.
        break
    print('Found: ' + ffi.string(dirent.d_name).decode('utf-8'))

lib.closedir(dir_fd)
```

readdir_r에 대한 맨 페이지가 struct dirent 안에있는 모든 typedef 선언을 완전하게 지정하지 않았기 때문에 "copy paste"를 따옴표 안에 넣었습니다. 예를 들어, ino_t가 길다는 것을 발견하려면 파기를해야합니다. cffi의 또 다른 목표 인 API 레벨은 Python 프로그래머가 이러한 선언을 건너 뛰고 C 컴파일러가 세부 사항을 완성 할 수있게하는 것입니다. 그러나 이것은 C 컴파일러를 필요로하기 때문에 ABI 레벨과는 매우 다른 해결책이라고 생각합니다. 사실,이 시점에서는 FFI가 아니라 파이썬 코드에 C 확장을 작성하는 대체 방법입니다.

