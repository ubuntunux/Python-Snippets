    class Window(QtGui.QMainWindow):
        def __init__(self):
            super(Window, self).__init__()
            uic.loadUi('UI/editor.ui', self)
            item = self.findChild(QtGui.QHBoxLayout, "horizontalLayout")