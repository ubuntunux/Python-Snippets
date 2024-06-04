> [Python Snippets](../../README.md) / [GUI](../README.md) / [PyQt](README.md) / item 얻어오기.md
## item 얻어오기
    class Window(QtGui.QMainWindow):
        def __init__(self):
            super(Window, self).__init__()
            uic.loadUi('UI/editor.ui', self)
            item = self.findChild(QtGui.QHBoxLayout, "horizontalLayout")