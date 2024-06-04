> [Python Snippets](../../README.md) / [각종 조각코드 모음](../README.md) / [멤버 변수에 직접 접근할 것인가  아니면 getter ](README.md) /  setter 패턴을 사용할 것인가.md
##  setter 패턴을 사용할 것인가
객체지향을 추구하는 언어의 대부분에서는 멤버변수에 대한 직접 접근을 꺼린다.
대부분 get/set과 같은 패턴으로 멤버변수에 대한 인터페이스를 작성하기 마련이다.

하지만 파이썬에서는 조금 다른 방법이 조금더 pythonic한 방법인듯 하다.

**첫번째 방법**
    - 평소에는 멤버변수를 직접접근해서 사용하다가 아래와 같이 변수를 얻기전에 무언가를 해야하는 경우가 생기면 propery 데코레이터를 사용하여 wrap 하는 것이 가능하다. 멤버변수를 직접 접근하듯이 사용하면 된다.

x라는 변수에 대해 직접접근해서 사용하는 것처럼 그대로 접근할 수 있다.

    class P:
        def __init__(self,x):
            self.x = x
    
        @property
        def x(self):
            return self.__x
    
        @x.setter
        def x(self, x):
            if x < 0:
                self.__x = 0
            elif x > 1000:
                self.__x = 1000
            else:
                self.__x = x


아래와 같이 구현 할 수도 있다. 결과는 같다.
    
    class P:    
        def __init__(self,x):
            self.set_x(x)
    
        def get_x(self):
            return self.__x
    
        def set_x(self, x):
            if x < 0:
                self.__x = 0
            elif x > 1000:
                self.__x = 1000
            else:
                self.__x = x
    
        x = property(get_x, set_x)
