[CONTENTS](README.md)
## 클로저 ( closure )
클로저(closure)는 일반 함수와 달리 생성당시의 상태를 저장할 수 있다는 점에서 굉장히 유용하게 사용된다.
하지만 반복문 안에서 closure가 사용될때에는 주의할 점이 한가지 있는데 바로 마지막으로 실행된 closure만이 적용된다는 점에 주의해야 한다.
한가지 예를 들어 아래와 같이 람다 함수로 0 ~  4 까지의 숫자를 출력하는 함수를 functions 리스트에 담았다고 치자.

    functions = []
    for i in range(5):
    	functions.append( lambda : print(i) )
    
이제 함수들을 실행하여 숫자를 출력해보자.
    
    for func in functions:
    	func()
    
    4
    4
    4
    4
    4

의도와는 다르게 숫자 4가 5번 출력되고 만다. 마지막 closure만이 저장되었기 때문이다. id로 확인해봐도 5개의 람다함수 모두 같은 id이다. 이것을 해결하는 방법중 한가지는 functiools 모듈을 사용하는 것이다. 이제 아래와 같이 수정해보자.

    from functools import partial
    functions = []
    for i in range(5):
    	functions.append( partial(print, i) )

자, 다시한번 출력해보자.

    for func in functions:
    	func()
    
    0
    1
    2
    3
    4

자~~~알~ 작동한다!!