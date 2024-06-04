[CONTENTS](README.md)
## ui 파일 불러오기
    from PyQt4 import QtGui, uic
    
    class Window(QtGui.QMainWindow):
        def __init__(self):
            super(Window, self).__init__()
            uic.loadUi('form.ui', self)
    
    if __name__ == '__main__':
        app = QtGui.QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec_())