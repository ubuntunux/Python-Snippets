[Previous](..)
## 람다(lambda)대신 고차함수 partial 활용하기
lambda대신 partial로 함수를 만들어 넘길때 자주 사용한다. 알아보자

    from functools import partial
    
    def sum(a, b):
        print(a+b)
        
    f = partial(sum, 10)   
    f(1)

##### 결과

    11


여기서 집고 넘어가야할 중요한게 있다.

바로 lambda와 partial은 서로 비슷하지만 차이점이 있다는 것. 람다의 경우 숫자 4만 5번출력하는데 이렇게 되는 이유는 람다가 평가될때가 되서야 비로서 코드가 생성되기 때문에 loop에서 마지막 값인 4가 출력되는 것이다. 반면 partial에 의한 함수는 생성될때 평가되므로 결과가 다른 것이다.

#### 람다예제

    funcs = []
    for i in range(5):
        funcs.append(lambda : print(i))
        
    for f in funcs:
        f()
        
##### 결과

    4
    4
    4
    4
    4

#### Partial 예제
    
    from functools import partial
    funcs = []
    for i in range(5):
        funcs.append(partial(print, i))
        
    for f in funcs:
        f()

##### 결과

    0
    1
    2
    3
    4