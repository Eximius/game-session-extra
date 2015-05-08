
from GameSession import GameSession

import sys

if len(sys.argv) < 2:
    print('usage: FA.exe [args...]')
    sys.exit(0)

from PyQt5.QtCore import *

app = QCoreApplication(sys.argv)

sess = GameSession()

i = 2
while i < len(sys.argv):
    assert sys.argv[i][0] == '/'
    j = i+1
    while j < len(sys.argv) and sys.argv[j][0] != '/':
        j += 1
    sess.addArg(sys.argv[i][1:], *sys.argv[i+1:j])
    i = j

sess.start(sys.argv[1])

excepthook_original = sys.excepthook
def excepthook(exc_type, exc_value, traceback_object):
    """
    This exception hook will stop the app if an uncaught error occurred, regardless where in the QApplication.
    """

    sys.excepthook = excepthook_original
    app.exit(0)

sys.excepthook = excepthook

interpreter_timer = QTimer(app)
interpreter_timer.start(500)
interpreter_timer.timeout.connect(lambda: None)

app.exec_()