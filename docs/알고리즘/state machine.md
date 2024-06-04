[CONTENTS](README.md)
## state machine
    #---------------------#
    # CLASS : StateItem
    #---------------------#
    class StateItem():  
      stateMgr = None
      
      def onEnter(self):
        pass
        
      def onUpdate(self):
        pass
        
      def onExit(self):
        pass
      
      def setState(self, state):
        if self.stateMgr:
          self.stateMgr.setState(state)
      
    #---------------------#
    # CLASS : StateMachine
    #---------------------#
    class StateMachine(object):
      stateCount = 0
      stateList = {}
      curState = None
      oldState = None
      
      def __init__(self):
        object.__init__(self)
        self.stateCount = 0
        self.stateList = {}
        self.curState = None
        self.oldState = None
        
      def addState(self, stateItem):
        self.stateList[stateItem] = stateItem()
        self.stateCount = len(self.stateList)
        stateItem.stateMgr = self
      
      def getCount(self):
        return self.stateCount
        
      def isState(self, index):
        return index == self.curState
        
      def getState(self):
        return self.curState
    
      def getStateItem(self):
        if self.curState:
          return self.stateList[self.curState]
    
      def setState(self, index, reset=False):
        if index:
          if index != self.curState:
            self.oldState = self.curState
            self.curState = index
            if self.oldState:
              self.stateList[self.oldState].onExit()
            self.stateList[index].onEnter()
          elif reset:
            self.stateList[index].onEnter()
    
      def updateState(self, *args):
        if self.curState:
          self.stateList[self.curState].onUpdate()
      
      def update(self, dt):
        '''must override'''
        pass
