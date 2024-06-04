[CONTENTS](README.md)
## pickle을 사용해서 데이타 저장하고 불러오기
데이터를 저장하고 불러올때 매우 유용한 라이브러리이다.

어떨때 유용한고 하니~ 클래스 자체를 통째로 파일로 저장했다가 그것을 그대로 불러올수도 있다.

당연히 파일을 불러오면 클래스가 그대로 복원이된다. 

그리고 또한가지 유용한 경우는 list, dictionary등을 파일 그대로 저장하면 용량이 매우 커지는데 pickle을 사용하면 binary형태로 저장되기 때문에 용량이 매우 작아진다.

binary형태로 직접 저장하는 방법도 있지만 pickle을 이용하지 않으면 매우매우~~~  복잡하고 귀찮아 진다.

** data를 pickle로 저장하기 **

```
import pickle

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

# save
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    
# load
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
```

추가적으로 gzip을 이용하여 pickle로 저장된 데이터를 압축하고 해제하는 예제이다. 당연히 대부분은 용량이 매우 줄어든다.

```
import pickle
import gzip

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

# save and compress.
with gzip.open('testPickleFile.pickle', 'wb') as f:
    pickle.dump(data, f)

# load and uncompress.
with gzip.open('testPickleFile.pickle','rb') as f:
    data = pickle.load(f)
```