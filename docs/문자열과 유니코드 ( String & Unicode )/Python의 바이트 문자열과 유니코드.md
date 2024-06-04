[https://stackoverflow.com/questions/6224052/what-is-the-difference-between-a-string-and-a-byte-string](https://stackoverflow.com/questions/6224052/what-is-the-difference-between-a-string-and-a-byte-string)

컴퓨터가 저장할 수있는 유일한 것은 바이트입니다.

컴퓨터에 저장하려면 먼저 인코딩해야합니다. 즉, 바이트로 변환해야 한다는 뜻입니다.

음악을 저장하려면 먼저 MP3, WAV 등을 사용하여 음악을 인코딩해야합니다.
그림을 저장하려면 PNG, JPEG 등을 사용하여 먼저 인코딩해야합니다.
텍스트를 저장하려면 먼저 ASCII, UTF-8 등을 사용하여 텍스트를 인코딩해야합니다.
MP3, WAV, PNG, JPEG, ASCII 및 UTF-8이 인코딩의 예입니다. 인코딩은 오디오, 이미지, 텍스트 등을 바이트 단위로 나타내는 형식입니다.

파이썬에서 바이트 문자열은 b'abcd'와 같이 나타내며 내부적으로는 인간이 읽을 수 없는 인코딩된 일련의 바이트들 입니다.

반면에 파이썬에서 u'abcd'와 같이 나타낸 것은 "string" 이라고도 불리며 인간이 읽을 수 있습니다. 문자열은 컴퓨터에 직접 저장할 수 없으므로 먼저 인코딩 (바이트 문자열로 변환)해야합니다. 문자열을 ASCII 및 UTF-8과 같은 바이트 문자열로 변환 할 수있는 여러 인코딩이 있습니다.

```
>>> 'I am a string'.encode ('ascii')
b'I am a string'
>>> 'I am a string'.encode ('utf-16')
b'\xff\xfeI\x00 \x00a\x00m\x00 \x00a\x00 \x00s\x00t\x00r\x00i\x00n\x00g\x00'
```

위의 파이썬 코드는 인코딩 ascii, utf-16를 사용하여 'I am a string'문자열을 인코딩해본 예제입니다. 위 코드의 결과는 바이트 문자열입니다. ascii로 인코딩 된것은 인간이 읽을수 있는것처럼 보이지만 사실은 그렇게 보여줄 뿐입니다. utf-16로 인코딩된 결과를 보면 왜 바이트 문자열이 인간이 읽을 수 없는 것인지 이해가 될것입니다.

인코딩에 사용 된 인코딩을 알고 있으면 바이트 문자열을 다시 문자열로 디코딩 할 수 있습니다.

```
>>> b'I am a string'.decode('ascii')
'I am a string'

>>> b'\xff\xfeI\x00 \x00a\x00m\x00 \x00a\x00 \x00s\x00t\x00r\x00i\x00n\x00g\x00'.decode('utf-16')
'I am a string'

>>> b'\xff\xfeI\x00 \x00a\x00m\x00 \x00a\x00 \x00s\x00t\x00r\x00i\x00n\x00g\x00'.decode('utf-8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
>>> 
```

위의 코드는 바이트 문자열을 디코딩하여 원래 문자열 'I am a string'을 반환합니다. 하지만 마지막의 예제처럼 utf-16으로 인코딩딘 바이트 문자열을 utf-8로 디코딩하면 에러가 발생하게 됩니다.

인코딩 및 디코딩은 역 연산입니다. 모든 것은 디스크에 기록되기 전에 인코딩되어야하며, 인간이 읽을 수 있으려면 먼저 디코딩해야합니다.

참고로 c언어의 char형은 ascii로 인코딩 된 바이트 문자이며 wchar_t는 파이썬의 유니코드와 같은 형식의 문자열임을 기억해두시기 바랍니다. 예를들어 ctypes 라이브러리를 이용해 printf를 실행할 경우 char \* 형을 입력해주어야 하기 때문에 바이트 문자열을 입력값으로 해야합니다.