> [Python Snippets](../README.md) / [알고리즘](README.md) / 여러가지 싱글톤(singleton) 구현방법.md
## 여러가지 싱글톤(singleton) 구현방법
[http://mataeoh.egloos.com/7081556](http://mataeoh.egloos.com/7081556)

Method 1: Method type

여기 예제중에서 call 속도도 가장 빠르고 여러가지 상속이나 기타 상황에서 가장 문제가 없는 방식이다.
사용 방식은 C/C++에서 자주사용하는 방식과 비슷하게 직접 instance 메소드를 실행하는 방법이다.
상속 순서역시 가장 뒤에 와도 상관없기 때문에 가장 좋은 방법인것 같다.
    
    class SingletonInstane:
      __instance = None
    
      @classmethod
      def __getInstance(cls):
        return cls.__instance
    
      @classmethod
      def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance
    
    class MyClass(BaseClass, SingletonInstane):
      pass
    
    c = MyClass.instance()


Method 2: A decorator

빠르지만 클래스 자체를 호출할경우 함수가 리턴되기 때문에 클래스의 StaticMethod에 접근할수가 없다..

    def singleton(class_):
      instances = {}
      def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
      return getinstance
    
    @singleton
    class MyClass(BaseClass):
      pass

  
  
Method 3: A base class

데코레이터 타입의 싱글톤보다 아주 살짝 느리지만 일반적인 클래스처럼 쓸 수가 있기 때문에 가장 범용적이다.

    class Singleton(object):
      _instance = None
      def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance
    
    class MyClass(Singleton, BaseClass):
      pass
  
  
  
Method 4: A metaclass

    class Singleton(type):
        _instances = {}
        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instances[cls]
    
    #Python2
    class MyClass(BaseClass):
        __metaclass__ = Singleton
    
    #Python3
    class MyClass(BaseClass, metaclass=Singleton):
        pass
    
    
    
Method 5: decorator returning a class with the same name

    def singleton(class_):
      class class_w(class_):
        _instance = None
        def __new__(class_, *args, **kwargs):
          if class_w._instance is None:
              class_w._instance = super(class_w, 
                                        class_).__new__(class_, 
                                                        *args, 
                                                        **kwargs)
              class_w._instance._sealed = False
          return class_w._instance
        def __init__(self, *args, **kwargs):
          if self._sealed:
            return
          super(class_w, self).__init__(*args, **kwargs)
          self._sealed = True
      class_w.__name__ = class_.__name__
      return class_w
    
    @singleton
    class MyClass(BaseClass):
        pass