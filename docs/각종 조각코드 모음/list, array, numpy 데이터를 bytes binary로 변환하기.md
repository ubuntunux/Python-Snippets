numpy 또는 list 등을 binary 데이터로 저장하고 싶을때나 반대로 binary data를 numpy나 list로 변환하고 싶을때가 있다. 이럴때 사용해보자.

데이터 변환문자 참고
[https://docs.python.org/3/library/struct.html](https://docs.python.org/3/library/struct.html)
[https://docs.python.org/3/library/array.html](https://docs.python.org/3/library/array.html)
[https://docs.scipy.org/doc/numpy-1.13.0/user/basics.types.html](https://docs.scipy.org/doc/numpy-1.13.0/user/basics.types.html)

##### int를 binary로 변환
```
>>> struct.pack('i', 1)
b'\x01\x00\x00\x00'
>>> struct.pack('ii', 77, 88)
b'M\x00\x00\x00X\x00\x00\x00'
```

##### binary를 int로 변환
```
>>> struct.unpack('i', b'\x01\x00\x00\x00')
(1,)
>>> struct.unpack('ii', b'M\x00\x00\x00X\x00\x00\x00')
(77, 88)
```

##### float list를 binary로 변환
```
>>> x = array('f', [3.141592, 7.2])
>>> bytes(x)
b'\xd8\x0fI@ff\xe6@'
```

##### binary를 float list로 변환
```
# [3.141592, 7.2]
>>> data = b'\xd8\x0fI@ff\xe6@' 
>>> list(array('f', data)
[3.141592025756836, 7.199999809265137]
```

##### binary를 numpy float list로 변환
```
# [3.141592, 7.2]
>>> data = b'\xd8\x0fI@ff\xe6@'  
>>> np.frombuffer(data, dtype=np.float32)
array([ 3.14159203,  7.19999981], dtype=float32)
```


##### numpy float list를 binary로 변환
```
>>> np.array([ 3.14159203,  7.19999981], dtype=np.float32).tobytes()
b'\xd8\x0fI@ff\xe6@'
```

