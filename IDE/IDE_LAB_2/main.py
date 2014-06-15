#!usr/bin/python
import sys
from PyQt4 import QtGui
from simulatron_v1 import Ui_App

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    obj = Ui_App()
    obj.show()
    sys.exit(app.exec_())
    