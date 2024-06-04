> [Python Snippets](../README.md) / [알고리즘](README.md) / multi method 오버로드.md
## multi method 오버로드
    #---------------------#
    # MultiMethod
    #---------------------#
    registry = {}
    
    class MultiMethod(object):
        def __init__(self, name):
            self.name = name
            self.typemap = {}
        def __call__(self, *args):
            types = tuple(arg.__class__ for arg in args) # a generator expression!
            function = self.typemap.get(types)
            if function is None:
                raise TypeError("no match")
            return function(*args)
        def register(self, types, function):
            if types in self.typemap:
                raise TypeError("duplicate registration")
            self.typemap[types] = function
    
    def multimethod(*types):
        def register(function):
            name = function.__name__
            mm = registry.get(name)
            if mm is None:
                mm = registry[name] = MultiMethod(name)
            mm.register(types, function)
            return mm
        return register
        
    overload = multimethod
    
    @overload()  
    def getX():
      return cX
      
    @overload(int)  
    def getX(a):
      return cX*a
    
    @overload(int, int)
    def getX(a,b):
      return cX*b