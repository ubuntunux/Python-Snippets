> [Python Snippets](../README.md) / [각종 조각코드 모음](README.md) / Gabage Collection 사용하기.md
## Gabage Collection 사용하기
Python에는 Gabage Collection이라는 것이 있기 때문에 C/C++ 처럼 메모리를 직접 할당/해제하는 수고를 하지 않아도 되며 메모리를 직접 다룸으로 인해 발생되는 수많은 버그나 위험으로 부터 안전한 편이다. 왜냐하면 Gabage Collection이라는 것이 생성된 객체들을 순회하며 해당 객체가 현재 쓰이는곳이 없을 경우 자동으로 해제를 해주기 때문이다. 그렇다고 사용자가 아무것도 하지 않아서는 안된다. Gabage Collection이 쓸모없어진 객체들을 잘 해제할수 있도록 레퍼런스 카운트에 신경을 써주어야 한다. 특히, 순환참조의 경우는 프로그램이 종료될때까지 메모리에 남아 있게 되므로 특히 주의 하여야 한다.

**예제1) del로 객체 지워보기.**
아래와 같이 a라는 객체를 만들고 del(a)를 하면 객체가 메모리에서 지워짐과 동시에 delete라는 메시지를 출력하도록 하였다.
```
class A:
    def __del__(self):
        print("deleted")
    
a = A()
del(a)
```
결과
```
deleted
```
너무도 뻔하고 쉬운 예제였다. 그렇다면 a를 다른 변수에서 사용되고 있는데 del를 한다면 어떻게 될까?


**예제2) 참조중인 객체 del 실행해보기.**

```
class A:
    def __del__(self):
        print("deleted")
    
a = A()
b = a

del(a)
```
이번 예제는 이전과는 다르게 delete라는 메시지를 출력하지 않는다. 즉, a라는 객체가 메모리에서 지워지지 않았다는 얘기이다. 왜냐하면 b라는 변수에서 a를 참조중이기 때문이다. 아무생각없이 대입하다 보면 메모리 참사가 일어날수도 있따.


**예제3) 참조된 횟수 알아내기 ( 레퍼런스 카운트 )**

```
import sys

class A:
    pass

a = A()
b = a

print(sys.getrefcount(a))
```
결과는 아래와 같이 3이 된다. 기본적으로 오브젝트가 생성이 되었을때 getrefcount로 알아보면 2개가 기본이다. 
```
3
```

**예제4) 오브젝트가 현재 참조중인 목록 알아내기**
```
import gc

def test():
    class A:
        pass

    class B:
        def __init__(self, obj): 
            self.obj = obj

    a = A()
    b = B(a)

    gc.collect() # make sure all garbage cleared before collecting referrers.    
    print( gc.get_referents(b))

test()
```
결과는 뻔하다. b라는 변수는 현재 'obj'라는 멤버변수를 가지고 있고 B라는 클래스로 부터 만들어 졌으므로 아래와 같이 출력된다.
```
[{'obj': <__main__.A object at 0x7fa49038e630>}, <class '__main__.B'>]
```


**예제5) 오브젝트를 참조중인 목록 알아내기**

```
import gc

def test():
    class A:
        pass

    class B:
        def __init__(self, obj): 
            self.obj = obj

    a = A()
    b = B(a)

    gc.collect() # make sure all garbage cleared before collecting referrers.    
    print( gc.get_referrers(a) )
    
test()
```
a를 참조하고 있는 목록이 아래와 같이 리스트로 출력이된다. 이 중에서 frame object는 무시해도 되는듯 하다. 그런데 리스트를 잘 살펴보면 a를 참조중인 오브젝트가 아니라 해당 오브젝트의 \_\_dict\_\_ 가 리스트에 들어있는 것을 볼수있다. 'obj'라는 변수에서 참조중이라는 정보는 알수 있지만 obj 변수의 부모 클래스는 알수가 없다. 
```
[<frame object at 0x7fa4903f9e10>, {'obj': <__main__.test.<locals>.A object at 0x7fa4902dd588>}]
```


**예제6) 현재 자신을 참조중인 오브젝트를 찾아내어 강제로 자신을 지우기.** 이 예제는 객체를 강제로 지워야 할때 유용할것 같다.

```
iimport sys, gc

def delete_me(obj):
    referrers = gc.get_referrers(obj)
    for referrer in referrers:
        if type(referrer) == dict:
            for key, value in referrer.items():
                if value is obj:
                    referrer[key] = None

def test():            
    class A:
        def __del__(self):
                print("deleted")

    class B:
        def __init__(self, obj): 
            self.obj = obj

    a = A()
    b = B(a)

    print("before : ", b.__dict__)
    delete_me(a)
    print("after : ", b.__dict__)
    print("ref count : ", sys.getrefcount(a))
    gc.collect()
    print("ref count : ", sys.getrefcount(a))
    del(a)

test()
```
결과
```
before :  {'obj': <__main__.test.<locals>.A object at 0x7fa4902f02b0>}
after :  {'obj': None}
ref count :  4
ref count :  2
deletedbefore :  {'obj': <__main__.test.<locals>.A object at 0x7fa4903c0940>}
after :  {'obj': None}
```
결과에서 보듯이 a객체는 원래 b객체의 'obj'라는 멤버 변수에서 참조 중이었지만 delete_me 함수로 a를 참조중인 객체들을 추적하여 None을 대입한 결과 b객체의 'obj'에는 None이 대입되었다. 

이제 a의 레퍼런스 카운트를 확인해보자. 분명히 다 a를 참조중인 것들이 다 None이 되었으니 reference count가 기본값인 2가 되어야 할것 같지만 4가 출력되었다. 이유는 Gabage Collection이 아직 불필요한 오브젝트를 지우는 작업을 수행하지 못했기 때문이다. gc.collect() 명령으로 그 작업을 수행할 수 있다. 다시한번 reference count를 확인해보면 이제는 2가 되었을음 확인 할수있다. 그럼이제 del(a)명령으로 a객체를 지울수있다.