[CONTENTS](README.md)
## 단위테스트 ( UnitTest )
유닛테스트는 왜 필요한가?


    #---------------------#
    # CLASS : StateItem
    #---------------------#
    class StateItem:
      def __init__(self, stateMgr, name):
        self.stateMgr = stateMgr
        self.name = name
    
      def onEnter(self):
        """
        override method
        """
        pass
    
      def onUpdate(self):
        """
        override method
        """
        pass
    
      def onExit(self):
        """
        override method
        """
        pass
    
      def getName(self):
          return self.name
    
      def setState(self, state):
        self.stateMgr.setState(state)
    
    
    #---------------------#
    # CLASS : StateMachine
    #---------------------#
    class StateMachine(object):
      def __init__(self):
        self.stateCount = 0
        self.stateList = {}
        self.curState = None
        self.oldState = None
    
      def createState(self, stateName):
        stateItem = StateItem(self, stateName)
        # stateItem is selfKey and value
        self.stateList[stateItem] = stateItem
        self.stateCount = len(self.stateList)
        return stateItem
    
      def getCount(self):
        return self.stateCount
    
      def isState(self, state):
        return state == self.curState
    
      def isStateName(self, stateName):
        return stateName == self.curState.name
    
      def getState(self):
        return self.curState
    
      def getStateName(self):
        return self.curState.name
    
      def setState(self, state, reset=False):
          if state != self.curState:
            self.oldState = self.curState
            self.curState = state
            if self.oldState:
              self.stateList[self.oldState].onExit()
            self.stateList[state].onEnter()
          elif reset:
            self.stateList[state].onEnter()
    
      def updateState(self, *args):
        if self.curState:
          self.stateList[self.curState].onUpdate()
    
    if __name__ == '__main__':
        import unittest
        class testStateMachine(unittest.TestCase):
            def test(self):
                s = StateMachine()
                state_A = s.createState(stateName="state_A")
                state_B = s.createState(stateName="state_B")
    
                s.setState(state_A)
                self.assertEqual(state_A, s.getState())
                self.assertEqual("state_A", s.getStateName())
    
                s.setState(state_B)
                self.assertTrue(s.isState(state_B))
                self.assertTrue(s.isStateName("state_B"))
    
                self.assertEqual(s.getCount(), 2)
        unittest.main()

----
또다른 예제


    import numpy as np
    import unittest
    from Utilities import Logger
    
    
    class Vector(object):
        def __init__(self, *args):
            self.length = len(args)
            self._vec = np.array(args)
    
        def __getitem__(self, index):
            return self._vec[index]
    
        def __setitem__(self, key, value):
            self._vec[key] = value
    
        def __mul__(self, other):
            return Vector()
    
        def __str__(self):
            return str(self._vec)
    
        def __add__(self, other):return self._vec + other._vec
        def __iadd__(self, other):return self._vec + other._vec
        def __sub__(self, other):return self._vec - other._vec
        def __isub__(self, other):return self._vec - other._vec
        def __mul__(self, other):return self._vec * other._vec
        def __imul__(self, other):return self._vec * other._vec
        def __idiv__(self, other):return self._vec / other._vec
        def __floordiv__(self, other):return self._vec / other._vec
    
        def norm(self):
            return np.linalg.norm(self._vec)
    
        def normalize(self):
            norm = np.linalg.norm(self._vec)
            if norm > 0.0:
                return Vector(*self._vec / norm)
            else:
                return Vector(*((0.0, ) * self.length))
    
        def dot(self, other):
            return np.dot(self._vec, other._vec)
    
        def cross(self, other):
            return Vector(*np.cross(self._vec, other._vec))
    
    if __name__ == '__main__':
        class test(unittest.TestCase):
            def testVector(self):
                vector = Vector(-1, -2, 3.5)
                other = Vector(1, 2, 3)
                logger = Logger.getLogger()
                logger.info("Test create vector : %s" % vector)
                logger.info("Test normalize : %s" % vector.normalize())
                logger.info("Test dot : %s" % vector.dot(other))
                logger.info("Test cross : %s" % vector.cross(other))
        unittest.main()